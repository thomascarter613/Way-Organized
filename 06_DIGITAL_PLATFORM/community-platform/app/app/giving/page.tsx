const funds = [
  ["General Fund", "Supports ordinary operations, facilities, programs, and staff."],
  ["Community Assistance", "Direct support for practical needs within the wider community."],
  ["Research & Library", "Sources, archives, publications, and the HTERP research program."],
];

export default function GivingPage() {
  return <div className="dashboard"><header className="dashboardHeader"><div><span className="eyebrow">Giving</span><h1>Support the work.</h1><p>Giving is designed around clear funds, donor control, receipts, and transparent reporting.</p></div></header><div className="dashboardGrid"><section className="panel"><span className="panelLabel">Your giving</span><h2>$0.00</h2><p className="muted">No gifts recorded in this preview account.</p><button className="button">Make a contribution</button></section><section className="panel"><span className="panelLabel">Recurring</span><h2>No recurring gift</h2><p className="muted">Recurring contributions will be managed through the connected payment provider.</p><button className="button secondary">Set up recurring giving</button></section></div><section className="panel"><div className="panelHeader"><div><span className="panelLabel">Funds</span><h2>Choose where to contribute</h2></div></div><div className="fundList">{funds.map(([name,desc]) => <article key={name}><div><strong>{name}</strong><p>{desc}</p></div><button className="quietButton">Give →</button></article>)}</div></section></div>;
}
