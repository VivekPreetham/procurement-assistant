from fastapi import APIRouter

from app.schemas.tool_calling import (
    ToolCallRequest,
    ToolCallResponse,
)

from app.services.tool_calling import handle_tool_call

router = APIRouter(
    prefix="/tools",
    tags=["tools"],
)

@router.post(
    "/execute",
    response_model=ToolCallResponse,
)
async def execute_tool_endpoint(
    request: ToolCallRequest,
) -> ToolCallResponse:
    result = handle_tool_call(
        tool_name=request.tool_name,
        arguments=request.arguments,
    )

    return ToolCallResponse(**result)