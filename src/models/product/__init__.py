from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.timestamp import TimestampMixin
from models.id import IdUuid, type_id_uuid
from models import BaseCrudModel
from database.session import Base, engine
from sqlalchemy.orm import relationship


@dataclass
class ProductModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "Product"
    # __table_args__ = {"schema": "public"}

    name: str = Column(String(255))
    sku: str = Column(String(255))
    partNumber: str = Column(String(255))
    cost: float = Column(Float(precision=2))
    totalStock: int = Column(Integer)
    idProductType = Column(type_id_uuid, ForeignKey("ProductType.id"))
    product_type = relationship("ProductTypeModel", back_populates="products")

    productxwarehouses = relationship(
        "WarehouseXProductModel", back_populates="product"
    )


Base.metadata.create_all(bind=engine)
