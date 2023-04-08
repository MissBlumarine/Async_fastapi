import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import software
from schemas import Software, SoftwareCreate, SoftwareBase

router = APIRouter(
    prefix="/software",
    tags=["Software"]
)


@router.get("/{software_id}")
async def get_software_by_id(
        software_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(software).where(software.c.id == software_id)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


#

@router.get("/version")
async def get_specific_operations(
        version: str,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(software).where(software.c.version == version)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


#

@router.post("")
async def add_software(new_operation: SoftwareCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(software).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

#
# @router.post("")
# async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}


@router.get("/")
async def get_all_software(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(software))
    return result.all()

# def get_all_software(session: AsyncSession):
#     return session.query(models.models.software).all()
#
#

# async def get_all_software(session: AsyncSession):
#     query = software.select()
#     return await query.fetch_all()
#
#
# async def create_software(session: AsyncSession, name: str, version: str):
#     software_new = software(name=name, version=version)
#     session.add(software_new)
#     return software_new
