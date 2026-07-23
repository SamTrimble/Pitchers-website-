import { ApiClientError, parseApiError } from "@/lib/api/errors";

export type RequestOptions = RequestInit & {
  accessToken?: string;
};

export function buildApiUrl(pathname: string): string {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
  return new URL(pathname, baseUrl).toString();
}

export async function apiRequest<T>(pathname: string, options: RequestOptions = {}): Promise<T> {
  const { accessToken, headers, ...init } = options;
  const response = await fetch(buildApiUrl(pathname), {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(accessToken ? { Authorization: `****** } : {}),
      ...headers,
    },
  });

  if (!response.ok) {
    throw await parseApiError(response);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return (await response.json()) as T;
}

export async function getHealth(): Promise<{ status: string; service: string }> {
  try {
    return await apiRequest<{ status: string; service: string }>("/api/v1/health");
  } catch (error) {
    if (error instanceof ApiClientError) {
      throw error;
    }
    throw new ApiClientError({
      code: "NETWORK_ERROR",
      message: "The API is currently unavailable.",
      status: 503,
    });
  }
}
