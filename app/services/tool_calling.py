from decimal import Decimal
from typing import Any

from app.tools.registry import execute_tool


DECIMAL_FIELDS = {
    "amount",
    "gst_rate",
    "total_budget",
    "used_budget",
    "monthly_cost",
    "exchange_rate",
}

INTEGER_FIELDS = {
    "subscription_count",
}


def normalize_arguments(arguments: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}

    for key, value in arguments.items():
        if key in DECIMAL_FIELDS:
            normalized[key] = Decimal(str(value))

        elif key in INTEGER_FIELDS:
            normalized[key] = int(value)

        else:
            normalized[key] = value

    return normalized


def handle_tool_call(
    tool_name: str,
    arguments: dict[str, Any],
) -> dict[str, Any]:
    try:
        normalized_arguments = normalize_arguments(arguments)

        result = execute_tool(
            tool_name=tool_name,
            arguments=normalized_arguments,
        )

        return {
            "success": True,
            "tool_name": tool_name,
            "result": result,
            "error": None,
        }

    except (TypeError, ValueError, ArithmeticError) as error:
        return {
            "success": False,
            "tool_name": tool_name,
            "result": None,
            "error": str(error),
        }