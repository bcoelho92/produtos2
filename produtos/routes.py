from typing import List

from fastapi import APIRouter, HTTPException, status, Response

from produtos.database.schemas import (
    UserSchema, UserListOutput, UserSchemaM,
    ProductsSchema, ProductListOutput,
    FavoritesSchema, FavoritesstOutput,
    ErrorOutput, StandardOutput, 
)
from produtos.service import UserService, ProductService, FavoriteService

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
        raise HTTPException(408, detail=str(error))

@router_user.patch('/update/{id_user}')
async def user_update_id(id_user: int, user_input: UserSchemaM): 
    return await UserService.update_user_by_id(id_user, name_user=user_input.name_user)


@router_user.delete('/{email}', description="Delete a user")
async def users_delete(email: str):
        await UserService.delete_user_id(email)
        return Response(status_code=204)

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

@router_products.put('/update/{id_product}')
async def product_update_id(id_product: int, imput: ProductsSchema):
    return await ProductService.update_product_by_id(id_product, title=imput.title, marca=imput.marca, description=imput.description)

    
@router_products.delete('/{id_product}', description="Delete product")
async def product_delete(id_product: int):
        await ProductService.delete_product(id_product)
        return Response(status_code=204)
    
# FAVORITE ROUTERS
@router_favorites.post(
        '/add/{id_user}/{id_product}',
        description='Add favorites!',
        response_model=StandardOutput,
        responses={400: {'model': ErrorOutput}}
)
async def add_favorites(id_user: int, id_product: int ):
        await FavoriteService.add_favorite(id_user=id_user, id_product=id_product)

@router_favorites.get('/list')
async def favorites_list_al():
    return await FavoriteService.list_favorites()
    

@router_favorites.get('/list/{id_user}', responses={402: {'model': ErrorOutput}})
async def favorite_list_by_id(id_user: int):
    try:
        return await FavoriteService.list_favorites_by_id(id_user)
    except Exception as error:
        raise HTTPException(402, detail=str(error))

@router_favorites.delete('/{id_user}/{id_product}')
async def renove_favorite(id_user: int, id_product: int):
    try:
        await FavoriteService.delete_favorite(id_user, id_product)
        return StandardOutput(message='favorito deletado com sucesso!') 
    except Exception as error:
        raise HTTPException(204, detail=str(error))

# @router_favorites.delete('/{id_user}/{id_product}', description="Delete favorite")
# async def delete_favorites(id_user: int, id_product: int):
#         await FavoriteService.delete_favorite(id_user, id_product)
#         return Response(status_code=204)