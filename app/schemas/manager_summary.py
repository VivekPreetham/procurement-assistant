from decimal import Decimal
from pydantic import BaseModel, Field

class ManagerRequestInput(BaseModel):
    item: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    estimated_budget: Decimal = Field(ge=0)
    business_justification: str = Field(min_length=1)
    department: str = Field(min_length=1)
    delivery_timeline: str = Field(min_length=1)


class ComplianceInput(BaseModel):
    is_compliant: bool
    violations: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class RequestedItem(BaseModel):
    item: str
    quantity: int


class ManagerSummaryResponse(BaseModel):
    summary: str 
    requested_items: list[RequestedItem]
    estimated_cost: Decimal
    business_justification: str
    department: str
    delivery_timeline: str
    compliance_status: str
    risks: list[str]
    recommended_action: str
