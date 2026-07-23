# API

## Health endpoints
- `GET /health`
- `GET /api/v1/health`

Both endpoints return:

```json
{
  "status": "ok",
  "service": "AthleteOS Platform",
  "environment": "local",
  "version": "0.1.0"
}
```

## Error envelope
All handled backend errors return:

```json
{
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "The 'dashboard:view' permission is required.",
    "details": {},
    "request_id": "uuid"
  }
}
```

## Phase 0 integration boundaries
- Supabase JWT verification lives behind `SupabaseJWTVerifier`.
- Tenant resolution lives behind `get_tenant_context`.
- S3 upload preparation lives behind `S3ObjectStorageStub`.
