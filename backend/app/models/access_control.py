from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import AuditMixin, OrganizationScopedMixin, RoleKeyMixin, TimestampMixin, UUIDPrimaryKeyMixin


class Role(UUIDPrimaryKeyMixin, TimestampMixin, AuditMixin, OrganizationScopedMixin, RoleKeyMixin, Base):
    __tablename__ = "roles"

    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_system_role: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class Permission(UUIDPrimaryKeyMixin, TimestampMixin, AuditMixin, Base):
    __tablename__ = "permissions"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    key: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    resource: Mapped[str] = mapped_column(String(100), nullable=False)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)


class RolePermission(UUIDPrimaryKeyMixin, TimestampMixin, AuditMixin, OrganizationScopedMixin, Base):
    __tablename__ = "role_permissions"
    __table_args__ = (UniqueConstraint("role_id", "permission_id", name="uq_role_permission_pair"),)

    role_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
    permission_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("permissions.id"),
        nullable=False,
    )


class UserRoleAssignment(UUIDPrimaryKeyMixin, TimestampMixin, AuditMixin, OrganizationScopedMixin, Base):
    __tablename__ = "user_role_assignments"
    __table_args__ = (UniqueConstraint("organization_id", "user_id", "role_id", name="uq_user_role_org"),)

    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id"), index=True, nullable=False)
    role_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
