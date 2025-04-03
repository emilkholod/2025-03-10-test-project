import asyncpg
from fastapi import Request as BaseRequest
from starlette.datastructures import State as BaseState


class State(BaseState):
    db_pool: asyncpg.Pool


class Request(BaseRequest):
    state: State
