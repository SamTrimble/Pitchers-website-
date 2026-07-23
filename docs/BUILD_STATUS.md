# Build Status

## Completed work
- Created the monorepo scaffold with `/frontend`, `/backend`, docs, and CI.
- Added a FastAPI application entrypoint, environment-driven settings, request ID middleware, structured API error responses, and `/health` plus `/api/v1/health`.
- Added SQLAlchemy base classes and mixins for UUIDs, UTC timestamps, audit fields, and organization scoping where applicable.
- Added initial Phase 0 entities: `users`, `organizations`, `organization_memberships`, `roles`, `permissions`, `role_permissions`, `user_role_assignments`, `invitations`, and `audit_logs`.
- Initialized Alembic and added the first migration for the Phase 0 schema.
- Added Supabase JWT verification, tenant context, and S3 storage integration stubs for future implementation.
- Added a Next.js landing page, login/register placeholders, protected app shell, org switcher placeholder, dashboard placeholder, typed API client, session abstraction, and permission guard stubs.
- Added Docker Compose, Makefile commands, FE/BE linting, type checking, tests, and a PR validation workflow.
- Added README, architecture, database, API, security, deployment, testing, roadmap, ADR, and contributing documentation.

## Remaining work
- Replace auth and organization stubs with real Supabase session handling and membership resolution.
- Seed roles and permissions through an explicit bootstrap flow instead of placeholders.
- Add persistence-backed tenant context resolution and audited authorization checks on protected routes.
- Introduce Phase 1 athlete management modules and UI flows.

## Setup steps
1. Copy `.env.example` to `.env`.
2. Run `make setup`.
3. Run `make dev`.
4. Run `make migrate` if the backend is started outside Docker Compose.

## Migrations
- Initial Alembic revision: `202607232030_phase0_foundation.py`
- Validation command: `cd backend && alembic upgrade head`

## Test evidence
- Backend: `pytest`
- Frontend: `npm run test -- --run`
- Cross-cutting: `make lint`, `make typecheck`, `make test`
- CI: `.github/workflows/pr.yml` runs FE/BE lint, typecheck, tests, and migration validation on pull requests.

## Known issues
- Supabase JWT verification is intentionally a Phase 0 interface stub and will raise `NotImplementedError` when auth stubs are disabled.
- S3 upload handling is limited to a presigned-upload interface stub.
- Role assignment and invitation flows are schema-complete but not yet exposed through application services or APIs.
