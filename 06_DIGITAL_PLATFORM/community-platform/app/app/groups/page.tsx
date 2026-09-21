const groups = [
  ["Origins Reading Circle", "Study · Tuesdays", "14 members", "Reading primary sources together and comparing their historical contexts."],
  ["Community Table Team", "Service · Thursdays", "8 volunteers", "Planning shared meals, hospitality, and practical support for gatherings."],
  ["Contemplative Practice", "Practice · Sundays", "21 members", "A quiet practice group exploring disciplined contemplative methods."],
  ["HTERP Research Commons", "Research · Online", "32 contributors", "Collaborative source collection, annotation, and encounter-record review."],
];

export default function GroupsPage() {
  return <div className="dashboard"><header className="dashboardHeader"><div><span className="eyebrow">Community</span><h1>Groups & circles</h1><p>Smaller spaces for study, practice, service, research, and friendship.</p></div><button className="button small">Find a group</button></header><div className="directoryGrid">{groups.map(([name,meta,count,desc]) => <article className="groupCard" key={name}><div className="groupIcon">◌</div><span className="panelLabel">{meta}</span><h2>{name}</h2><p>{desc}</p><div className="groupFoot"><span>{count}</span><button className="quietButton">Open group →</button></div></article>)}</div></div>;
}
