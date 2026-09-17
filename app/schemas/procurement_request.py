from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProcurementRequestCreate(BaseModel):
    item: str = Field(min_length=1, max_length=255)
    quantity: int = Field(gt=0)
    estimated_budget: float = Field(gt=0)
    department: str = Field(min_length=1, max_length=100)
    justification: str = Field(min_length=1)
    delivery_timeline: str = Field(min_length=1, max_length=50)

class ProcurementRequestResponse(BaseModel):
    id: int
    item: str
    quantity: int
    estimated_budget: float
    department: str
    justification: str
    delivery_timeline: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
