from my_aiohttp_app.clickhouse.core import ClickhouseManager
from my_aiohttp_app.clickhouse.schemas import (
    RepositoriesAuthorsCommitsSchema,
    RepositoriesPositionsSchema,
    RepositorySchema,
)


class RepositoryManager(ClickhouseManager):
    tablename = "test.repositories"
    schema = RepositorySchema


class RepositoriesAuthorsCommitsManager(ClickhouseManager):
    tablename = "test.repositories_authors_commits"
    schema = RepositoriesAuthorsCommitsSchema


class RepositoriesPositionsManager(ClickhouseManager):
    tablename = "test.repositories_positions"
    schema = RepositoriesPositionsSchema
