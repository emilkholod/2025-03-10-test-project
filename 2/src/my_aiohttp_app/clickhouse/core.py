from abc import ABC, abstractmethod
from dataclasses import astuple, fields
from itertools import batched

from aiohttp import ClientSession

from my_aiohttp_app.clickhouse.client import get_client


class ClickhouseManager(ABC):
    def __init__(self, session: ClientSession | None = None):
        self.session = session

    @property
    @abstractmethod
    def tablename(self) -> str:
        pass

    @property
    @abstractmethod
    def schema(self):
        pass

    async def write(self, rows: list):
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
