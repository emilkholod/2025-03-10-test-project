from tests.mixins import TestClientMixin


class TestAPI(TestClientMixin):

    def test_api(self):
        response = self.client.get("/api/db_version")
        assert response.status_code == 200
