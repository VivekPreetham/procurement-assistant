from sqlalchemy import select
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

def get_procurement_requests(
    db: Session,
) -> list[ProcurementRequest]:
    statement = select(ProcurementRequest).order_by(
        ProcurementRequest.created_at.desc()
    )

    return list(db.scalars(statement).all())

def get_procurement_request(
    db: Session,
    request_id: int,
) -> ProcurementRequest | None:
    return db.get(ProcurementRequest, request_id)