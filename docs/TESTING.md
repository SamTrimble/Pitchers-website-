# Testing

## Backend
- `cd backend && pytest`
- `cd backend && ruff check app tests`
- `cd backend && mypy app tests`

## Frontend
- `cd frontend && npm run lint`
- `cd frontend && npm run typecheck`
- `cd frontend && npm run test -- --run`

## CI
The PR workflow runs:
- frontend lint
- frontend typecheck
- frontend tests
- backend lint
- backend typecheck
- backend tests
- Alembic migration validation against PostgreSQL
