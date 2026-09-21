import Link from "next/link";
import { site } from "@/lib/site";

export function SiteFooter() {
  return (
    <footer className="siteFooter">
      <div className="container footerGrid">
        <div>
          <div className="brand footerBrand"><span className="brandMark">◌</span>{site.name}</div>
          <p className="muted maxText">A digital home for inquiry, shared practice, learning, service, and community life.</p>
        </div>
        <div>
          <strong>Explore</strong>
          <Link href="/about">About</Link>
          <Link href="/research">Research</Link>
          <Link href="/governance">Governance</Link>
        </div>
        <div>
          <strong>Participate</strong>
          <Link href="/app/events">Gatherings</Link>
          <Link href="/app/groups">Groups</Link>
          <Link href="/app/giving">Give</Link>
        </div>
      </div>
    </footer>
  );
}
