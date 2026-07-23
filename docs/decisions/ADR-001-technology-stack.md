# ADR-001: Technology Stack

## Status
Accepted

## Decision
Phase 0 uses:
- Next.js + TypeScript for the frontend
- FastAPI on Python 3.12+ for the backend
- PostgreSQL for persistence
- Supabase Auth for identity integration
- AWS S3 for object storage interfaces
- Docker Compose for local development
- AWS as the documented hosting target

## Rationale
- The stack matches the finalized project direction and SRS guidance.
- FastAPI, SQLAlchemy, and Alembic support explicit APIs and migrations.
- Next.js provides a modern app shell for responsive product development.
- Supabase and S3 are isolated behind interfaces so the platform can evolve without rewriting the entire foundation.
