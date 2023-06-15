from pydantic import BaseModel
from typing import Optional


class PokemonResponse(BaseModel):
    name: str
    url: Optional[str]
    imgUrl: Optional[str]
