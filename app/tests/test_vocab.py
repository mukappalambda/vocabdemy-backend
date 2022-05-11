from app import main
from fastapi.testclient import TestClient

client = TestClient(main.app)


class TestVocab:
    def test_create_one_vocab(self):
        response = client.post(
            "/vocabs",
            json={"vocab": "abc"}
        )
        print(response)

        assert response.status_code == 201
