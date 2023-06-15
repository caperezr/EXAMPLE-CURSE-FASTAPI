from typing import Optional
from pydantic import BaseModel


class Pokemon(BaseModel):
    name: str
    url: str
