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


class ResponseTemplateWarehouse(BaseModel):
    id: UUID4
    idWarehouseType: UUID4
    name: str

    class Config:
        orm_mode = True


class ResponseTemplateWarehouseXProudct(BaseModel):
    id: UUID4
    stock: int
    idWarehouse: UUID4
    idProduct: UUID4

    class Config:
        orm_mode = True
