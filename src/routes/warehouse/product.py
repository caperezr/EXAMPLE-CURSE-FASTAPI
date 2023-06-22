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
