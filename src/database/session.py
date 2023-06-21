from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from .base import BaseQuery
from configs.environment import Config


engine = create_engine(
    Config.DB_HOST,
    max_overflow=40,
    pool_timeout=110,
    pool_size=Config.SQLALCHEMY_ENGINE_OPTIONS_POOL_RECYCLE,
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, query_cls=BaseQuery, bind=engine)
)

Base = declarative_base()
Base.query = SessionLocal.query_property()
