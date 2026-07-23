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
    database_url_override: str | None = Field(default=None, alias="DATABASE_URL")
    database_host: str = Field(default="localhost", alias="DATABASE_HOST")
    database_port: int = Field(default=5432, alias="DATABASE_PORT")
    database_name: str = Field(default="athleteos", alias="DATABASE_NAME")
    database_user: str = Field(default="postgres", alias="DATABASE_USER")
    database_password: str = Field(default="postgres", alias="DATABASE_PASSWORD")
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
    auth_stub_enabled: bool = Field(default=True, alias="AUTH_STUB_ENABLED")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def database_url(self) -> str:
        if self.database_url_override:
            return self.database_url_override
        return (
            "postgresql+psycopg://"
            f"{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
