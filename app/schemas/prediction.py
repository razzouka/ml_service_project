from pydantic import BaseModel
from datetime import datetime
from typing import Any


class PredictionRequest(BaseModel):
    model_id: int
    input_data: dict[str, Any]


class PredictionResponse(BaseModel):
    id: int
    user_id: int
    model_id: int
    input_data: dict[str, Any]
    status: str
    result: dict[str, Any] | None = None
    created_at: datetime

    class Config:
        from_attributes = True