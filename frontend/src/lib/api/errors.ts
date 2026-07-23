export type ApiErrorEnvelope = {
  error: {
    code: string;
    message: string;
    details: Record<string, unknown>;
    request_id: string;
  };
};

export class ApiClientError extends Error {
  code: string;
  details: Record<string, unknown>;
  requestId: string;
  status: number;

  constructor(params: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
    requestId?: string;
    status: number;
  }) {
    super(params.message);
    this.name = "ApiClientError";
    this.code = params.code;
    this.details = params.details ?? {};
    this.requestId = params.requestId ?? "unknown";
    this.status = params.status;
  }
}

export async function parseApiError(response: Response): Promise<ApiClientError> {
  let payload: ApiErrorEnvelope | null = null;

  try {
    payload = (await response.json()) as ApiErrorEnvelope;
  } catch {
    payload = null;
  }

  return new ApiClientError({
    code: payload?.error.code ?? "UNEXPECTED_ERROR",
    message: payload?.error.message ?? "An unexpected API error occurred.",
    details: payload?.error.details ?? {},
    requestId: payload?.error.request_id ?? "unknown",
    status: response.status,
  });
}
