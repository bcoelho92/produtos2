from asyncio import gather
from typing import List

from fastapi import APIRouter, HTTPException, status
from starlette import responses

from database.schemas import (
    UserSchema, UserListOutput,
    ProductsSchema, ProductListOutput,
    ErrorOutput, StandardOutput, 
)
from service import UserService, ProductService

router_user = APIRouter()
router_favorites = APIRouter()
router_products = APIRouter()

# USER ROUTERS
@router_user.post(
        '/create',
        status_code=status.HTTP_201_CREATED,
        description='create user!',
        response_model=StandardOutput,
        responses={400: {'model': ErrorOutput}}
)
async def user_create(user_input: UserSchema):
    try:
        await UserService.create_user(name_user=user_input.name_user, email=user_input.email)
        return StandardOutput(message='Cadastrado com sucesso!') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@router_user.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@router_user.get('/list/{id_user}', response_model=UserListOutput, responses={400: {'model': ErrorOutput}})
async def user_list_id(id_user: int):
    try:
        return await UserService.list_user_by_id(id_user)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router_user.delete('/delete/{id_user}', response_model=StandardOutput)
async def users_delete(id_user: int):
    try:
        await UserService.delete_user(id_user)
        return StandardOutput(message=f'User id: {id_user}, deletado com sucesso!')
    except Exception as error:
        raise HTTPException(408, detail=str(error))

# PRODUCT ROUTERS
@router_products.post(
        '/create',
        status_code=status.HTTP_201_CREATED,
        description='create product!',
        response_model=StandardOutput,
        responses={400: {'model': ErrorOutput}}
)
async def create_product(imput: ProductsSchema):
    try:
        await ProductService.create_product(title=imput.title, marca=imput.marca, description=imput.description)
        return StandardOutput(message='Produto cadastrado com sucesso!')
    except Exception as error:
        raise HTTPException(408, detail=str(error))

@router_products.get('/list', response_model=List[ProductListOutput], responses={400: {'model': ErrorOutput}})
async def product_list():
    try:
        return await ProductService.list_product()
    except Exception as error:
        raise HTTPException(408, detail=str(error))

@router_products.get('/list/{id_product}', response_model=ProductListOutput, responses={400: {'model': ErrorOutput}})
async def product_list_id(id_product: int):
    try:
        return await ProductService.list_product_by_id(id_product)
    except Exception as error:
        raise HTTPException(408, detail=str(error))
    
@router_products.delete('/delete/{id_product}', response_model=StandardOutput)
async def product_delete(id_product: int):
    try:
        await ProductService.delete_product(id_product)
        return StandardOutput(message=f'Producto com ID:{id_product}, deletado com sucesso!')
    except Exception as error:
        raise HTTPException(408, detail=str(error))
    
# PRODUCT ROUTERS
@router_favorites.post('/add')
async def add_favorites():
    pass

@router_favorites.delete('/remove')
async def renove_favorites():
    pass

