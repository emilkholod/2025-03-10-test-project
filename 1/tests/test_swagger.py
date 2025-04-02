from tests.mixins import TestClientMixin


class TestSwagger(TestClientMixin):

    def test_docs(self):
        response = self.client.get("/docs")
        assert response.status_code == 200
