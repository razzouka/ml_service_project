from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModelCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ModelOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True