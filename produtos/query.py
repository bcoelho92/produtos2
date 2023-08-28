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
    async def list_user_by_id(id_user: str):
        async with db.async_session() as session:
            result = await session.execute(select(md.User).where(md.User.id_user==id_user))
            return result.scalar()
