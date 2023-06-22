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
