from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


class PokemonRequest(BaseModel):
    name: str


class Tipado_b:
    def __init__(
        self, name: str = Body(), variable_c: int = Body(), var_b: int = Body(...)
    ) -> None:
        self.name = name
        self.variable_c = variable_c
        self.var_b = var_b


""" class FormPaginationSchema(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str] """
