from dataclasses import dataclass
from datetime import date, datetime


@dataclass(kw_only=True, slots=True)
class RepositorySchema:
    name: str
    owner: str
    stars: int
    watchers: int
    forks: int
    language: str
    updated: datetime


@dataclass(kw_only=True, slots=True)
class RepositoriesAuthorsCommitsSchema:
    date: date
    repo: str
    author: str
    commits_num: int


@dataclass(kw_only=True, slots=True)
class RepositoriesPositionsSchema:
    date: date
    repo: str
    position: int
