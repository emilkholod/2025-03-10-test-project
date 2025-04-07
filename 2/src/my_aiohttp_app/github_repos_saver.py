from datetime import datetime

from aiohttp import ClientSession

from my_aiohttp_app.clickhouse import managers, serializers
from my_aiohttp_app.dto import Repository


async def save_repositories(repositories: list[Repository]):
    ch_repos = []
    updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for repo in repositories:
        ch_repo = serializers.RepositorySerializer(repo).get_object(
            updated=updated,
        )
        ch_repos.append(ch_repo)

    async with ClientSession() as session:
        await managers.RepositoryManager(session).write(ch_repos)

    ch_repo_authors_commits = []
    today = datetime.today().strftime("%Y-%m-%d")
    for repo in repositories:
        for authors_commits_num_today in repo.authors_commits_num_today:
            ch_repo_author_commit = serializers.RepositoriesAuthorsCommitsSerializer(
                authors_commits_num_today
            ).get_object(date=today, repo=repo.name)
            ch_repo_authors_commits.append(ch_repo_author_commit)

    async with ClientSession() as session:
        await managers.RepositoriesAuthorsCommitsManager(session).write(
            ch_repo_authors_commits
        )

    ch_repos_position = []
    today = datetime.today().strftime("%Y-%m-%d")
    for repo in repositories:
        ch_repo_position = serializers.RepositoriesPositionsSerializer(repo).get_object(
            date=today,
        )
        ch_repos_position.append(ch_repo_position)

    async with ClientSession() as session:
        await managers.RepositoriesPositionsManager(session).write(ch_repos_position)
