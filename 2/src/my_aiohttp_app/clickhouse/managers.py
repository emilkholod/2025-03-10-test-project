from my_aiohttp_app.clickhouse import schemas
from my_aiohttp_app.clickhouse.core import create_clickhouse_manager

RepositoryManager = create_clickhouse_manager(
    tablename="test.repositories",
    schema=schemas.RepositoryClickhouseSchema,
)

RepositoriesAuthorsCommitsManager = create_clickhouse_manager(
    tablename="test.repositories_authors_commits",
    schema=schemas.RepositoriesAuthorsCommitsClickhouseSchema,
)

RepositoriesPositionsManager = create_clickhouse_manager(
    tablename="test.repositories_positions",
    schema=schemas.RepositoriesPositionsClickhouseSchema,
)
