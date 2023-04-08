from pydantic import BaseModel, Field
from typing import Optional


class SoftwareBase(BaseModel):
    name: str
    version: str


class SoftwareCreate(SoftwareBase):
    pass


class Software(SoftwareBase):
    id: int

    class Config:
        orm_mode = True
