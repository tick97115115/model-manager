from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from os.path import join, dirname
from sqlmodel import SQLModel, create_engine
from .tables import LocalLora

sqlite_file_path = join(dirname(__file__), "sqlite3.db")
sqlite_uri = "sqlite:///{}".format(sqlite_file_path)

def create_db_engine():
    return create_engine(sqlite_uri)

def create_async_db_engine():
    return create_async_engine(sqlite_uri)

def create_sqlite_file():
    engine = create_db_engine(sqlite_uri)
    SQLModel.metadata.create_all(engine)
