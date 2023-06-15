from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class PokemonRequest(BaseModel):
    name: str


""" class FormPaginationSchema(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str] """
