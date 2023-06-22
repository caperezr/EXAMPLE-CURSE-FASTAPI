from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine


@dataclass
class WarehouseXProductModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "WarehouseXProduct"
    # __table_args__ = {"schema": "public"}

    idWarehouse = Column(Integer, ForeignKey("Warehouse.id"))
    idProduct = Column(Integer, ForeignKey("Product.id"))
    stock = Column(Integer)


Base.metadata.create_all(bind=engine)
