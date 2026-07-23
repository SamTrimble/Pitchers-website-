# Contributing

## Workflow
1. Read `/AthleteOS_Extreme_SRS_v2.md` before changing platform behavior.
2. Keep work aligned to the current implementation phase.
3. Prefer small, reviewable changes.
4. Do not commit secrets, hardcoded tenant identifiers, or authorization bypasses.

## Local development
- Use `make setup` to install frontend and backend dependencies.
- Use `make dev` to run PostgreSQL, Redis, FastAPI, and Next.js together.
- Use `make lint`, `make typecheck`, and `make test` before opening a PR.
- Use `make migrate` after schema changes.

## Pull requests
Each PR should include:
- a short summary of the change
- setup or migration notes when relevant
- test evidence
- remaining follow-up work

## Phase discipline
Phase 0 is limited to platform foundation work. Do not add athlete, workout, recruiting, billing, or AI product features until the foundation is accepted.
