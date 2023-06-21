from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class WarehouseTypeRequest(BaseModel):
    name: str


class RequestTemplateSchema(BaseModel):
    name: str
