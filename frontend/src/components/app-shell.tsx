import Link from "next/link";

import { OrgSwitcher } from "@/components/org-switcher";
import type { AppSession } from "@/lib/auth/types";

type AppShellProps = {
  session: AppSession;
  children: React.ReactNode;
};

const navigation = [
  { href: "/app", label: "Dashboard" },
  { href: "/app/athletes", label: "Athletes (Phase 1)" },
  { href: "/app/settings", label: "Settings (stub)" },
];

export function AppShell({ session, children }: AppShellProps) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <p className="eyebrow">Protected App</p>
          <h1>AthleteOS</h1>
          <p className="muted">Supabase session and RBAC plumbing land in Phase 1.</p>
        </div>
        <OrgSwitcher
          organizations={session.organizations}
          activeOrganizationId={session.activeOrganizationId}
        />
        <nav>
          <ul>
            {navigation.map((item) => (
              <li key={item.href}>
                <Link href={item.href}>{item.label}</Link>
              </li>
            ))}
          </ul>
        </nav>
      </aside>
      <main className="content">{children}</main>
    </div>
  );
}
