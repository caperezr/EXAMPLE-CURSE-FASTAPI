from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, ForeignKey
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine


@dataclass
class WarehouseModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "Warehouse"
    # __table_args__ = {"schema": "public"}

    idWarehouseType = Column(Integer, ForeignKey("WarehouseType.id"))
    name = Column(String(255))


Base.metadata.create_all(bind=engine)
