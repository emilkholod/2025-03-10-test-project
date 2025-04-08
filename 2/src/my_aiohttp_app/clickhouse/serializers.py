from typing import Any, override

from my_aiohttp_app.clickhouse import schemas
from my_aiohttp_app.core.serializer import Serializer


class RepositorySerializer(Serializer[schemas.RepositoryClickhouseSchema]):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()

        transformed_data.pop("position", None)
        transformed_data.pop("authors_commits_num_today", None)

        return transformed_data


class RepositoriesAuthorsCommitsSerializer(
    Serializer[schemas.RepositoriesAuthorsCommitsClickhouseSchema]
):
    pass


class RepositoriesPositionsSerializer(
    Serializer[schemas.RepositoriesPositionsClickhouseSchema]
):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()

        transformed_data["repo"] = transformed_data["name"]

        return transformed_data
