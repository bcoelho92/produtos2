from asyncio import gather
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import responses

from database.schemas import (
    UserSchema, RequestUser, RequestIdUser,
    ProductsSchema, RequestProducts, RequestIdProducts,
    ErrorOutput, StandardOutput, UserListOutput
)
from service import UserService, ProductService

router_user = APIRouter()
router_favorites = APIRouter()
router_products = APIRouter()

# USER ROUTERS
@router_user.post('/create', description='create user!', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserSchema):
    try:
        await UserService.create_user(name_user=user_input.name_user, email=user_input.email)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@router_user.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@router_user.delete('/delete')
async def users_delete():
    pass

# PRODUCT ROUTERS
@router_products.post('/create', description='create product!', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def product_create():
    pass

@router_products.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def product_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@router_products.delete('/delete')
async def product_delete():
    pass