from models import models as md
from database import db_session as db
from sqlalchemy.future import select
from sqlalchemy import delete

# Usuario
class UserService:
    async def create_user(name_user:str, email:str):
        async with db.async_session() as session:
            session.add(md.User(name_user=name_user, email=email)) 
            await session.commit()
    
    async def delete_user(id_user: int):
        async with db.async_session() as session:
            await session.execute(delete(md.User).where(md.User.id_user==id_user))
            await session.commit()

    async def list_user():
        async with db.async_session() as session:
            result = await session.execute(select(md.User))
            return result.scalars().all()
        
    async def list_user_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.User).where(md.User.id_user==id_user))
            return result.scalar()
    
# Produto
class ProductService:
    async def create_product(title:str, marca:str, description:str):
        async with db.async_session() as session:
            session.add(md.Product(title=title, marca=marca, description=description))
            await session.commit()
    
    async def delete_product(id_product: int):
        async with db.async_session() as session:
            await session.execute(delete(md.Product).where(md.Product.id_product==id_product))
            await session.commit()

    async def list_product():
        async with db.async_session() as session:
            result = await session.execute(select(md.Product))
            return result.scalars().all()
        
    async def list_product_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.Product).where(md.Product.id_product==id_user))
            return result.scalar()
# Favoritos
class FavoriteService:
    async def add_favorite(id_user: int, id_product: int):
        async with db.async_session() as session:
            session.add(md.ProductFavorite(id_user=id_user, id_product=id_product ))
            await session.commit()
    
    async def list_favorites():
        async with db.async_session() as session:
            result = await session.execute(select(md.ProductFavorite))
            return result.scalars().all()
    
    async def list_favorites_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user))
            return result.scalars().all()

    async def remove_favorite (id_user: int, id_product: int):
        async with db.async_session() as session:
            await session.execute(delete(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user, md.ProductFavorite.id_product==id_product))
            await session.commit()