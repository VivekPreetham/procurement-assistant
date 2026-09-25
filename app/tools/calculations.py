from decimal import Decimal

def calculate_gst(
    amount: Decimal,
    gst_rate: Decimal,
) -> dict[str, Decimal]:
    gst_amount = amount * gst_rate / Decimal("100")
    total_amount = amount + gst_amount

    return {
        "base_amount": amount,
        "gst_rate": gst_rate,
        "gst_amount": gst_amount,
        "total_amount": total_amount
    }

def calculate_budget_utilization(
        total_budget: Decimal,
        used_budget: Decimal,
) -> dict[str, Decimal]:
    if total_budget <= 0:
        raise ValueError("Total Budget must be greater than zero")

    if used_budget < 0:
        raise ValueError("Used Budget cannot be negative")

    remaining_budget = total_budget - used_budget

    utilization_percentage = ( used_budget / total_budget ) * Decimal("100")

    return {
        "total_budget": total_budget,
        "used_budget": used_budget,
        "remaining_budget": remaining_budget,
        "utilization_percentage": utilization_percentage
    }

def calculate_annual_subscription(
        monthly_cost: Decimal,
        subscription_count: int = 1,
) -> dict[str, Decimal]:
    if monthly_cost < 0:
        raise ValueError("Monthly cost cannot be negative")

    if subscription_count < 0:
        raise ValueError("Subscription count must be greater than zero")

    annual_cost_per_subscription = monthly_cost * Decimal("12")

    total_annual_cost = ( annual_cost_per_subscription * Decimal(subscription_count))

    return {
        "monthly_cost": monthly_cost,
        "subscription_count": subscription_count,
        "annual_cost_per_subscription": annual_cost_per_subscription,
        "total_annual_cost": total_annual_cost,
    }


def convert_currency(
    amount: Decimal,
    exchange_rate: Decimal,
) -> dict[str, Decimal]:
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than zero.")

    converted_amount = amount * exchange_rate

    return {
        "amount": amount,
        "exchange_rate": exchange_rate,
        "converted_amount": converted_amount,
    }