from decimal import Decimal

from pydantic import BaseModel

class GSTCalculationResponse(BaseModel):
    base_amount: Decimal
    gst_rate: Decimal
    gst_amount: Decimal
    total_amount: Decimal


class BudgetUtilizationResponse(BaseModel):
    total_budget: Decimal
    used_budget: Decimal
    remaining_budget: Decimal
    utilization_percentage: Decimal


class AnnualSubscriptionResponse(BaseModel):
    monthly_cost: Decimal
    subscription_count: Decimal
    annual_cost_per_subscription: Decimal
    total_annual_cost: Decimal