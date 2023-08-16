from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/produtos'
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/produtos"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)