import Link from "next/link";
import { site } from "@/lib/site";

export function SiteHeader() {
  return (
    <header className="siteHeader">
      <div className="container headerInner">
        <Link className="brand" href="/">
          <span className="brandMark" aria-hidden="true">◌</span>
          <span>{site.name}</span>
        </Link>
        <nav className="publicNav" aria-label="Primary navigation">
          <Link href="/about">About</Link>
          <Link href="/research">Research</Link>
          <Link href="/governance">Governance</Link>
          <Link href="/app/events">Gatherings</Link>
        </nav>
        <div className="headerActions">
          <Link className="textButton" href="/sign-in">Sign in</Link>
          <Link className="button small" href="/app">Enter community</Link>
        </div>
      </div>
    </header>
  );
}
