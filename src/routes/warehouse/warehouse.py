from fastapi import APIRouter
from controllers.warehouse.warehouse import WarehouseResource
from validators.warehouse.response import ResponseTemplateWarehouse
from middlewares.auth_db import AuthDbMiddleware

router = APIRouter(prefix="/apiwarehouse", route_class=AuthDbMiddleware)

# CRUD WAREHOUSE
router.add_api_route(
    "/warehouse",
    WarehouseResource.create_warehouse,
    methods=["POST"],
    tags=["database warehouse service"],
    name="Create warehouse",
    response_model=ResponseTemplateWarehouse,
)

router.add_api_route(
    "/warehouses",
    WarehouseResource.get_warehouses,
    methods=["GET"],
    tags=["database warehouse service"],
    name="Get all warehouses",
    response_model=list[ResponseTemplateWarehouse],
)

router.add_api_route(
    "/updatewarehouse",
    WarehouseResource.update_warehouse,
    methods=["PUT"],
    tags=["database warehouse service"],
    name="Update warehouse",
    response_model=ResponseTemplateWarehouse,
)
