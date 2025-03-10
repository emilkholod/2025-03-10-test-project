import pytest
from fastapi.testclient import TestClient


class TestClientMixin:
    @pytest.fixture(autouse=True)
    def _client(self, client: TestClient):
        self.client = client
