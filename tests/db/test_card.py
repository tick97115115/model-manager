from datetime import datetime
import pytest
from sqlmodel import create_engine, SQLModel, Session, select
from sqlmodel.pool import StaticPool
from model_manager.db.tables import LocalLora, Category
from os.path import join,dirname

# This is the same as using the @pytest.mark.anyio on all test functions in the module
pytestmark = pytest.mark.anyio

@pytest.fixture
def db_engine():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    return engine

def test_create_Card(db_engine):
    data = LocalLora(relative_file_path="test.jpg", category=Category.Character, created_at=datetime.now(), modified_at=datetime.now())
    with Session(db_engine) as session:
        session.add(data)
        session.commit()
        session.flush()
    
    with Session(db_engine) as session:
        statement = select(LocalLora).where(LocalLora.relative_file_path == "test.jpg")
        result = session.exec(statement)
        for row in result:
            assert row.relative_file_path == "test.jpg"
            assert row.category == Category.Character
    
    
    
