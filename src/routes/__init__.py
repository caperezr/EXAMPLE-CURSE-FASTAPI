from fastapi import APIRouter
from routes.electricity.router import router as electricity_router

router = APIRouter()

router.include_router(electricity_router, prefix="/electricity")

