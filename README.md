# AthleteOS Phase 0 Foundation

This repository now contains the Phase 0 foundation scaffold for a multi-tenant athlete development platform based on the SRS in `/AthleteOS_Extreme_SRS_v2.md`.

## Stack
- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python 3.12
- Database: PostgreSQL
- Auth: Supabase Auth interface stubs
- Storage: AWS S3 interface stub
- Local orchestration: Docker Compose
- Hosting target: AWS (documented), local development via containers

## Repository layout
- `/frontend` — Next.js app shell, auth placeholders, typed API client, permission guards
- `/backend` — FastAPI app, config, health routes, SQLAlchemy models, auth and tenant stubs, Alembic
- `/docs` — build status, architecture, database, API, security, deployment, testing, roadmap, ADRs
- `/.github/workflows/pr.yml` — pull request validation workflow

## Quick start
1. Copy `.env.example` to `.env` and adjust local values as needed.
2. Install dependencies:
   - `make setup`
3. Start the local stack:
   - `make dev`
4. Apply the initial migration if running the backend outside Docker:
   - `make migrate`

## Validation commands
- `make lint`
- `make typecheck`
- `make test`
- `cd backend && alembic upgrade head`

## Phase 0 deliverables implemented
- Monorepo scaffold with frontend and backend foundations
- Versioned FastAPI health endpoints and consistent API error envelope
- SQLAlchemy entities, common mixins, session management, and first Alembic migration
- Supabase JWT verification and tenant context guard stubs
- Next.js landing page, auth placeholders, protected app shell, and dashboard placeholder
- Docker Compose, Makefile, FE/BE linting, type checking, and tests
- PR CI workflow and supporting documentation

## Next phase
Phase 1 should build athlete management, richer organization workflows, real Supabase wiring, and production-grade role assignment flows on top of this foundation.
