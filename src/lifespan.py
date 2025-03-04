from contextlib import asynccontextmanager
from typing import AsyncIterator

import asyncpg
from fastapi import FastAPI

import config


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    db_pool = await asyncpg.create_pool(
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        host=config.DB_HOST,
        port=config.DB_PORT,
    )

    yield {
        "db_pool": db_pool,
    }

    await db_pool.close()
