from dataclasses import dataclass
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from configs import connection_database_engine
from models.id import IdUuid

from models.timestamp import TimestampMixin
from models.id import IdUuid, type_id_uuid


engine, Base, Session = connection_database_engine()


@dataclass
class WarehousetypeModel(Base, TimestampMixin, IdUuid):
    __tablename__ = "WarehouseType"
    name: str = Column(String(255), default=None)


@dataclass
class WarehouseModel(Base, TimestampMixin, IdUuid):
    __tablename__ = "Warehouse"
    idWarehouseType = Column(type_id_uuid, ForeignKey("WarehouseType.id"))
    name = Column(String(255))
    warehouse_type = relationship("WarehousetypeModel", backref="warehouses")


@dataclass
class ProductTypeModel(TimestampMixin, IdUuid, Base):
    __tablename__ = "ProductType"
    name = Column(String(255), default=None)


@dataclass
class ProductModel(TimestampMixin, IdUuid, Base):
    __tablename__ = "Product"

    name: str = Column(String(255))
    sku: str = Column(String(255))
    partNumber: str = Column(String(255))
    cost: float = Column(Float(precision=2))
    totalStock: int = Column(Integer)
    idProductType = Column(type_id_uuid, ForeignKey("ProductType.id"))
    product_type = relationship("ProductTypeModel", backref="products")


@dataclass
class WarehouseXProductModel(TimestampMixin, IdUuid, Base):
    __tablename__ = "WarehouseXProduct"

    idWarehouse = Column(type_id_uuid, ForeignKey("Warehouse.id"))
    idProduct = Column(type_id_uuid, ForeignKey("Product.id"))
    stock = Column(Integer)
    warehouse = relationship("WarehouseModel", backref="warehouse_products")
    product = relationship("ProductModel", backref="product_warehouses")


def create_tables():
    Base.metadata.create_all(engine)
