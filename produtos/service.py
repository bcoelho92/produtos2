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
            await session.execut(delete(md.User).where(md.User.id_user==id_user))
            await session.commit()

    async def list_user():
        async with db.async_session() as session:
            result = await session.execute(select(md.User))
            return result.scalars().all()
        
    async def get_user_by_id(id_user: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.User).where(md.User.id_user==id_user))
            return result.scalar()
    
# Produto
class ProductService:
    async def create_product(title: str,  marca: str, description: str):
        async with db.async_session() as session:
            session.add(md.Product(title=title, marca=marca, description=description)) 
            await session.commit()
    
    async def delete_product(id_product: int):
        async with db.async_session() as session:
            await session.execut(delete(md.Product).where(md.Product.id_product==id_product))
            await session.commit()

    async def list_products():
        async with db.async_session() as session:
            result = await session.execute(select(md.Product))
            return result.scalars().all()
        
    async def get_product_by_id(id_product: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.Product).where(md.Product.id_product==id_product))
            return result.scalar()
    
# Favoritos
class FavoriteService:
    pass