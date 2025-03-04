from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.main import create_app


@pytest.fixture(scope="class")
def client() -> Generator[TestClient]:
    with TestClient(create_app()) as client:
        yield client
