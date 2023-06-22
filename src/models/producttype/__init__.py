from dataclasses import dataclass
from sqlalchemy import Column, String
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey

from sqlalchemy.orm import relationship


@dataclass
class ProductTypeModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "ProductType"
    # __table_args__ = {"schema": "public"}

    name = Column(String(255), default=None)
    products = relationship("ProductModel", back_populates="product_type")


Base.metadata.create_all(bind=engine)
