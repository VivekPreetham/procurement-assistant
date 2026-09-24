from decimal import Decimal

from fastapi import APIRouter

from app.schemas.compliance import (
    ComplianceValidationRequest,
    ComplianceValidationResponse,
)
from app.services.compliance import (
    validate_procurement_compliance,
)

router = APIRouter(
    prefix="/compliance",
    tags=["compliance"],
)


@router.post(
    "/validate",
    response_model=ComplianceValidationResponse,
)
async def validate_compliance(
    request: ComplianceValidationRequest,
) -> ComplianceValidationResponse:
    result = validate_procurement_compliance(
        estimated_budget=Decimal(str(request.estimated_budget)),
        approval_limit=Decimal(str(request.approval_limit)),
        justification=request.justification,
    )

    return ComplianceValidationResponse(
        is_compliant=result.is_compliant,
        requires_additional_approval=(
            result.requires_additional_approval
        ),
        violations=list(result.violations),
        explanations=list(result.explanations),
    )