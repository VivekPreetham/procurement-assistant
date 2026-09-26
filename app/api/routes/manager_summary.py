from fastapi import APIRouter

from app.schemas.manager_summary import (
    ManagerRequestInput,
    ManagerSummaryResponse,
    ComplianceInput
)
from app.services.manager_summary import generate_manager_summary

router = APIRouter(
    prefix="/manager",
    tags=["manager"],
)


@router.post(
    "/summary",
    response_model=ManagerSummaryResponse
)
async def generate_summary_endpoint(
    request: ManagerRequestInput,
    compliance: ComplianceInput,
) -> ManagerSummaryResponse:
    return generate_manager_summary(
        request=request,
        compliance=compliance
    )