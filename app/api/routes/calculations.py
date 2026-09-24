from decimal import Decimal

from fastapi import APIRouter

from app.schemas.calculations import (
    AnnualSubscriptionResponse,
    BudgetUtilizationResponse,
    GSTCalculationResponse,
)
from app.tools.calculations import (
    calculate_gst,
    calculate_budget_utilization,
    calculate_annual_subscription
) 

router = APIRouter(
    prefix="/calculations",
    tags=["calculations"],
)

@router.post(
    "/gst",
    response_model=GSTCalculationResponse
)
async def calculate_gst_endpoint(
    amount: Decimal,
    gst_rate: Decimal,
) -> GSTCalculationResponse:
    result = calculate_gst(
        amount=amount,
        gst_rate=gst_rate,
    )

    return GSTCalculationResponse(**result)


@router.post(
    "/budget-utilization",
    response_model=BudgetUtilizationResponse
)
async def calculate_budget_utilization_endpoint(
    total_budget: Decimal,
    used_budget: Decimal,
) -> BudgetUtilizationResponse:
    result = calculate_budget_utilization(
        total_budget=total_budget,
        used_budget=used_budget,
    )

    return BudgetUtilizationResponse(**result)


@router.post(
    "/annual-subscription",
    response_model=AnnualSubscriptionResponse,
)
async def calculate_annual_subscription_endpoint(
    monthly_cost: Decimal,
    subscription_count: int = 1,
) -> AnnualSubscriptionResponse:
    result = calculate_annual_subscription(
        monthly_cost=monthly_cost,
        subscription_count=subscription_count,
    )

    return AnnualSubscriptionResponse(**result)