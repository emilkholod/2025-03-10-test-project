from environs import env

env.read_env()

MCR = env.int("MCR", 5)
"""Maximum concurrent requests"""

RPS = env.int("RPS", 10)
"""Requests per second"""

GITHUB_API_BASE_URL: str = "https://api.github.com"
GITHUB_ACCESS_TOKEN: str = env.str("GITHUB_ACCESS_TOKEN", "")

CLICKHOUSE_HOST: str = env.str("CLICKHOUSE_HOST", default="clickhouse")
CLICKHOUSE_PORT: int = env.int("CLICKHOUSE_PORT", default=8123)
CLICKHOUSE_DB: str = env.str("CLICKHOUSE_DB", default="test")
CLICKHOUSE_USER: str = env.str("CLICKHOUSE_USER", default="default")
CLICKHOUSE_PASSWORD: str = env.str("CLICKHOUSE_PASSWORD", default="default")
