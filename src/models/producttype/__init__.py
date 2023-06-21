from sqlalchemy import Column, String
from models.timestamp import TimestampMixin
from models.id import IdUuid
from models import BaseCrudModel
from database.session import Base, engine


class ProductTypeModel(BaseCrudModel, TimestampMixin, IdUuid, Base):
    __tablename__ = "ProductType"
    __table_args__ = {"schema": "public"}

    name = Column(String(255), default=None)


Base.metadata.create_all(bind=engine)
