from fastapi import APIRouter
from controllers.warehouse import DatabaseResource
from validators.warehouse.response import WarehouseTypeResponse

router = APIRouter(prefix="/database")

router.add_api_route(
    "/warehousetype",
    DatabaseResource.create_warehousetype,
    methods=["POST"],
    tags=["database"],
    name="Create WarehouseType",
    response_model=WarehouseTypeResponse,
)

router.add_api_route(
    "/warehousetypes",
    DatabaseResource.get_warehouse_types,
    methods=["GET"],
    tags=["database"],
    name="Get all Warehouses type",
    response_model=list[WarehouseTypeResponse],
)

router.add_api_route(
    "/updatewarehouse",
    DatabaseResource.update_warehousetype,
    methods=["PATCH"],
    tags=["database"],
    name="Update Warehouse Type",
    response_model=WarehouseTypeResponse,
)
