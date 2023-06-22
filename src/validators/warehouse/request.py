from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, UUID4


class WarehouseTypeRequest(BaseModel):
    name: str


class RequestTemplateSchema(BaseModel):
    name: str


class RequestTemplateWarehouse(BaseModel):
    idWarehouseType: UUID4
    name: str


class RequestTemplateWarehouseXProudct(BaseModel):
    stock: int
    idWarehouse: UUID4
    idProduct: UUID4
