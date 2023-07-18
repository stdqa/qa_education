import sqlite3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = 'data_for_pytest.db'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(engine, autoflush=False, autocommit=False)

Model = declarative_base(name='Model')

session = Session()


def create_db():
    Model.metadata.create_all(engine)


