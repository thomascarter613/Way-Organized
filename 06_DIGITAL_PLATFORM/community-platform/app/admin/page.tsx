import { AppShell } from "@/components/app-shell";

const areas = [
  ["Identity & access", "Roles, capabilities, privileged access, sessions, and invitations."],
  ["Organization", "Communities, locations, households, teams, and organizational settings."],
  ["Integrations", "Payments, email, calendar, storage, analytics, and external services."],
  ["Audit & security", "Privileged actions, security events, policy checks, and exportable audit history."],
  ["Data governance", "Retention schedules, privacy requests, consent, exports, and deletion workflows."],
  ["System", "Feature flags, health, jobs, environment, and operational diagnostics."],
];

export default function AdminPage() {
  return <AppShell mode="admin"><div className="dashboard"><header className="dashboardHeader"><div><span className="eyebrow">Administration</span><h1>System control plane</h1><p>Administrative access is capability-based. Sensitive records should never be exposed merely because someone is an administrator.</p></div></header><div className="directoryGrid">{areas.map(([title,desc]) => <article className="groupCard" key={title}><span className="groupIcon">◇</span><h2>{title}</h2><p>{desc}</p><button className="quietButton">Configure →</button></article>)}</div></div></AppShell>;
}
