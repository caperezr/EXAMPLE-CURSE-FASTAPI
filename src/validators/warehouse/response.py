from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, UUID4


class WarehouseTypeResponse(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


class ResponseTemplateSchema(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True
