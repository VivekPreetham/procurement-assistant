from sqlalchemy.orm import Session

from app.repositories.procurement_request import (
    create_procurement_request,
    get_procurement_request,
    get_procurement_requests,
) 
from app.schemas.procurement_request import ProcurementRequestCreate


def create_request(
        db: Session,
        request: ProcurementRequestCreate
):
    return create_procurement_request(db, request)

def get_requests(db: Session):
    return get_procurement_requests(db)

def get_request(
    db: Session,
    request_id: int,
):
    return get_procurement_request(db, request_id)