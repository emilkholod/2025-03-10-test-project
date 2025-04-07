import asyncio
from dataclasses import Field
from functools import wraps
from typing import Any, ClassVar, Protocol

from aiohttp import ClientError


class RetryException(Exception):
    def __init__(self, *args, retry_in_seconds=None):
        super().__init__()
        self.retry_in_seconds = max(retry_in_seconds, 1)


async def retry(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        last_exception = None
        for attempt in range(3):
            try:
                result = await func(*args, **kwargs)
                break
            except RetryException as e:
                await asyncio.sleep(e.retry_in_seconds)
                last_exception = e
            except (asyncio.TimeoutError, ClientError) as e:
                await asyncio.sleep(2**attempt)  # Экспоненциальная задержка
                last_exception = e
        else:
            raise RuntimeError(f"Request failed: {last_exception}")
        return result

    return wrapper


class DataclassInstance(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]
