from fastapi import APIRouter
from controllers.warehouse.warehouse import WarehouseResource
from validators.warehouse.response import ResponseTemplateWarehouse
from middlewares.auth_db import AuthDbMiddleware

router = APIRouter(prefix="/apiwarehouse", route_class=AuthDbMiddleware)

# CRUD WAREHOUSE
router.add_api_route(
    "/product",
    WarehouseResource.create_warehouse,
    methods=["POST"],
    tags=["database warehouse service"],
    name="Create warehouse",
    response_model=ResponseTemplateWarehouse,
)
