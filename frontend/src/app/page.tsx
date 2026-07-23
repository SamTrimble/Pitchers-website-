import Link from "next/link";

const foundationTracks = [
  "Multi-tenant FastAPI backend with SQLAlchemy and Alembic",
  "Next.js app shell with typed API access and auth abstractions",
  "Docker Compose, CI, testing, and Phase 0 documentation",
];

export default function Home() {
  return (
    <main className="page-shell landing-grid">
      <section className="hero-card">
        <p className="eyebrow">Phase 0 Foundation</p>
        <h1>Remote athlete development platform scaffold</h1>
        <p className="muted">
          This repository now carries the initial foundation for the AthleteOS monorepo,
          aligned to the SRS and ready for Phase 1 athlete management work.
        </p>
        <div className="button-row">
          <Link className="button primary" href="/app">
            Open protected shell
          </Link>
          <Link className="button secondary" href="/login">
            View auth placeholder
          </Link>
        </div>
      </section>
      <section className="panel">
        <h2>Included in this drop</h2>
        <ul>
          {foundationTracks.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
