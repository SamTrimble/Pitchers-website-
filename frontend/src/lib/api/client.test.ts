import { apiRequest, buildApiUrl } from "@/lib/api/client";
import { ApiClientError, parseApiError } from "@/lib/api/errors";

const originalFetch = global.fetch;

describe("api client", () => {
  afterEach(() => {
    global.fetch = originalFetch;
  });

  it("builds API URLs from the configured base", () => {
    expect(buildApiUrl("/api/v1/health")).toBe("http://localhost:8000/api/v1/health");
  });

  it("parses structured API errors", async () => {
    const response = new Response(
      JSON.stringify({
        error: {
          code: "TENANT_HEADER_REQUIRED",
          message: "Missing tenant header",
          details: {},
          request_id: "req-123",
        },
      }),
      { status: 403 },
    );

    await expect(parseApiError(response)).resolves.toMatchObject({
      code: "TENANT_HEADER_REQUIRED",
      requestId: "req-123",
      status: 403,
    });
  });

  it("throws ApiClientError when a request fails", async () => {
    global.fetch = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          error: {
            code: "HTTP_ERROR",
            message: "Not found",
            details: {},
            request_id: "req-404",
          },
        }),
        { status: 404 },
      ),
    ) as typeof global.fetch;

    await expect(apiRequest("/missing")).rejects.toBeInstanceOf(ApiClientError);
  });
});
