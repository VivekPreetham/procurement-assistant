from decimal import Decimal

from fastapi import APIRouter

from app.schemas.calculations import (
    AnnualSubscriptionResponse,
    BudgetUtilizationResponse,
    CurrencyConversionResponse,
    GSTCalculationResponse,
)
from app.tools.calculations import (
    calculate_annual_subscription,
    calculate_budget_utilization,
    calculate_gst,
    convert_currency,
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


@router.post(
    "/currency-conversion",
    response_model=CurrencyConversionResponse,
)
async def convert_currency_endpoint(
    amount: Decimal,
    exchange_rate: Decimal,
) -> CurrencyConversionResponse:
    result = convert_currency(
        amount=amount,
        exchange_rate=exchange_rate,
    )

    return CurrencyConversionResponse(**result)