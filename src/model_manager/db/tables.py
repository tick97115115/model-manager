from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from enum import Enum

class Category(str, Enum):
    Character = "Character"
    Clothing = "Clothing"
    Style = "Style"
    Scene = "Scene"

class LocalLora(SQLModel, table=True):
    # id: UUID = Field(default_factory=uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    relative_file_path: str = Field(unique=True)
    category: Category | None = Field(default=None, index=True)
    created_at: datetime = Field(index=True)
    modified_at: datetime = Field(index=True)

class Tags(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

class LoraTags(SQLModel, table=True):
    lora_id: int = Field(foreign_key="local_lora.id")
    tag_id: int = Field(foreign_key="tags.id")
