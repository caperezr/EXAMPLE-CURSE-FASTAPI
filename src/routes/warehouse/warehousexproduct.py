from fastapi import APIRouter
from controllers.warehouse.warehousexproduct import WarehouseXProductResource
from validators.warehouse.response import ResponseTemplateWarehouseXProudct
from middlewares.auth_db import AuthDbMiddleware

router = APIRouter(prefix="/apiwarehousexproduct", route_class=AuthDbMiddleware)

# CRUD WAREHOUSEXPRODUCT
router.add_api_route(
    "/warehousexproduct",
    WarehouseXProductResource.create_warehouse_x_product,
    methods=["POST"],
    tags=["database warehouse by product service"],
    name="Create warehouse by product",
    response_model=ResponseTemplateWarehouseXProudct,
)
