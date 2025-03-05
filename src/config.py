from starlette.config import Config

config = Config()

ENV: str = config("ENV", default="prod")

DB_HOST: str = config("DB_HOST", default="database")
DB_PORT: int = config("DB_PORT", cast=int, default=5432)
DB_NAME: str = config("DB_NAME", default="postgres")
DB_USER: str = config("DB_USER", default="root")
DB_PASSWORD: str = config("DB_PASSWORD", default="root")
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
