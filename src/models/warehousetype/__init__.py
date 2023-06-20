from dataclasses import dataclass
from sqlalchemy import Column, String
from models.timestamp import TimestampMixin
from models.id import IdHex
from models import BaseCrudModel
from database.session import Base


class WarehousetypeModel(BaseCrudModel, TimestampMixin, IdHex, Base):
    __tablename__ = "WarehouseType"
    __table_args__ = {"schema": "public"}

    name: str = Column(String(255), default=None)
