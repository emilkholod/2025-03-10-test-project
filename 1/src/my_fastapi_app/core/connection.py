import asyncpg

from my_fastapi_app.core.request import Request


async def get_pg_connection(
    request: Request,
) -> asyncpg.Connection:
    async with request.state.db_pool.acquire() as conn:
        yield conn
