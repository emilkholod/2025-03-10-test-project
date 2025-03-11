from typing import Generator

import pytest
from fastapi.testclient import TestClient

from my_fastapi_app.main import create_app


@pytest.fixture(scope="class")
def client() -> Generator[TestClient, None, None]:
    with TestClient(create_app()) as client:
        yield client
