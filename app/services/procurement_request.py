from sqlalchemy.orm import session

from app.repositories.procurement_request import create_procurement_request
from app.schemas.procurement_request import ProcurementRequestCreate


def create_request(db: session, request: ProcurementRequestCreate):
    return create_procurement_request(db, request)
