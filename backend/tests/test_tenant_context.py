from uuid import uuid4

import pytest

from app.api.deps.auth import AuthenticatedUser
from app.api.deps.tenant import build_tenant_context
from app.core.errors import TenantContextError


def test_build_tenant_context_accepts_member_org() -> None:
    organization_id = uuid4()
    user = AuthenticatedUser(raw_token="token", organization_ids=[organization_id])

    context = build_tenant_context(user, organization_id)

    assert context.organization_id == organization_id
    assert context.membership_verified is True


def test_build_tenant_context_rejects_unknown_org() -> None:
    user = AuthenticatedUser(raw_token="token", organization_ids=[])

    with pytest.raises(TenantContextError):
        build_tenant_context(user, uuid4())
