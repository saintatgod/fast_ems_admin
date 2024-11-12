from datetime import datetime
from sqlmodel import SQLModel, Field
import uuid

class BaseModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="主键ID")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")

    def save(self):
        self.updated_at = datetime.now()
