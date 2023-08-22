from fastapi.testclient import TestClient
import pytest
from produtos.main import app

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c 