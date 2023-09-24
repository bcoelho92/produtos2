from .models import models as md
from .database import db_session as db
from sqlalchemy.future import select
from sqlalchemy import delete, func, and_
from produtos.query import Queries
from produtos.commands import Commands
from fastapi import HTTPException, status

# Usuario
class UserService:
    def __init__(self) -> None:
        self.queries = Queries()

    async def create_user(name_user:str, email:str):
        async with db.async_session() as session:
            session.add(md.User(name_user=name_user, email=email)) 
            await session.commit()
    
    async def list_user():
        async with db.async_session() as session:
            result = await session.execute(select(md.User).order_by(md.User.created_at).limit(20))
            return result.scalars().all()
        
    async def get_user_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.User).where(md.User.id_user==id_user))
            return result.scalar()
        
    async def delete_user_id(email: str):
        list_user = await Queries.get_user_by_email(email)
        if list_user is None:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "User não encontrado")
        await Commands.delete_user(email)

    async def update_user_by_id(id_user: int, name_user: str):
        async with db.async_session() as session:
            usuario = select(md.User).where(md.User.id_user == id_user)
            result = await session.execute(usuario)
            user = result.scalar()

            if user:
                user.name_user = name_user
                
                await session.commit()
                raise HTTPException(status_code= status.HTTP_202_ACCEPTED, detail= "User atualizado!")
            else:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "User não encontrado")
    
# Produto
class ProductService:
    def __init__(self) -> None:
        self.queries = Queries()

    async def create_product(title:str, marca:str, description:str):
        async with db.async_session() as session:
            session.add(md.Product(title=title, marca=marca, description=description))
            await session.commit()
    
    async def delete_product(self, id_product: int):
        list_product = await self.queries.get_product_by_id(id_product)
        if list_product is None:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Produto não encontrado")
        await Commands.delete_produto(id_product)

    async def list_product():
        async with db.async_session() as session:
            result = await session.execute(select(md.Product).order_by(md.Product.created_at).limit(20))
            return result.scalars().all()
        
    async def get_product_by_id(id_product: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.Product).where(md.Product.id_product==id_product))
            return result.scalar()
    
    async def update_product_by_id(id_product: int, title:str, marca:str, description:str):
        async with db.async_session() as session:
            product = select(md.Product).where(md.Product.id_product == id_product)
            result = await session.execute(product)
            product = result.scalar()

            if product:
                product.title = title
                product.marca  = marca
                product.description = description

                await session.commit()
                raise HTTPException(status_code= status.HTTP_202_ACCEPTED, detail= "Produto atualizado!")
            else:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Produto não encontrado")

# Favoritos
class FavoriteService:
    def __init__(self) -> None:
        self.queries = Queries()

    async def add_favorite(id_user: int, id_product: int):
        async with db.async_session() as session:     
            # result = select(func.count(md.ProductFavorite)).where (md.ProductFavorite.id_user == id_user)
            result = select(func.count(md.ProductFavorite.id_favorite)).where(md.ProductFavorite.id_user == id_user)
            cont_regist = await session.execute(result)
            registros = cont_regist.scalar()
            if registros < 5:
                session.add(md.ProductFavorite(id_user=id_user, id_product=id_product ))
                await session.commit()
                raise HTTPException(status_code= status.HTTP_202_ACCEPTED, detail= "Favorito adicionado com sucesso!")
            else:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Cota de favoritos atingida")
    
    async def list_favorites():
        async with db.async_session() as session:
            result = await session.execute(select(md.ProductFavorite).order_by(md.ProductFavorite.created_at).limit(20))
            if result:  
                return result.scalars().all()
            elif result is None:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, message= "Nenhum favorito encontrado")
                
    async def get_favorites_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user))
            return result.scalars().all()

    async def delete_favorite(id_user: int, id_product: int):
        async with db.async_session() as session:
            await session.execute(delete(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user, md.ProductFavorite.id_product==id_product))
            await session.commit()
    
    # async def delete_favorite(id_user: int, id_product: int):
    #     list_product = await Queries.get_favorite_by_ids(id_user, id_product)
    #     if list_product is None:
    #         raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Favorito não encontrado")
    #     await Commands.delete_favorite(id_user, id_product)
