# Architecture

## Overview
Phase 0 establishes a multi-tenant monorepo with a Next.js frontend and FastAPI backend. The frontend consumes versioned backend APIs through a typed client. The backend owns tenant isolation, RBAC enforcement, persistence, and integration boundaries.

## Components
- **Frontend**: App Router shell, public placeholders, protected shell, session abstraction, permission guards.
- **Backend**: FastAPI app, settings, request IDs, error envelope, health endpoints, SQLAlchemy models, Alembic migrations.
- **Persistence**: PostgreSQL for relational data and Redis reserved for queue/session support.
- **External boundaries**: Supabase Auth JWT verification interface and AWS S3 upload interface stub.

## Multi-tenant boundary
- Tenant-owned records include `organization_id` where applicable.
- Tenant context is modeled through an authenticated user plus an organization header.
- RBAC is split across roles, permissions, role-permission joins, and user role assignments.

## Phase 0 design principles
- UUID primary keys
- UTC timestamps
- explicit versioned API routes
- consistent error envelopes
- readable, testable modules
- no secrets in source control
