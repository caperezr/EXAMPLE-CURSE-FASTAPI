from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connection_database_engine():
    DATABASE_URL = "postgresql://sonarqube:sonarpass@192.168.1.3/fastapidb"
    engine = create_engine(DATABASE_URL)
    Base = declarative_base(bind=engine)
    Session = sessionmaker(bind=engine)

    return engine, Base, Session
