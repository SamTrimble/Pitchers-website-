from typing import Annotated
from uuid import UUID

from fastapi import Depends, Header
from pydantic import BaseModel, EmailStr

from app.core.config import Settings, get_settings
from app.core.errors import ApiError, AuthenticationRequiredError
from app.integrations.auth.supabase import SupabaseJWTVerifier, TokenPayload


class AuthenticatedUser(BaseModel):
    subject: UUID | None = None
    email: EmailStr | None = None
    organization_ids: list[UUID] = []
    permissions: list[str] = []
    raw_token: str


async def get_current_user(
    authorization: Annotated[str | None, Header()] = None,
    settings: Settings = Depends(get_settings),
) -> AuthenticatedUser:
    if not authorization:
        raise AuthenticationRequiredError()

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise AuthenticationRequiredError()

    verifier = SupabaseJWTVerifier(settings)
    payload = await verifier.verify(token)
    return AuthenticatedUser(
        subject=payload.subject,
        email=payload.email,
        organization_ids=payload.organization_ids,
        permissions=payload.permissions,
        raw_token=token,
    )


def require_permission(permission: str):
    def dependency(user: AuthenticatedUser = Depends(get_current_user)) -> AuthenticatedUser:
        if permission not in user.permissions:
            raise ApiError(
                code="PERMISSION_DENIED",
                message=f"The '{permission}' permission is required.",
                status_code=403,
            )
        return user

    return dependency
