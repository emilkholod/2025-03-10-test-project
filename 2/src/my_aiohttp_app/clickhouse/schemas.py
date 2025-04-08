from dataclasses import dataclass
from datetime import date, datetime


@dataclass(kw_only=True, slots=True)
class RepositoryClickhouseSchema:
    name: str
    owner: str
    stars: int
    watchers: int
    forks: int
    language: str
    updated: datetime


@dataclass(kw_only=True, slots=True)
class RepositoriesAuthorsCommitsClickhouseSchema:
    date: date
    repo: str
    author: str
    commits_num: int


@dataclass(kw_only=True, slots=True)
class RepositoriesPositionsClickhouseSchema:
    date: date
    repo: str
    position: int
