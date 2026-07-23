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

function createStubSession(): AppSession {
  const userId = crypto.randomUUID();
  const organizationId = crypto.randomUUID();

  return {
    accessToken: "phase-0-stub-token",
    user: {
      id: userId,
      email: "owner@example.com",
      displayName: "Org Owner",
    },
    organizations: [
      {
        id: organizationId,
        name: "Pitchers Lab",
        slug: "pitchers-lab",
      },
    ],
    activeOrganizationId: organizationId,
    permissions: ["dashboard:view", "organization:read"],
  };
}

const SessionContext = createContext<SessionContextValue | undefined>(undefined);

export function SessionProvider({ children }: { children: React.ReactNode }) {
  const [session, setSession] = useState<AppSession | null>(() =>
    authStubEnabled ? createStubSession() : null,
  );
  const status: SessionStatus = session ? "authenticated" : "unauthenticated";

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
