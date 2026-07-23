SHELL := /bin/bash
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: setup dev lint typecheck test migrate lint-backend typecheck-backend test-backend lint-frontend typecheck-frontend test-frontend

setup:
	cd frontend && npm install
	cd backend && $(PIP) install -e .[dev]

dev:
	docker compose up --build

lint: lint-frontend lint-backend

typecheck: typecheck-frontend typecheck-backend

test: test-frontend test-backend

migrate:
	cd backend && alembic upgrade head

lint-backend:
	cd backend && ruff check app tests

typecheck-backend:
	cd backend && mypy app tests

test-backend:
	cd backend && pytest

lint-frontend:
	cd frontend && npm run lint

typecheck-frontend:
	cd frontend && npm run typecheck

test-frontend:
	cd frontend && npm run test -- --run
