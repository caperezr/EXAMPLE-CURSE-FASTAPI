from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, UUID4


class ProductRequest(BaseModel):
    idProductType: UUID4
    name: str
    sku: str
    partNumber: str
    cost: float
    totalStock: int
