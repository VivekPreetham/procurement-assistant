from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.procurement_request import (
    ProcurementRequestCreate,
    ProcurementRequestResponse
) 
from app.services.procurement_request import (
    create_request,
    get_request,
    get_requests,
) 

router = APIRouter(
    prefix="/procurement-requests",
    tags=["procurement requests"],
)


@router.post(
    "/", 
    response_model=ProcurementRequestResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_procurement_request(
    request: ProcurementRequestCreate,
    db: Session = Depends(get_db),
):
    return create_request(db, request)

@router.get(
    "/",
    response_model=list[ProcurementRequestResponse],
)
async def list_procurement_requests(
    db: Session = Depends(get_db),
):
    return get_requests(db)

@router.get(
    "/{request_id}",
    response_model=ProcurementRequestResponse,
)
async def get_procurement_request_by_id(
    request_id: int,
    db: Session = Depends(get_db),
):
    request = get_request(db, request_id)

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Procurement Request not found",
        )

    return request