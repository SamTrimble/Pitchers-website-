export type OrganizationSummary = {
  id: string;
  name: string;
  slug: string;
};

export type AppSession = {
  accessToken: string;
  user: {
    id: string;
    email: string;
    displayName: string;
  };
  organizations: OrganizationSummary[];
  activeOrganizationId: string | null;
  permissions: string[];
};

export type SessionStatus = "loading" | "authenticated" | "unauthenticated";
