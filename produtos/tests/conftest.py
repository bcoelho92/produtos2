from fastapi.testclient import TestClient
from httpx import AsyncClient
from typing import AsyncGenerator
import pytest
from fastapi import FastAPI

@pytest.fixture(autouse=True)
async def client()-> FastAPI:
    app = FastAPI()
    with TestClient(app) as c:
        yield c 

# @pytest.fixture(scope='module')
# def fast_api_app():
#     app = FastAPI()
#     return app

# @pytest.fixture
# async def client(fast_api_app) -> AsyncGenerator:
#     async with AsyncClient(
#         app=fast_api_app,
#         base_url="http://testserver",
#     ) as client:
#         yield client