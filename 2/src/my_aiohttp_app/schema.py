from copy import deepcopy
from dataclasses import fields
from typing import Any

from my_aiohttp_app.dto import Repository


class RepositoryResponseSchema:
    dataclass_fields = {f.name for f in fields(Repository)}

    @classmethod
    def load(cls, response_data: dict[str, Any]):
        repository_data = deepcopy(response_data)
        repository_data["owner"] = repository_data["owner"]["login"]
        return {k: v for k, v in repository_data.items() if k in cls.dataclass_fields}
