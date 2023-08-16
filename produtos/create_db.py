from asyncio import run

from database import db_session as db
from models import models as md


async def create_database():
    async with db.engine.begin() as connection:
        await connection.run_sync(md.Base.metadata.drop_all)
        await connection.run_sync(md.Base.metadata.create_all)

if __name__ == '__main__':
    run(create_database())