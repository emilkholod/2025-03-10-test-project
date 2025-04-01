import asyncpg

from my_fastapi_app.core.state import RequestState


async def get_pg_connection(
    state: RequestState,
) -> asyncpg.Connection:
    async with state.db_pool.acquire() as conn:
        yield conn
