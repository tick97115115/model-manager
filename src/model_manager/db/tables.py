from sqlmodel import SQLModel, create_engine, Field
import sqlalchemy as sa
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

class Category(str, Enum):
    Character = "character"
    Clothing = "clothing"
    Style = "style"
    Pose = "pose"

class LocalLora(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    relative_file_path: str = Field(unique=True)
    category: Category | None = Field(default=None, index=True)
    created_at: datetime = Field(index=True)
    modified_at: datetime = Field(index=True)
