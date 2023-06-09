from datetime import datetime
from typing import AsyncGenerator
from sqlalchemy import Column, String, Integer, TIMESTAMP
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

#
# class Software(Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     version = Column(String, nullable=False)
#     register_date = Column(TIMESTAMP, default=datetime.utcnow)
#     updated_at = Column(TIMESTAMP, nullable=True)


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all())
#         await conn.run_sync(Base.metadata.drop_all())


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
