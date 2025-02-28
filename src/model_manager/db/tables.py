from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from enum import Enum

class Category(str, Enum):
    Character = "Character"
    Clothing = "Clothing"
    Style = "Style"
    Scene = "Scene"

class LocalLoraTagsLink(SQLModel, table=True):
    lora_id: int | None = Field(default=None, foreign_key="local_lora.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)

    local_lora: "LocalLora" = Relationship(back_populates="tag_links")
    tag: "Tag" = Relationship(back_populates="local_lora_links")

class LocalLora(SQLModel, table=True):
    # id: UUID = Field(default_factory=uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    relative_file_path: str = Field(unique=True)
    category: Category | None = Field(default=None, index=True)
    created_at: datetime = Field(index=True)
    modified_at: datetime = Field(index=True)

    tag_links: list[LocalLoraTagsLink] = Relationship(back_populates="local_lora")

class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    
    local_lora_links: list[LocalLoraTagsLink] = Relationship(back_populates="tag")

