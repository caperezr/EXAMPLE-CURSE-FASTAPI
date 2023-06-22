from fastapi import Depends, Body
from starlette.endpoints import HTTPEndpoint
from database.get_db import get_db
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader
from typing import List
from validators.product.request import ProductRequest
from validators.product.response import ProductResponse
from models.product import ProductModel


class ProductResource(HTTPEndpoint):
    @staticmethod
    async def create_product(
        data: ProductRequest,
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        new_product = ProductModel.create(
            db_session,
            idProductType=data.idProductType,
            name=data.name,
            sku=data.sku,
            partNumber=data.partNumber,
            cost=data.cost,
            totalStock=data.totalStock,
        )

        product_response = ProductResponse(
            id=new_product.id,
            idProductType=new_product.idProductType,
            name=new_product.name,
            sku=new_product.sku,
            partNumber=new_product.partNumber,
            cost=new_product.cost,
            totalStock=new_product.totalStock,
        )
        return product_response
