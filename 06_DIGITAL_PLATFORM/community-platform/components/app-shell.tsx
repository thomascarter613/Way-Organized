import Link from "next/link";
import type { ReactNode } from "react";

const memberNav = [
  ["/app", "Home"], ["/app/events", "Calendar"], ["/app/groups", "Community"],
  ["/app/learn", "Learn"], ["/app/giving", "Give"], ["/research", "Research"],
] as const;

const staffNav = [
  ["/staff", "Dashboard"], ["/app/events", "Events"], ["/app/groups", "Groups"],
  ["/research", "Research"], ["/governance", "Governance"], ["/admin", "Admin"],
] as const;

export function AppShell({ children, mode = "member" }: { children: ReactNode; mode?: "member" | "staff" | "admin" }) {
  const nav = mode === "member" ? memberNav : staffNav;
  return (
    <div className="appFrame">
      <aside className="sidebar">
        <Link className="brand sidebarBrand" href="/"><span className="brandMark">◌</span><span>Community</span></Link>
        <nav className="sideNav" aria-label={`${mode} navigation`}>
          {nav.map(([href, label]) => <Link key={href} href={href}>{label}</Link>)}
        </nav>
        <div className="sidebarFoot">
          <div className="avatar">TC</div>
          <div><strong>Demo User</strong><span>{mode === "member" ? "Participant" : "Staff access"}</span></div>
        </div>
      </aside>
      <main className="appMain">{children}</main>
    </div>
  );
}
