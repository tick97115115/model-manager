from sqlmodel import SQLModel, create_engine, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

class LocalLora(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    file_path: str = Field(unique=True)
    created_at: datetime = Field(index=True)
    modified_at: datetime = Field(index=True)