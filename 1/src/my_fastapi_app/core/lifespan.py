from contextlib import asynccontextmanager
from typing import AsyncIterator, TypedDict

import asyncpg
from fastapi import FastAPI

from my_fastapi_app.core.config import get_settings


class LifeSpanState(TypedDict):
    db_pool: asyncpg.Pool


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[LifeSpanState]:
    settings = await get_settings()

    db_settings = settings.DATABASE_SETTINGS

    db_pool = await asyncpg.create_pool(
        user=db_settings.DB_USER,
        password=db_settings.DB_PASSWORD,
        database=db_settings.DB_NAME,
        host=db_settings.DB_HOST,
        port=db_settings.DB_PORT,
    )

    yield {
        "db_pool": db_pool,
    }

    await db_pool.close()
