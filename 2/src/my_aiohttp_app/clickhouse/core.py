from abc import ABC
from dataclasses import astuple, fields
from itertools import batched
from typing import (
    Generic,
    Type,
    TypeVar,
    cast,
    get_args,
)

from aiohttp import ClientSession

from my_aiohttp_app.clickhouse.client import get_client
from my_aiohttp_app.utils import DataclassInstance

T = TypeVar("T", bound=DataclassInstance)


class ClickhouseManager(ABC, Generic[T]):
    tablename: str

    def __init__(self, session: ClientSession | None = None):
        self.session = session

    @property
    def schema(self) -> Type[T]:
        return cast(
            Type[T], get_args(self.__orig_bases__[0])[0]  # type: ignore[attr-defined]
        )

    async def write(self, rows: list[T]):
        if not rows:
            return  # Нечего вставлять

        client = get_client(self.session)
        column_names = ", ".join(f.name for f in fields(self.schema))
        query = f"INSERT INTO {self.tablename} ({column_names}) VALUES"

        try:
            for sub_rows in batched(rows, 100):
                if sub_rows:  # batched может вернуть None
                    await client.execute(query, *map(astuple, sub_rows))
        except Exception as e:
            raise RuntimeError(f"Ошибка при записи в ClickHouse: {e}")


def create_clickhouse_manager(
    *, tablename: str, schema: Type[T]
) -> type[ClickhouseManager[T]]:
    tablename_ = tablename

    class _ClickhouseManager(ClickhouseManager[schema]):  # type: ignore[valid-type]
        tablename = tablename_

    return _ClickhouseManager
