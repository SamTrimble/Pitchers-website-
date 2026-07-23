"use client";

import Link from "next/link";

import { AppShell } from "@/components/app-shell";
import { useSession } from "@/lib/auth/session-provider";

export default function ProtectedLayout({ children }: { children: React.ReactNode }) {
  const { session, status } = useSession();

  if (status !== "authenticated" || !session) {
    return (
      <main className="page-shell narrow-stack">
        <div className="panel">
          <p className="eyebrow">Protected Route Stub</p>
          <h1>Authentication required</h1>
          <p className="muted">
            Phase 0 keeps the protected shell behind the session abstraction without wiring
            the real Supabase flows yet.
          </p>
          <Link className="button primary" href="/login">
            Go to login placeholder
          </Link>
        </div>
      </main>
    );
  }

  return <AppShell session={session}>{children}</AppShell>;
}
