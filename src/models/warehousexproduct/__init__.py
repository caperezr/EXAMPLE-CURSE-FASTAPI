from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine
from models.id import IdUuid, type_id_uuid
from sqlalchemy.orm import relationship


@dataclass
class WarehouseXProductModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "WarehouseXProduct"
    # __table_args__ = {"schema": "public"}

    stock = Column(Integer)
    idWarehouse = Column(type_id_uuid, ForeignKey("Warehouse.id"))
    idProduct = Column(type_id_uuid, ForeignKey("Product.id"))
    product = relationship("ProductModel", back_populates="productxwarehouses")
    warehouse = relationship("WarehouseModel", back_populates="warehousexproducts")


Base.metadata.create_all(bind=engine)
