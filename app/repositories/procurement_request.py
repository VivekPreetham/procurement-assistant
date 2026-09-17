from sqlalchemy.orm import Session

from app.models.procurement_request import ProcurementRequest
from app.schemas.procurement_request import ProcurementRequestCreate


def create_procurement_request(
    db: Session, request: ProcurementRequestCreate
) -> ProcurementRequest:
    procurement_request = ProcurementRequest(**request.model_dump())

    db.add(procurement_request)
    db.commit()
    db.refresh(procurement_request)

    return procurement_request
