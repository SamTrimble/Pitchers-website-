from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from app.core.config import Settings

request_id_context: ContextVar[str] = ContextVar("request_id", default="")


class RequestContextMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, *, settings: Settings) -> None:
        super().__init__(app)
        self.settings = settings

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        request_id = request.headers.get(self.settings.request_id_header, str(uuid4()))
        request_id_context.set(request_id)
        response = await call_next(request)
        response.headers[self.settings.request_id_header] = request_id
        return response


def get_request_id() -> str:
    return request_id_context.get() or str(uuid4())
