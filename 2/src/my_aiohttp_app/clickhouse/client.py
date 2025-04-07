from aiochclient import ChClient

from my_aiohttp_app import config


def get_client(session=None):
    return ChClient(
        session=session,
        url=f"http://{config.CLICKHOUSE_HOST}:{config.CLICKHOUSE_PORT}/",
        user=config.CLICKHOUSE_USER,
        password=config.CLICKHOUSE_PASSWORD,
        database=config.CLICKHOUSE_DB,
    )
