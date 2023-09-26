from typing import (
    Any,
    Optional,
)

from sqlalchemy import (
    and_,
    asc,
    desc,
    func,
    select,
)
from .models import models as md
from .database import db_session as db
from sqlalchemy.future import select
from sqlalchemy import delete

class Queries:
    async def get_user_by_email(email: str):
        async with db.async_session() as session:
            result = await session.execute(select(md.User).where(md.User.email==email))
            return result.scalar()
            
    async def get_product_by_id(id_product: int):
        async with db.async_session() as session:
            result = await session.execute(select(md.Product).where(md.Product.id_product==id_product))
            return result.scalar()

    async def get_product_by_title(titulo: str):
            async with db.async_session() as session:
                result = await session.execute(select(md.Product).where(md.Product.title==titulo))
                return result.scalar()
    
    async def get_id_product_by_title(titulo: str):
            async with db.async_session() as session:
                result = await session.query(md.Product.id_product).filter(md.Product.title==titulo).first()
                return result.scalar()      

    # async def get_favorite_by_ids(id_user: int, id_product: int):
    #     async with db.async_session() as session:
    #         result = await session.execute(select(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user, md.ProductFavorite.id_product==id_product))
    #         return result.scalars().all()        