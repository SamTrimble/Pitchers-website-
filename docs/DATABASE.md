# Database

## Core Phase 0 tables
- `users`
- `organizations`
- `organization_memberships`
- `roles`
- `permissions`
- `role_permissions`
- `user_role_assignments`
- `invitations`
- `audit_logs`

## Shared model patterns
Most Phase 0 tables use:
- `id` as UUID primary key
- `created_at` and `updated_at` in UTC
- `created_by` and `updated_by` audit fields
- `organization_id` when the record is tenant-owned or tenant-scoped

## Notes
- `roles`, `role_permissions`, and `user_role_assignments` allow nullable `organization_id` so the model can evolve toward platform-wide roles while still enforcing tenant scoping for organization-owned data.
- `audit_logs` capture actor, target entity, request ID, and metadata for future audit trails.

## Migration
Use `cd backend && alembic upgrade head` to apply the initial schema.
