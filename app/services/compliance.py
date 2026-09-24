from decimal import Decimal

from app.rules.validation import (
    ComplianceValidationResult,
    validate_request,
)


def validate_procurement_compliance(
    estimated_budget: Decimal,
    approval_limit: Decimal,
    justification: str,
) -> ComplianceValidationResult:
    return validate_request(
        estimated_budget=estimated_budget,
        approval_limit=approval_limit,
        justification=justification,
    )