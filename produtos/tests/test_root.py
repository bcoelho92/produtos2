from fastapi.testclient import TestClient
from fastapi import status

def test_get_root(client: TestClient) -> None:
    response = client.get('/')
    bady = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert bady['message'] == "API favoritos!"


