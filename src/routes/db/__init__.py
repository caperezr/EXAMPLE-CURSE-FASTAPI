from fastapi import APIRouter
from controllers.db import DatabaseResource
from validators.db.response import WarehouseTypeResponse

router = APIRouter(prefix="/database")

router.add_api_route(
    "/warehousetype",
    DatabaseResource.create_warehousetype,
    methods=["POST"],
    tags=["database"],
    name="Create WarehouseType",
    response_model=WarehouseTypeResponse,
)
