from typing import Annotated, Any

import asyncpg
from fastapi import APIRouter, Depends

from my_fastapi_app.core.connection import get_pg_connection

router = APIRouter(prefix="/api")


@router.get("/db_version")
async def get_db_version(
    conn: Annotated[asyncpg.Connection, Depends(get_pg_connection)],
) -> Any:
    return await conn.fetchval("SELECT version()")
