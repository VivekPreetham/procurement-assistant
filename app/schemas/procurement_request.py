from pydantic import BaseModel, Field


class ProcurementRequestCreate(BaseModel):
    item: str = Field(min_length=1, max_length=255)
    quantity: int = Field(gt=0)
    estimated_budget: float = Field(gt=0)
    department: str = Field(min_length=1, max_length=100)
    justification: str = Field(min_length=1)
    delivery_timeline: str = Field(min_length=1, max_length=50)
