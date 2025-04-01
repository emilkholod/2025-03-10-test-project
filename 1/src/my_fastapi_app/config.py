from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MY_FASTAPI_APP_", case_sensitive=True)

    ENV: str = Field("prod")

    DB_HOST: str = Field("database")
    DB_PORT: int = Field(5432)
    DB_NAME: str = Field("postgres")
    DB_USER: str = Field("root")
    DB_PASSWORD: str = Field("root")
    MIN_CONNECTIONS_COUNT: int = Field(10)
    MAX_CONNECTIONS_COUNT: int = Field(10)


@lru_cache(maxsize=1)
def get_settings():
    return Settings()
