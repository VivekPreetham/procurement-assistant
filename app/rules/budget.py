from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class BudgetValidationResult:
    is_compliant: bool
    requires_additional_approval: bool
    explanation: str


def validate_budget(
        estimated_budget: Decimal,
        approval_limit: Decimal,
) -> BudgetValidationResult:
    if estimated_budget > approval_limit:
        return BudgetValidationResult(
            is_compliant=True,
            requires_additional_approval=True,
            explanation=(
                "The estimated budget excees the standard "
                "approval limit and requires additional approval"
            ),
        )

    return BudgetValidationResult(
        is_compliant=True,
        requires_additional_approval=False,
        explanation=(
            "The estimated budget is within the standard "
            "approval limit."
        ),
    )