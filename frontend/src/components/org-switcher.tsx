import type { OrganizationSummary } from "@/lib/auth/types";

type OrgSwitcherProps = {
  organizations: OrganizationSummary[];
  activeOrganizationId: string | null;
};

export function OrgSwitcher({ organizations, activeOrganizationId }: OrgSwitcherProps) {
  return (
    <div className="org-switcher">
      <span className="eyebrow">Organization</span>
      <strong>
        {organizations.find((organization) => organization.id === activeOrganizationId)?.name ??
          "Select an organization"}
      </strong>
      <span className="muted">Phase 0 placeholder for tenant switching.</span>
    </div>
  );
}
