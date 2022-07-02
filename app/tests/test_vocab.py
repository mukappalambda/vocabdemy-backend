from app import main
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(main.app)


class TestVocab:
    def test_create_one_vocab(self):
        response = client.post(
            "/vocabs",
            json={"vocab": "abc"}
        )
        print(response)

        assert response.status_code == 201

    def test_update_vocab(self):

        id = 1

        response = client.put(
            f"/vocabs/{id}",
            json={"vocab": "cba"}
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
