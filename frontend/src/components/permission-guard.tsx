import { hasAnyPermission } from "@/lib/permissions/guards";

type PermissionGuardProps = {
  permissions: string[];
  required: string[];
  children: React.ReactNode;
  fallback?: React.ReactNode;
};

export function PermissionGuard({
  permissions,
  required,
  children,
  fallback = <p className="muted">Permission placeholder: access rules will tighten in Phase 1.</p>,
}: PermissionGuardProps) {
  return hasAnyPermission(permissions, required) ? <>{children}</> : <>{fallback}</>;
}
