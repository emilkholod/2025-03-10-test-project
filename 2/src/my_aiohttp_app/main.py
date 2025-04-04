import asyncio
from collections import Counter
from datetime import datetime, timedelta
from itertools import count
from typing import Any, Final

from aiohttp import ClientSession
from aiolimiter import AsyncLimiter

from my_aiohttp_app import config
from my_aiohttp_app.dto import Repository, RepositoryAuthorCommitsNum
from my_aiohttp_app.schema import RepositoryResponseSchema
from my_aiohttp_app.utils import RetryException, retry

GITHUB_API_BASE_URL: Final[str] = "https://api.github.com"


class GithubReposScrapper:
    semaphore = asyncio.Semaphore(config.MCR)
    limiter = AsyncLimiter(config.RPS)

    def __init__(self, session: ClientSession):
        self.session = session

    @retry
    async def _make_request(
        self, endpoint: str, method: str = "GET", params: dict[str, Any] | None = None
    ) -> Any:
        url = f"{GITHUB_API_BASE_URL}/{endpoint}"
        async with self.session.request(method, url, params=params) as response:
            if response.status == 403:
                reset_time = response.headers.get("X-RateLimit-Reset")
                if reset_time:
                    sleep_time = int(reset_time) - int(datetime.now().timestamp())
                    raise RetryException(retry_in_seconds=sleep_time)
            elif response.status >= 400:
                raise RuntimeError(
                    f"GitHub API error {response.status}:" f" {await response.text()}"
                )

            return await response.json()

    async def _get_top_repositories(self, limit: int = 100) -> list[dict[str, Any]]:
        """
        GitHub REST API:
        https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
        """
        data = await self._make_request(
            endpoint="search/repositories",
            params={
                "q": "stars:>1",
                "sort": "stars",
                "order": "desc",
                "per_page": limit,
            },
        )
        return data["items"]

    async def _get_repository_commits(
        self,
        owner: str,
        repo: str,
        params: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """
        GitHub REST API:
        https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#list-commits
        """
        commits = []
        for page in count(1):
            async with self.semaphore, self.limiter:
                data = await self._make_request(
                    endpoint=f"repos/{owner}/{repo}/commits",
                    params={**(params or {}), "per_page": 100, "page": page},
                )
                if data:
                    commits.extend(data)
                else:
                    break
                if len(data) < 100:
                    break
        return commits

    async def get_repositories(self, limit: int = 100) -> list[Repository]:
        repositories_data = await self._get_top_repositories(limit)
        if not repositories_data:
            return []

        repositories = [
            Repository(**RepositoryResponseSchema.load(r)) for r in repositories_data
        ]

        params = {"since": (datetime.now() - timedelta(days=1)).isoformat()}
        tasks = [
            self._get_repository_commits(r.owner, r.name, params=params)
            for r in repositories
        ]
        results = await asyncio.gather(*tasks)

        for repo, author_commits_num in zip(repositories, results):
            if isinstance(author_commits_num, Exception):
                continue

            commits_per_author = Counter(
                c["commit"]["author"]["name"] for c in author_commits_num
            )
            repo.authors_commits_num_today = [
                RepositoryAuthorCommitsNum(author=author, commits_num=commits_num)
                for author, commits_num in commits_per_author.items()
            ]

        return repositories
