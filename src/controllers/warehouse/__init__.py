from fastapi import Depends
from starlette.endpoints import HTTPEndpoint
from validators.warehouse.response import WarehouseTypeResponse
from validators.warehouse.request import WarehouseTypeRequest
from database import WarehouseType
from configs import connection_database_engine
from typing import List

engine, Base, Session = connection_database_engine()


class DatabaseResource(HTTPEndpoint):
    @staticmethod
    async def create_warehousetype(data: WarehouseTypeRequest):
        warehouse_type_data = WarehouseType(name=data.name)
        session = Session()
        session.add(warehouse_type_data)
        session.commit()
        data_response = WarehouseTypeResponse(
            id=warehouse_type_data.id, name=warehouse_type_data.name
        )
        return data_response

    @staticmethod
    async def get_warehouse_types() -> List[WarehouseTypeResponse]:
        session = Session()
        warehouse_types = session.query(WarehouseType).all()
        warehouse_types_response = [
            WarehouseTypeResponse(id=wt.id, name=wt.name) for wt in warehouse_types
        ]
        return warehouse_types_response

    @staticmethod
    async def update_warehousetype(
        id: int, data: WarehouseTypeRequest
    ) -> WarehouseTypeResponse:
        session = Session()
        warehouse_type = (
            session.query(WarehouseType).filter(WarehouseType.id == id).first()
        )

        if warehouse_type:
            warehouse_type.name = data.name
            session.commit

        return WarehouseTypeResponse(id=warehouse_type.id, name=warehouse_type.name)
