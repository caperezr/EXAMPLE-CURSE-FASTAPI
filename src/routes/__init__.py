from fastapi import APIRouter
from routes.pokemon import router as pokemon_router

router = APIRouter(prefix="/api")


router.include_router(pokemon_router)
