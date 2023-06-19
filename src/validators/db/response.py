from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class WarehouseTypeResponse(BaseModel):
    id: int
    name: str