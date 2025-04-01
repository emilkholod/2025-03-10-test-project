from typing import Annotated, Any

import asyncpg
import uvicorn
from fastapi import APIRouter, Depends, FastAPI
from fastapi.responses import RedirectResponse

from my_fastapi_app.core.lifespan import lifespan
from my_fastapi_app.core.state import RequestState


async def get_pg_connection(
    state: RequestState,
) -> asyncpg.Connection:
    async with state.db_pool.acquire() as conn:
        yield conn


async def get_db_version(
    conn: Annotated[asyncpg.Connection, Depends(get_pg_connection)],
) -> Any:
    return await conn.fetchval("SELECT version()")


async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")


def register_routes(app: FastAPI) -> None:
    router = APIRouter(prefix="/api")
    router.add_api_route(path="/db_version", endpoint=get_db_version)
    app.include_router(router)
    app.add_api_route(path="/", endpoint=redirect_to_docs, include_in_schema=False)


def create_app() -> FastAPI:
    app = FastAPI(title="e-Comet", lifespan=lifespan)
    register_routes(app)
    return app


if __name__ == "__main__":
    uvicorn.run("my_fastapi_app.main:create_app", factory=True)
