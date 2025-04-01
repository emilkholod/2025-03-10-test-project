from dataclasses import dataclass
from typing import Annotated

import asyncpg
from fastapi import Depends, Request


@dataclass
class State:
    db_pool: asyncpg.Pool


async def get_state(request: Request) -> State:
    db_pool = request.state.db_pool
    return State(db_pool)


TypedState = Annotated[State, Depends(get_state)]
