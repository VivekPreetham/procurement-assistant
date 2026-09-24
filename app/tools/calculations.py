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