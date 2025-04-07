from abc import ABC
from copy import deepcopy
from dataclasses import fields
from typing import (
    Any,
    Generic,
    Type,
    TypeVar,
    cast,
    get_args,
    override,
)

from my_aiohttp_app import dto
from my_aiohttp_app.utils import DataclassInstance

T = TypeVar("T", bound=DataclassInstance)


class ResponseSchema(ABC, Generic[T]):
    @property
    def dto_model(self) -> Type[T]:
        return cast(
            Type[T], get_args(self.__orig_bases__[0])[0]  # type: ignore[attr-defined]
        )

    def __init__(self, **response_data: Any):
        self.response_data = deepcopy(response_data)

    @property
    def dataclass_fields(self) -> set[str]:
        return {f.name for f in fields(self.dto_model)}

    def load(self) -> dict[str, Any]:
        transformed_data = self.transform()
        try:
            result = {
                k: v for k, v in transformed_data.items() if k in self.dataclass_fields
            }
        except KeyError as e:
            raise RuntimeError(f"Missing expected key: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error during data transformation: {e}")
        return result

    def get_object(self) -> T:
        return self.dto_model(**self.load())

    def transform(self) -> dict[str, Any]:
        return deepcopy(self.response_data)


class RepositoryResponseSchema(ResponseSchema[dto.Repository]):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()
        transformed_data["owner"] = transformed_data["owner"]["login"]
        return transformed_data


class RepositoryAuthorCommitsNumSchema(ResponseSchema[dto.RepositoryAuthorCommitsNum]):
    pass
