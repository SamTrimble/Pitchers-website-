"use client";

import { PermissionGuard } from "@/components/permission-guard";
import { useSession } from "@/lib/auth/session-provider";

export default function DashboardPage() {
  const { session } = useSession();

  if (!session) {
    return null;
  }

  return (
    <section className="narrow-stack">
      <div className="panel">
        <p className="eyebrow">Dashboard Placeholder</p>
        <h2>Welcome back, {session.user.displayName}</h2>
        <p className="muted">
          This protected shell proves the route structure, auth abstraction, and tenant-aware
          UI placeholders for the next phases.
        </p>
      </div>
      <PermissionGuard permissions={session.permissions} required={["dashboard:view"]}>
        <div className="panel card-grid">
          <div>
            <h3>Organization context</h3>
            <p className="muted">Active org: {session.organizations[0]?.name ?? "Unavailable"}</p>
          </div>
          <div>
            <h3>API readiness</h3>
            <p className="muted">Typed client is ready for health, auth, and tenant-aware APIs.</p>
          </div>
        </div>
      </PermissionGuard>
    </section>
  );
}
