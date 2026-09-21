import { SiteHeader } from "@/components/site-header";
import { SiteFooter } from "@/components/site-footer";

const records = [
  ["Prophetic encounter", "Claimed communication or commissioning associated with a divine or transcendent source."],
  ["Mystical encounter", "Reports of union, presence, absorption, illumination, or altered relation to ultimate reality."],
  ["Visionary encounter", "Dreams, visions, auditions, apparitions, and other extraordinary perceptual claims."],
  ["Contemplative realization", "Experiences arising in sustained contemplative, meditative, ascetic, or ritual practice."],
];

export default function ResearchPage() {
  return <><SiteHeader /><main className="articlePage"><div className="container"><div className="sectionHeading"><span className="eyebrow">HTERP · Research</span><h1>Human testimony about transcendent encounter.</h1><p>The research layer is being designed as structured data, not merely a document archive. Sources, witnesses, dates, locations, claims, evidence, interpretations, and traditions can be related while retaining provenance and uncertainty.</p></div><div className="cardGrid">{records.map(([title,text]) => <article className="featureCard" key={title}><h3>{title}</h3><p>{text}</p><span className="recordTag">Research record type</span></article>)}</div></div></main><SiteFooter /></>;
}
