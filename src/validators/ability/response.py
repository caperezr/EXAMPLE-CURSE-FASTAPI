from pydantic import BaseModel
from typing import Optional
from utils.ability.pokemon import Pokemon


class AbilityResponse(BaseModel):
    name: str
    pokemon: list[Pokemon]

    class Config:
        arbitrary_types_allowed = True
