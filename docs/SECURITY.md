# Security

## Phase 0 controls
- UUID primary keys are used across the initial domain entities.
- Tenant-aware entities carry `organization_id` fields where applicable.
- Request IDs are attached to responses and error envelopes for traceability.
- Authorization is modeled through explicit role and permission entities.
- No secrets are committed; `.env.example` contains placeholder values only.

## Known deferred items
- Real Supabase signature verification and key rotation
- persistent membership-backed tenant resolution
- route-level authorization on business endpoints
- signed S3 upload policies and content validation

## Guardrails
- Do not hardcode user or organization identifiers.
- Keep timestamps in UTC.
- Treat AI, recruiting, medical, and billing data as out of scope until later phases add proper controls.
