from collections.abc import Mapping
from http import HTTPStatus
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.request_context import get_request_id


class ApiError(Exception):
    def __init__(
        self,
        *,
        code: str,
        message: str,
        status_code: int,
        details: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = dict(details or {})


class AuthenticationRequiredError(ApiError):
    def __init__(self) -> None:
        super().__init__(
            code="AUTHENTICATION_REQUIRED",
            message="A bearer token is required for this operation.",
            status_code=int(HTTPStatus.UNAUTHORIZED),
        )


class TenantContextError(ApiError):
    def __init__(self, message: str, *, code: str = "TENANT_CONTEXT_INVALID") -> None:
        super().__init__(
            code=code,
            message=message,
            status_code=int(HTTPStatus.FORBIDDEN),
        )


class AuthorizationError(ApiError):
    def __init__(self, permission: str) -> None:
        super().__init__(
            code="PERMISSION_DENIED",
            message=f"The '{permission}' permission is required.",
            status_code=int(HTTPStatus.FORBIDDEN),
        )


def build_error_payload(error: ApiError) -> dict[str, Any]:
    return {
        "error": {
            "code": error.code,
            "message": error.message,
            "details": error.details,
            "request_id": get_request_id(),
        }
    }


async def api_error_handler(_: Request, error: ApiError) -> JSONResponse:
    return JSONResponse(status_code=error.status_code, content=build_error_payload(error))


async def http_error_handler(_: Request, error: StarletteHTTPException) -> JSONResponse:
    phrase = HTTPStatus(error.status_code).phrase if error.status_code in HTTPStatus._value2member_map_ else "HTTP error"
    api_error = ApiError(
        code="HTTP_ERROR",
        message=str(error.detail or phrase),
        status_code=error.status_code,
    )
    return JSONResponse(status_code=error.status_code, content=build_error_payload(api_error))


async def validation_error_handler(_: Request, error: RequestValidationError) -> JSONResponse:
    api_error = ApiError(
        code="VALIDATION_ERROR",
        message="The request payload is invalid.",
        status_code=int(HTTPStatus.UNPROCESSABLE_ENTITY),
        details={"errors": error.errors()},
    )
    return JSONResponse(status_code=api_error.status_code, content=build_error_payload(api_error))


def register_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApiError, api_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
