from typing import Any, override

from my_aiohttp_app.clickhouse import schemas
from my_aiohttp_app.core.serializer import Serializer


class RepositorySerializer(Serializer[schemas.RepositorySchema]):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()

        transformed_data.pop("position", None)
        transformed_data.pop("authors_commits_num_today", None)

        return transformed_data


class RepositoriesAuthorsCommitsSerializer(
    Serializer[schemas.RepositoriesAuthorsCommitsSchema]
):
    pass


class RepositoriesPositionsSerializer(Serializer[schemas.RepositoriesPositionsSchema]):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()

        transformed_data["repo"] = transformed_data["name"]

        return transformed_data
