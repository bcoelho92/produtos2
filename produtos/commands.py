from .models import models as md
from .database import db_session as db
from sqlalchemy.future import select
from sqlalchemy import delete

class Commands:
    async def delete_user(email: str):
        async with db.async_session() as session:
            await session.execute(delete(md.User).where(md.User.email==email))
            await session.commit()
    
    async def delete_produto(id_produto: int):
        async with db.async_session() as session:
            await session.execute(delete(md.Product).where(md.Product.id_product==id_produto))
            await session.commit()

    # async def delete_favorite (id_user: int, id_product: int):
    #     async with db.async_session() as session:
    #         await session.execute(delete(md.ProductFavorite).where(md.ProductFavorite.id_user==id_user, md.ProductFavorite.id_product==id_product))
    #         await session.commit()