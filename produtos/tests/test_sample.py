import pytest
from fastapi.testclient import TestClient
from fastapi import status, FastAPI
from produtos.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "API favoritos!"}
    

@pytest.mark.asyncio
def test_user_create_correto():
    response = client.post(
        "/create",
        json={"name_user": "Carlos", "email": "carlos@test.com"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "message":"Cadastrado com sucesso!"
    } 

# @pytest.mark.asyncio
# def test_user_create_validavao_email():
#     response = client.post(
#         "/items/",
#         json={"name_user": "Carlos", "email": "carlos123test.com"},
#     )
#     assert response.status_code == 422
#     assert response.json() == {
#     "detail": [
#         {
#         "loc": [
#             "body",
#             "email"
#         ],
#         "msg": "value is not a valid email address",
#         "type": "value_error.email"
#         }
#     ]
#     }

# @pytest.mark.asyncio
# def test_user_delete():
#     response = client.post(
#         "/items/",
#         headers={"email": "carlos@test.com"}
#     )
#     assert response.status_code == 204
#     assert response.json() == {
#      "message": "User deletado com sucesso!"
#     }