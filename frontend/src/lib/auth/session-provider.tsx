"use client";

import { createContext, useContext, useMemo, useState } from "react";

import type { AppSession, SessionStatus } from "@/lib/auth/types";

type SessionContextValue = {
  session: AppSession | null;
  status: SessionStatus;
  setSession: (nextSession: AppSession | null) => void;
  signOut: () => void;
};

const authStubEnabled = process.env.NEXT_PUBLIC_ENABLE_AUTH_STUB === "true";

const stubSession: AppSession = {
  accessToken: "phase-0-stub-token",
  user: {
    id: "00000000-0000-0000-0000-000000000001",
    email: "owner@example.com",
    displayName: "Org Owner",
  },
  organizations: [
    {
      id: "00000000-0000-0000-0000-000000000101",
      name: "Pitchers Lab",
      slug: "pitchers-lab",
    },
  ],
  activeOrganizationId: "00000000-0000-0000-0000-000000000101",
  permissions: ["dashboard:view", "organization:read"],
};

const SessionContext = createContext<SessionContextValue | undefined>(undefined);

export function SessionProvider({ children }: { children: React.ReactNode }) {
  const [session, setSession] = useState<AppSession | null>(authStubEnabled ? stubSession : null);
  const status: SessionStatus = authStubEnabled ? "authenticated" : "unauthenticated";

  const value = useMemo<SessionContextValue>(
    () => ({
      session,
      status,
      setSession,
      signOut: () => setSession(null),
    }),
    [session, status],
  );

  return <SessionContext.Provider value={value}>{children}</SessionContext.Provider>;
}

export function useSession() {
  const context = useContext(SessionContext);
  if (!context) {
    throw new Error("useSession must be used within a SessionProvider");
  }
  return context;
}
