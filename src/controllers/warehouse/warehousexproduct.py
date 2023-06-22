from fastapi import Depends, Body
from starlette.endpoints import HTTPEndpoint
from database.get_db import get_db
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader
from typing import List
from validators.warehouse.request import RequestTemplateWarehouseXProudct
from validators.warehouse.response import ResponseTemplateWarehouseXProudct
from models.warehousexproduct import WarehouseXProductModel


class WarehouseXProductResource(HTTPEndpoint):
    @staticmethod
    async def create_warehouse_x_product(
        data: RequestTemplateWarehouseXProudct,
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        new_warehouse_x_product = WarehouseXProductModel.create(
            db_session,
            stock=data.stock,
            idWarehouse=data.idWarehouse,
            idProduct=data.idProduct,
        )

        warehouse_x_product_response = ResponseTemplateWarehouseXProudct(
            id=new_warehouse_x_product.id,
            stock=new_warehouse_x_product.stock,
            idWarehouse=new_warehouse_x_product.idWarehouse,
            idProduct=new_warehouse_x_product.idProduct,
        )
        return warehouse_x_product_response

    """ @staticmethod
    async def get_warehousesxproduct(
        _authorization=Depends(APIKeyHeader(name="Authorization")),
    ) -> List[ResponseTemplateWarehouse]:
        warehouses_model = WarehouseModel.read_select()
        warehouses_response = [
            ResponseTemplateWarehouse(
                id=w.id,
                idWarehouseType=w.idWarehouseType,
                name=w.name,
            )
            for w in warehouses_model
        ]
        return warehouses_response """

    """ @staticmethod
    async def update_warehouse(
        id: str,
        data: RequestTemplateWarehouse = Body(...),
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        warehouse_model = WarehouseModel.update(
            db_session,
            id,
            idWarehouseType=data.idWarehouseType,
            name=data.name,
        )
        warehouse_response = ResponseTemplateWarehouse(
            id=warehouse_model.id,
            idWarehouseType=warehouse_model.idWarehouseType,
            name=warehouse_model.name,
        )
        return warehouse_response """
