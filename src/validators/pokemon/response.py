from pydantic import BaseModel
from typing import Optional


class PokemonResponse(BaseModel):
    id: Optional[int]
    name: str
    url: Optional[str]
    imgUrl: Optional[str]