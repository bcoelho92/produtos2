import pytest
from fastapi.testclient import TestClient
from fastapi import status, FastAPI
from produtos.main import app
import time

client = TestClient(app)
tm = 3

@pytest.mark.asyncio
async def test_get_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "API favoritos!"}
    
@pytest.mark.asyncio
async def test_user_create_correto():
    response = client.post(
        '/users/create/',
        json={"name_user": "test", "email": "test@test.com"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "message":"Cadastrado com sucesso!"
    } 

@pytest.mark.asyncio
async def test_user_create_validacao_email():
    response = client.post(
        "/users/create/",
        json={"name_user": "test", "email": "testaaatest.com"},
    )
    assert response.status_code == 422
    assert response.json() == {
    "detail": [
        {
        "loc": [
            "body",
            "email"
        ],
        "msg": "value is not a valid email address",
        "type": "value_error.email"
        }
    ]
    }

# time.sleep(tm)

# @pytest.mark.asyncio
# async def test_user_delete():
#     email = "test@test.com"
#     response = client.delete(
#         url=f"/users/{email}"
#     )
#     assert response.status_code == 204