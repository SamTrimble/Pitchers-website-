from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def public_health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.project_name,
        environment=settings.environment,
        version="0.1.0",
    )


@router.get("/api/v1/health", response_model=HealthResponse)
def versioned_health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.project_name,
        environment=settings.environment,
        version="0.1.0",
    )
