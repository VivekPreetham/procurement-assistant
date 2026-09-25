from typing import Any
from pydantic import BaseModel, Field

class ToolCallRequest(BaseModel):
    tool_name: str = Field(min_length=1)
    arguments: dict[str, Any]


class ToolCallResponse(BaseModel):
    success: bool
    tool_name: str
    result: dict[str, Any] | None = None
    error: str | None = None