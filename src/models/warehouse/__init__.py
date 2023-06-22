from dataclasses import dataclass
from sqlalchemy import Column, String, ForeignKey
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine
from sqlalchemy.orm import relationship
from models.id import IdUuid, type_id_uuid


@dataclass
class WarehouseModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "Warehouse"
    # __table_args__ = {"schema": "public"}

    idWarehouseType = Column(type_id_uuid, ForeignKey("WarehouseType.id"))
    name = Column(String(255))
    warehouse_type = relationship("WarehousetypeModel", back_populates="warehouses")
    warehousexproducts = relationship(
        "WarehouseXProductModel", back_populates="warehouse"
    )


Base.metadata.create_all(bind=engine)
