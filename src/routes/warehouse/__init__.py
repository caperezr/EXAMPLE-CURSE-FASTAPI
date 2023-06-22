from fastapi import APIRouter
from controllers.warehouse import DatabaseResource
from validators.warehouse.response import WarehouseTypeResponse, ResponseTemplateSchema
from middlewares.auth_db import AuthDbMiddleware


router = APIRouter(prefix="/database", route_class=AuthDbMiddleware)
# CRUD WAREHOUSETYPE
router.add_api_route(
    "/warehousetype",
    DatabaseResource.create_warehousetype,
    methods=["POST"],
    tags=["database warehouse type service"],
    name="Create WarehouseType",
    response_model=WarehouseTypeResponse,
)

router.add_api_route(
    "/warehousetypes",
    DatabaseResource.get_warehouse_types,
    methods=["GET"],
    tags=["database warehouse type service"],
    name="Get all Warehouses type",
    response_model=list[WarehouseTypeResponse],
)

router.add_api_route(
    "/updatewarehousetype",
    DatabaseResource.update_warehousetype,
    methods=["PATCH"],
    tags=["database warehouse type service"],
    name="Update Warehouse Type",
    response_model=WarehouseTypeResponse,
)

# CRUD PRODUCTTYPE
router.add_api_route(
    "/producttype",
    DatabaseResource.create_product_type,
    methods=["POST"],
    tags=["database product type service"],
    name="Create Product type",
    response_model=ResponseTemplateSchema,
)

router.add_api_route(
    "/producttypes",
    DatabaseResource.get_product_types,
    methods=["GET"],
    tags=["database product type service"],
    name="Get all product types",
    response_model=list[ResponseTemplateSchema],
)

router.add_api_route(
    "/updateproducttype",
    DatabaseResource.update_product_type,
    methods=["PUT"],
    tags=["database product type service"],
    name="Update Product Type",
    response_model=ResponseTemplateSchema,
)
