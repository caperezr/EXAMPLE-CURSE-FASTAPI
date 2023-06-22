from fastapi import Depends, Body
from starlette.endpoints import HTTPEndpoint
from database.get_db import get_db
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader
from typing import List
from validators.warehouse.request import RequestTemplateWarehouse
from validators.warehouse.response import ResponseTemplateWarehouse
from models.warehouse import WarehouseModel


class WarehouseResource(HTTPEndpoint):
    @staticmethod
    async def create_warehouse(
        data: RequestTemplateWarehouse,
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        new_warehouse = WarehouseModel.create(
            db_session,
            idWarehouseType=data.idWarehouseType,
            name=data.name,
        )

        warehouse_response = ResponseTemplateWarehouse(
            id=new_warehouse.id,
            idWarehouseType=new_warehouse.idWarehouseType,
            name=new_warehouse.name,
        )
        return warehouse_response

    @staticmethod
    async def get_warehouses(
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
        return warehouses_response

    @staticmethod
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
        return warehouse_response
