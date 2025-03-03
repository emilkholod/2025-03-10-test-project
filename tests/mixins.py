from fastapi.testclient import TestClient

from src.main import create_app


class TestClientMixin:

    @classmethod
    def setup_class(cls):
        cls.client = TestClient(create_app())
