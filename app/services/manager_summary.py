from app.schemas.manager_summary import (
    ManagerRequestInput,
    ComplianceInput,
    RequestedItem,
    ManagerSummaryResponse
)


def generate_manager_summary(
    request: ManagerRequestInput,
    compliance: ComplianceInput,
) -> ManagerSummaryResponse:
    
    estimated_cost = request.estimated_budget

    if not compliance.is_compliant:
        compliance_status = "Non-Compliant"
        recommended_action = "Review compliance violations"

    elif compliance.warnings:
        compliance_status = "Compliant with warnings"
        recommended_action = "Review warnings before approval"
    else:
        compliance_status = "Compliant"
        recommended_action = "Approve"

    risks = [
        *compliance.violations,
        *compliance.warnings
    ]

    summary = (
        f"Procurement request for {request.item}. "
        f"Quantity: {request.quantity}. "
        f"Esimated cost: {estimated_cost}. "
        f"Department: {request.department}. "
        f"Compliance status: {compliance_status}."
    )

    return ManagerSummaryResponse(
        summary=summary,
        requested_items=[
            RequestedItem(
                item=request.item,
                quantity=request.quantity,
            )
        ],
        estimated_cost=estimated_cost,
        business_justification=request.business_justification,
        department=request.department,
        delivery_timeline=request.delivery_timeline,
        compliance_status=compliance_status,
        risks=risks,
        recommended_action=recommended_action
    )