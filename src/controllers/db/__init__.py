from fastapi import Depends
from starlette.endpoints import HTTPEndpoint
from validators.db.request import WarehouseTaypeRequest
from validators.db.response import WarehouseTypeResponse
from database import WarehouseType
from configs import connection_database_engine

engine, Base, Session = connection_database_engine()


class DatabaseResource(HTTPEndpoint):
    @staticmethod
    async def create_warehousetype(data: WarehouseTaypeRequest):
        warehouse_type_data = WarehouseType(name=data.name)
        session = Session()
        session.add(warehouse_type_data)
        session.commit()
        data_response = WarehouseTypeResponse(
            id=warehouse_type_data.id, name=warehouse_type_data.name
        )
        return data_response
