from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.procurement_requests import router as procurement_request_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )

    app.include_router(health_router)
    app.include_router(procurement_request_router)

    return app


app = create_app()
