from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.procurement_request import ProcurementRequestCreate
from app.services.procurement_request import create_request

router = APIRouter(
    prefix="/procurement-requests",
    tags=["procurement requests"],
)


@router.post("/")
async def create_procurement_request(
    request: ProcurementRequestCreate,
    db: Session = Depends(get_db),
):
    return create_request(db, request)
