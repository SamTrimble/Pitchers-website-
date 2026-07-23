import { hasAnyPermission, hasPermission } from "@/lib/permissions/guards";

describe("permission guards", () => {
  it("matches a single permission", () => {
    expect(hasPermission(["dashboard:view"], "dashboard:view")).toBe(true);
  });

  it("matches any permission in a required list", () => {
    expect(hasAnyPermission(["organization:read"], ["dashboard:view", "organization:read"])).toBe(
      true,
    );
  });

  it("rejects when permissions are missing", () => {
    expect(hasAnyPermission([], ["dashboard:view"])).toBe(false);
  });
});
