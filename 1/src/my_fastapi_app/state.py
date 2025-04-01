from dataclasses import dataclass

import asyncpg
from fastapi import Request


@dataclass
class State:
    db_pool: asyncpg.Pool


async def get_state(request: Request) -> State:
    db_pool = request.state.db_pool
    return State(db_pool)
