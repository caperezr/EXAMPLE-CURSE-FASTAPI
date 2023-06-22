from fastapi import APIRouter
from routes.pokemon import router as pokemon_router
from routes.ability import router as ability_router
from routes.exercise import router as exercise_router
from routes.warehouse import router as db_router

from routes.warehouse.product import router as product_router
from routes.warehouse.warehouse import router as warehouse_router
from routes.warehouse.warehousexproduct import router as warehouse_x_product_router

router = APIRouter(prefix="/api")


router.include_router(pokemon_router)
router.include_router(ability_router)
router.include_router(exercise_router)
router.include_router(db_router)

router.include_router(product_router)
router.include_router(warehouse_router)
router.include_router(warehouse_x_product_router)
