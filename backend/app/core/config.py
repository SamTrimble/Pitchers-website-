from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = Field(default="AthleteOS Platform", alias="PROJECT_NAME")
    environment: str = Field(default="local", alias="ENVIRONMENT")
    backend_host: str = Field(default="0.0.0.0", alias="BACKEND_HOST")
    backend_port: int = Field(default=8000, alias="BACKEND_PORT")
    frontend_url: str = Field(default="http://localhost:3000", alias="FRONTEND_URL")
    backend_url: str = Field(default="http://localhost:8000", alias="BACKEND_URL")
    database_url: str = Field(
        default="******localhost:5432/athleteos",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    auth_secret: str = Field(default="replace-me", alias="AUTH_SECRET")
    supabase_url: str = Field(default="https://example.supabase.co", alias="SUPABASE_URL")
    supabase_jwks_url: str = Field(
        default="https://example.supabase.co/auth/v1/.well-known/jwks.json",
        alias="SUPABASE_JWKS_URL",
    )
    supabase_jwt_audience: str = Field(default="authenticated", alias="SUPABASE_JWT_AUDIENCE")
    supabase_jwt_issuer: str = Field(
        default="https://example.supabase.co/auth/v1",
        alias="SUPABASE_JWT_ISSUER",
    )
    s3_bucket: str = Field(default="athleteos-local", alias="S3_BUCKET")
    s3_region: str = Field(default="us-east-1", alias="S3_REGION")
    s3_access_key_id: str = Field(default="local-access-key", alias="S3_ACCESS_KEY_ID")
    s3_secret_access_key: str = Field(
        default="local-secret-key",
        alias="S3_SECRET_ACCESS_KEY",
    )
    request_id_header: str = Field(default="X-Request-Id")
    organization_header: str = Field(
        default="X-Organization-Id",
        alias="DEFAULT_ORGANIZATION_HEADER",
    )
    auth_stub_enabled: bool = Field(default=True, alias="NEXT_PUBLIC_ENABLE_AUTH_STUB")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
