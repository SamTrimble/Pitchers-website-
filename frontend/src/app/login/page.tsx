import Link from "next/link";

export default function LoginPage() {
  return (
    <main className="page-shell narrow-stack">
      <div className="panel">
        <p className="eyebrow">Auth Placeholder</p>
        <h1>Sign in with Supabase</h1>
        <p className="muted">
          Phase 0 only ships the session abstraction layer. Email/password, social login,
          verification, and MFA wiring land in the next implementation steps.
        </p>
        <div className="button-row">
          <Link className="button primary" href="/app">
            Continue to shell
          </Link>
          <Link className="button secondary" href="/register">
            Open registration placeholder
          </Link>
        </div>
      </div>
    </main>
  );
}
