from abc import ABC
from copy import deepcopy
from dataclasses import asdict, fields
from functools import singledispatchmethod
from typing import (
    Any,
    Generic,
    Type,
    TypeVar,
    cast,
    get_args,
)

from my_aiohttp_app.utils import DataclassInstance

T = TypeVar("T", bound=DataclassInstance)


class Serializer(ABC, Generic[T]):
    @property
    def target_model(self) -> Type[T]:
        return cast(
            Type[T], get_args(self.__orig_bases__[0])[0]  # type: ignore[attr-defined]
        )

    @singledispatchmethod  # type: ignore[misc]
    def __init__(self, response_data):
        raise NotImplementedError()

    @__init__.register
    def _(self, response_data: dict):
        self.response_data = deepcopy(response_data)

    @__init__.register
    def _(self, response_data: DataclassInstance):
        self.response_data = asdict(response_data)

    @property
    def dataclass_fields(self) -> set[str]:
        return {f.name for f in fields(self.target_model)}

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

    def get_object(self, **defaults) -> T:
        defaults = defaults or {}
        return self.target_model(**self.load(), **defaults)

    def transform(self) -> dict[str, Any]:
        transformed_data = deepcopy(self.response_data)
        return transformed_data
