import uvicorn
from fastapi import FastAPI

from my_fastapi_app.core.lifespan import lifespan
from my_fastapi_app.routers import api, redirects


def register_routes(app: FastAPI) -> None:
    app.include_router(api.router)
    app.include_router(redirects.router)


def create_app() -> FastAPI:
    app = FastAPI(title="e-Comet", lifespan=lifespan)
    register_routes(app)
    return app


if __name__ == "__main__":
    uvicorn.run("my_fastapi_app.main:create_app", factory=True)
