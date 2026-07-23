# Deployment

## Local
- Use `docker compose up --build` or `make dev`.
- Services: PostgreSQL, Redis, FastAPI backend, Next.js frontend.

## AWS target
Phase 0 documents AWS as the deployment target:
- frontend hosted behind a CDN or managed Node runtime
- backend hosted on a container platform such as ECS/Fargate or App Runner
- PostgreSQL on a managed database service
- Redis on a managed cache service
- object uploads via S3

## Release notes
- Apply Alembic migrations before enabling new backend revisions.
- Keep `.env` values environment-specific and out of source control.
- Promote real auth, storage, and secret management before production use.
