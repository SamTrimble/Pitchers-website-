from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.errors import register_error_handlers
from app.core.logging import configure_logging
from app.core.request_context import RequestContextMiddleware


def create_application() -> FastAPI:
    settings = get_settings()
    configure_logging()

    app = FastAPI(
        title=settings.project_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.add_middleware(RequestContextMiddleware, settings=settings)
    register_error_handlers(app)
    app.include_router(api_router)
    return app
