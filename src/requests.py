import asyncpg
from fastapi import Request as BaseRequest


class RequestState:
    db_pool: asyncpg.Pool


class Request(BaseRequest):

    @property
    def state(self) -> RequestState:
        return super().state()
