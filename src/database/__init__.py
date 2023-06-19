from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://sonarqube:sonarpass@192.168.1.4/fastapidb"
engine = create_engine(DATABASE_URL)
Base = declarative_base(bind=engine)


class WarehouseType(Base):
    __tablename__ = "WarehouseType"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))


class Warehouse(Base):
    __tablename__ = "Warehouse"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idWarehouseType = Column(Integer, ForeignKey("WarehouseType.id"))
    name = Column(String(255))
    warehouse_type = relationship("WarehouseType", backref="warehouses")


class ProductType(Base):
    __tablename__ = "ProductType"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idProductType = Column(Integer, ForeignKey("ProductType.id"))
    name = Column(String(255))
    sku = Column(String(255))
    partNumber = Column(String(255))
    cost = Column(Float(precision=2))
    totalStock = Column(Integer)
    product_type = relationship("ProductType", backref="products")


class WarehouseXProduct(Base):
    __tablename__ = "WarehouseXProduct"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idWarehouse = Column(Integer, ForeignKey("Warehouse.id"))
    idProduct = Column(Integer, ForeignKey("Product.id"))
    stock = Column(Integer)
    warehouse = relationship("Warehouse", backref="warehouse_products")
    product = relationship("Product", backref="product_warehouses")


def create_tables():
    Base.metadata.create_all(engine)
