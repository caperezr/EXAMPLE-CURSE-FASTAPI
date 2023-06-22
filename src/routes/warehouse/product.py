from fastapi import APIRouter
from controllers.warehouse.product import ProductResource
from validators.product.response import ProductResponse
from middlewares.auth_db import AuthDbMiddleware

router = APIRouter(prefix="/apiproduct", route_class=AuthDbMiddleware)

# CRUD PRODUCT
router.add_api_route(
    "/product",
    ProductResource.create_product,
    methods=["POST"],
    tags=["database product service"],
    name="Create product",
    response_model=ProductResponse,
)

router.add_api_route(
    "/products",
    ProductResource.get_products,
    methods=["GET"],
    tags=["database product service"],
    name="Get all products",
    response_model=list[ProductResponse],
)

router.add_api_route(
    "/updateproducttype",
    ProductResource.update_product,
    methods=["PUT"],
    tags=["database product service"],
    name="Update Product",
    response_model=ProductResponse,
)
