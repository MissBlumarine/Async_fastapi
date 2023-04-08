import os
from typing import List
from fastapi import FastAPI, Depends
from os import environ
import databases
from sqlalchemy import select
from schemas import SoftwareBase, Software, SoftwareCreate
from models.models import software
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi import FastAPI

from crud import router


# load_dotenv()
#
# # DB_HOST = environ.get("DB_HOST", "localhost")
# # DB_NAME = environ.get("DB_NAME", "software_db")
# # DB_USER = environ.get("DB_USER", "software_username")
# # DB_PASS = environ.get("DB_PASS", "passwd_soft")
#
# DB_HOST = os.environ.get("DB_HOST")
# DB_NAME = os.environ.get("DB_NAME")
# DB_USER = os.environ.get("DB_USER")
# DB_PASS = os.environ.get("DB_PASS")
#
# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
# )
#
# database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI(
    title="Async app"
)

app.include_router(router)
#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

#
# @app.get("/", response_model=List[Software])
# async def get_all_software(session: AsyncSession = Depends(get_async_session)):
#     query = await get_all_software(session)
#     return [Software(name=c.name, version=c.version) for c in query]

# @app.get("/", response_model=List[Software])
# async def get_all_software(session: AsyncSession = Depends(get_async_session)):
#     query = await get_all_software(session)
#     return [Software(name=c.name, version=c.version) for c in query]

# @app.post("/create_software", response_model=Software)
# async def create_software(software_new: SoftwareCreate):
#     query = software.insert().values(name=software_new.name, version=software_new.version, register_at=)
#     last_record_id = await database.execute(query)
#     return {**software_new.dict(), "id": last_record_id}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# #
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
