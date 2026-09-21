import Link from "next/link";
import { SiteHeader } from "@/components/site-header";
import { SiteFooter } from "@/components/site-footer";

const pillars = [
  ["Encounter", "Create space for reverence, contemplative practice, and honest attention to transcendent experience."],
  ["Inquiry", "Study religious and philosophical testimony without requiring premature agreement."],
  ["Community", "Build durable relationships through gatherings, groups, meals, learning, and mutual care."],
  ["Service", "Put convictions into practice through volunteer work, mutual aid, and care for the wider world."],
];

export default function HomePage() {
  return (
    <>
      <SiteHeader />
      <main>
        <section className="hero">
          <div className="container heroGrid">
            <div>
              <span className="eyebrow">A community taking shape</span>
              <h1>A place for encounter, inquiry, practice, and shared life.</h1>
              <p className="heroCopy">We are building a religious community that can hold deep conviction and open inquiry together—without requiring every inherited tradition to become the same thing.</p>
              <div className="buttonRow">
                <Link className="button" href="/app">Enter the community</Link>
                <Link className="button secondary" href="/about">Understand the project</Link>
              </div>
            </div>
            <div className="heroPanel">
              <span className="panelLabel">This week</span>
              <h2>Three ways to participate</h2>
              <div className="miniEvent"><b>Sunday · 10:30</b><span>Weekly Assembly</span></div>
              <div className="miniEvent"><b>Tuesday · 7:00</b><span>Origins Reading Circle</span></div>
              <div className="miniEvent"><b>Thursday · 6:30</b><span>Community Table</span></div>
              <Link href="/app/events">View full calendar →</Link>
            </div>
          </div>
        </section>
        <section className="section"><div className="container">
          <div className="sectionHeading"><span className="eyebrow">What we are building</span><h2>More than a website.</h2><p>This platform is the public front door, member commons, research library, giving portal, staff workspace, and governance record of the community.</p></div>
          <div className="cardGrid">{pillars.map(([title, text]) => <article className="featureCard" key={title}><span className="featureIndex">0{pillars.findIndex(x => x[0] === title)+1}</span><h3>{title}</h3><p>{text}</p></article>)}</div>
        </div></section>
        <section className="section splitSection"><div className="container splitGrid">
          <div><span className="eyebrow">Research</span><h2>Study the evidence, not just the conclusions.</h2><p>Our research program compares claimed encounters with transcendent reality across time, cultures, texts, and traditions—distinguishing encounter, testimony, interpretation, and later institution.</p><Link className="textLink" href="/research">Explore the research model →</Link></div>
          <div className="quoteCard"><span>Encounter</span><span>→</span><span>Testimony</span><span>→</span><span>Interpretation</span><span>→</span><span>Tradition</span></div>
        </div></section>
        <section className="section"><div className="container callout"><div><span className="eyebrow">Institutional safeguards</span><h2>Authority should be understandable.</h2><p>Governance, finances, leadership limits, grievance processes, and safeguarding policies belong in public view wherever confidentiality does not require otherwise.</p></div><Link className="button secondary" href="/governance">View governance</Link></div></section>
      </main>
      <SiteFooter />
    </>
  );
}
