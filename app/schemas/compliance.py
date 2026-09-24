from pydantic import BaseModel, Field


class ComplianceValidationRequest(BaseModel):
    estimated_budget: float = Field(gt=0)
    approval_limit: float = Field(gt=0)
    justification: str


class ComplianceValidationResponse(BaseModel):
    is_compliant: bool
    requires_additional_approval: bool
    violations: list[str]
    explanations: list[str]