from dataclasses import dataclass
from decimal import Decimal

from app.rules.budget import (
    BudgetValidationResult,
    validate_budget
)

@dataclass(frozen=True)
class ComplianceValidationResult:
    is_compliant: bool
    requires_additional_approval: bool
    violations: tuple[str, ...]
    explanations: tuple[str, ...]


def validate_request(
    estimated_budget: Decimal,
    approval_limit: Decimal,
    justification: str,
) -> ComplianceValidationResult:
    violations: list[str] = []
    explanations: list[str] = []

    # Rule 1: Validate justification
    if not justification.strip():
        violations.append("Justification is missing.")
    else:
        explanations.append("Justification is provided.")

    # Rule 2: Validate budget
    budget_result: BudgetValidationResult = validate_budget(
        estimated_budget=estimated_budget,
        approval_limit=approval_limit,
    )

    if budget_result.requires_additional_approval:
        explanations.append(budget_result.explanation)
    else:
        explanations.append(
            "The estimated budget is within the standard approval limit."
        )

    return ComplianceValidationResult(
        is_compliant=len(violations) == 0,
        requires_additional_approval=(
            budget_result.requires_additional_approval
        ),
        violations=tuple(violations),
        explanations=tuple(explanations),
    )