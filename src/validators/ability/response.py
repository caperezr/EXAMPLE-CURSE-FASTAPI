from pydantic import BaseModel
from typing import Optional, List
from utils.ability.pokemon import Pokemon


class AbilityResponse(BaseModel):
    name: str
    url: Optional[str]
    pokemon: Optional[List[Pokemon]]

    class Config:
        arbitrary_types_allowed = True
