from fastapi import APIRouter

from .pokemon import router as pokemon

router = APIRouter(prefix="/poke_api")

router.include_router(pokemon)
