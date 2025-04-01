from contextlib import asynccontextmanager
from typing import AsyncIterator, TypedDict

import asyncpg
from fastapi import FastAPI

from my_fastapi_app.config import get_settings


class LifeSpanState(TypedDict):
    db_pool: asyncpg.Pool


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[LifeSpanState]:
    settings = get_settings()

    db_pool = await asyncpg.create_pool(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )

    yield {
        "db_pool": db_pool,
    }

    await db_pool.close()
