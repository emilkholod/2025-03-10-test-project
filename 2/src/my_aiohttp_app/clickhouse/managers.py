from my_aiohttp_app.clickhouse import schemas
from my_aiohttp_app.clickhouse.core import ClickhouseManager


class RepositoryManager(ClickhouseManager):
    tablename = "test.repositories"
    schema = schemas.RepositoryClickhouseSchema


class RepositoriesAuthorsCommitsManager(ClickhouseManager):
    tablename = "test.repositories_authors_commits"
    schema = schemas.RepositoriesAuthorsCommitsClickhouseSchema


class RepositoriesPositionsManager(ClickhouseManager):
    tablename = "test.repositories_positions"
    schema = schemas.RepositoriesPositionsClickhouseSchema
