from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, UUID4


class ProductResponse(BaseModel):
    id: UUID4
    idProductType: UUID4
    name: str
    sku: str
    partNumber: str
    cost: float
    totalStock: int

    class Config:
        orm_mode = True
