from dataclasses import dataclass, field
from uuid import UUID

from app.core.config import Settings


@dataclass(slots=True)
class TokenPayload:
    subject: UUID | None = None
    email: str | None = None
    organization_ids: list[UUID] = field(default_factory=list)
    permissions: list[str] = field(default_factory=list)


class SupabaseJWTVerifier:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def verify(self, token: str) -> TokenPayload:
        del token
        if self.settings.auth_stub_enabled:
            return TokenPayload()
        raise NotImplementedError(
            "Supabase JWT verification is not wired yet. Phase 0 exposes the interface only."
        )
