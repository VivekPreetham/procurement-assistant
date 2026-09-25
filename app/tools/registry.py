from collections.abc import Callable
from typing import Any

from app.tools.calculations import (
    calculate_annual_subscription,
    calculate_budget_utilization,
    calculate_gst,
    convert_currency
)

TOOL_REGISTRY: dict[str, Callable[..., Any]] = {
    "calculate_gst": calculate_gst,
    "calculate_budget_utilization": calculate_budget_utilization,
    "calculate_annual_subscription": calculate_annual_subscription,
    "convert_currency": convert_currency,
}


TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "name": "calculate_gst",
        "description": "Calculate GST and the total amount.",
        "parameters": {
            "type": "object",
            "properities": {
                "amount": {
                    "type": "number",
                    "description": "Base amount.",
                },
                "gst_rate": {
                    "type": "number",
                    "description": "GST percentage",
                },
            },
            "required": ["amount", "gst_rate"],
        },
    },
    {
        "name": "calculate_budget_utilization",
        "description": "Calculate budget utilization",
        "parameters": {
            "type": "object",
            "properities": {
                "total_budget": {"type": "number"},
                "used_budget": {"type": "number"},
            },
            "required": ["total_budget", "used_budget"],
        },
    },
    {
        "name": "calculate_annual_subscription",
        "description": "Calculate annual subscription costs.",
        "parameters": {
            "type": "object",
            "properties": {
                "monthly_cost": {"type": "number"},
                "subscription_count": {"type": "integer"},
            },
            "required": ["monthly_cost"],
        },
    },
    {
        "name": "convert_currency",
        "description": "Convert an amount using an exchange rate.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "exchange_rate": {"type": "number"},
            },
            "required": ["amount", "exchange_rate"],
        },
    },
]


def execute_tool(
    tool_name: str,
    arguments: dict[str, Any],
) -> Any:
    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        raise ValueError(f"Unknown tool: {tool_name}")

    return tool(**arguments)


def get_tool_definitions() -> list[dict[str, Any]]:
    return TOOL_DEFINITIONS.copy()