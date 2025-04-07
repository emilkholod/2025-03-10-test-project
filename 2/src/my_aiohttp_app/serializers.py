from typing import Any, override

from my_aiohttp_app import dto
from my_aiohttp_app.core.serializer import Serializer


class RepositorySerializer(Serializer[dto.Repository]):
    @override
    def transform(self) -> dict[str, Any]:
        transformed_data = super().transform()
        transformed_data["owner"] = transformed_data["owner"]["login"]
        return transformed_data


class RepositoryAuthorCommitsNumSerializer(Serializer[dto.RepositoryAuthorCommitsNum]):
    pass
