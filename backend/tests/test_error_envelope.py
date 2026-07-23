from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.core.errors import ApiError, register_error_handlers
from app.core.request_context import RequestContextMiddleware


def test_api_error_envelope_shape() -> None:
    local_app = FastAPI()
    local_app.add_middleware(RequestContextMiddleware, settings=get_settings())
    register_error_handlers(local_app)

    @local_app.get("/boom")
    def boom() -> None:
        raise ApiError(code="TEST_ERROR", message="broken", status_code=418)

    client = TestClient(local_app)
    response = client.get("/boom")

    assert response.status_code == 418
    payload = response.json()["error"]
    assert payload["code"] == "TEST_ERROR"
    assert payload["request_id"]
