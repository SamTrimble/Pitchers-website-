from typing import Annotated
from uuid import UUID

from fastapi import Depends, Header
from pydantic import BaseModel

from app.api.deps.auth import AuthenticatedUser, get_current_user
from app.core.config import Settings, get_settings
from app.core.errors import TenantContextError


class TenantContext(BaseModel):
    organization_id: UUID
    user_id: UUID | None
    membership_verified: bool


def build_tenant_context(user: AuthenticatedUser, organization_id: UUID) -> TenantContext:
    if organization_id not in user.organization_ids:
        raise TenantContextError(
            "The active organization is not part of the authenticated membership set.",
            code="TENANT_MEMBERSHIP_REQUIRED",
        )
    return TenantContext(
        organization_id=organization_id,
        user_id=user.subject,
        membership_verified=True,
    )


async def get_tenant_context(
    organization_id_header: Annotated[str | None, Header(alias="X-Organization-Id")] = None,
    user: AuthenticatedUser = Depends(get_current_user),
    settings: Settings = Depends(get_settings),
) -> TenantContext:
    raw_org_id = organization_id_header
    if raw_org_id is None:
        raise TenantContextError(
            f"The {settings.organization_header} header is required for tenant-aware routes.",
            code="TENANT_HEADER_REQUIRED",
        )
    try:
        organization_id = UUID(raw_org_id)
    except ValueError as exc:
        raise TenantContextError("The organization header must be a valid UUID.") from exc
    return build_tenant_context(user, organization_id)
