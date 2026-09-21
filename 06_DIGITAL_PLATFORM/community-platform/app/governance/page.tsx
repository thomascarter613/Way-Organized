import { SiteHeader } from "@/components/site-header";
import { SiteFooter } from "@/components/site-footer";

const safeguards = ["Published governing documents", "Leadership selection and removal rules", "Conflict-of-interest controls", "Financial reporting", "Grievance and appeal processes", "Safeguarding and incident reporting", "Freedom to leave and dissent", "Audit trails for privileged actions"];

export default function GovernancePage() {
  return <><SiteHeader /><main className="articlePage"><div className="container narrow"><span className="eyebrow">Governance & safeguards</span><h1>Institutional authority should be legible.</h1><p className="lead">The platform is designed so governance is not hidden behind organizational mystique. Public records and internal accountability workflows are first-class product features.</p><div className="checkList">{safeguards.map(item => <div key={item}><span>✓</span>{item}</div>)}</div><p className="muted">Confidential case information, private personal data, and legally protected records remain restricted even when the governing process itself is transparent.</p></div></main><SiteFooter /></>;
}
