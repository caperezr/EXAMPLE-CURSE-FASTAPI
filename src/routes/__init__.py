from fastapi import APIRouter
from routes.pokemon import router as pokemon_router
from routes.ability import router as ability_router
from routes.exercise import router as exercise_router

router = APIRouter(prefix="/api")


router.include_router(pokemon_router)
router.include_router(ability_router)
router.include_router(exercise_router)
