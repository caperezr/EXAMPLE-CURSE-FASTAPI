from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configs.environment import Config
from sqlalchemy.engine.reflection import Inspector


def connection_database_engine():
    DATABASE_URL = Config.DB_HOST
    # print(Config.DB_HOST)
    # DATABASE_URL = Config.DB_HOST
    # Ver la lista de schemas en la bd en la cual estoy trabajando
    engine = create_engine(DATABASE_URL)
    inspector = Inspector.from_engine(engine)
    schemas = inspector.get_schema_names()
    for schema in schemas:
        print(schema)

    Base = declarative_base(bind=engine)
    Session = sessionmaker(bind=engine)

    return engine, Base, Session
