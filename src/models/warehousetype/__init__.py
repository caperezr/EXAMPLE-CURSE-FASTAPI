from dataclasses import dataclass
from sqlalchemy import Column, String
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine
from sqlalchemy.orm import relationship


@dataclass
class WarehousetypeModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "WarehouseType"
    # __table_args__ = {"schema": "public"}

    name: str = Column(String(255), default=None)
    warehouses = relationship("WarehouseModel", back_populates="warehouse_type")


Base.metadata.create_all(bind=engine)
