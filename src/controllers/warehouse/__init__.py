from fastapi import Depends, Body
from starlette.endpoints import HTTPEndpoint
from validators.warehouse.response import WarehouseTypeResponse, ResponseTemplateSchema
from validators.warehouse.request import WarehouseTypeRequest, RequestTemplateSchema
from models.warehousetype import WarehousetypeModel
from models.producttype import ProductTypeModel
from database.get_db import get_db
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader

from typing import List


class DatabaseResource(HTTPEndpoint):
    # CRUD WAREHOUSE TYPE
    @staticmethod
    async def create_warehousetype(
        data: WarehouseTypeRequest,
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        new_warehouse_type = WarehousetypeModel.create(db_session, name=data.name)
        warehouse_types_response = WarehouseTypeResponse(
            id=new_warehouse_type.id, name=new_warehouse_type.name
        )
        return warehouse_types_response

    # Preguntar por que ya no es necesario pasarle el db_session
    @staticmethod
    async def get_warehouse_types(
        _authorization=Depends(APIKeyHeader(name="Authorization")),
    ) -> List[WarehouseTypeResponse]:
        warehouse_types_model = WarehousetypeModel.read_select()
        warehouse_types_response = [
            WarehouseTypeResponse(id=wt.id, name=wt.name)
            for wt in warehouse_types_model
        ]
        return warehouse_types_response

    # Preguntar por que al id: str no se le puede poner Path
    @staticmethod
    async def update_warehousetype(
        id: str,
        data: WarehouseTypeRequest = Body(...),
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        warehouse_type_model = WarehousetypeModel.update(db_session, id, name=data.name)
        warehouse_types_response = WarehouseTypeResponse(
            id=warehouse_type_model.id, name=warehouse_type_model.name
        )
        return warehouse_types_response

    # CRUD PRODUCT TYPE
    @staticmethod
    async def create_product_type(
        data: RequestTemplateSchema = Body(...),
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        new_product_type = ProductTypeModel.create(db_session, name=data.name)
        product_type_response = ResponseTemplateSchema(
            id=new_product_type.id, name=new_product_type.name
        )
        return product_type_response

    @staticmethod
    async def get_product_types(
        _authorization=Depends(APIKeyHeader(name="Authorization")),
    ):
        product_types_model = ProductTypeModel.read_select()
        product_types_respose = [
            ResponseTemplateSchema(id=pt.id, name=pt.name) for pt in product_types_model
        ]
        return product_types_respose

    @staticmethod
    async def update_product_type(
        id: str,
        data: RequestTemplateSchema = Body(...),
        _authorization=Depends(APIKeyHeader(name="Authorization")),
        db_session: Session = Depends(get_db),
    ):
        product_type_model = ProductTypeModel.update(db_session, id, name=data.name)
        product_type_response = ResponseTemplateSchema(
            id=product_type_model.id, name=product_type_model.name
        )
        return product_type_response
