const courses = [
  ["Encounter & Testimony", "42%", "Foundations", "How to distinguish reported event, memory, testimony, interpretation, and institutional reception."],
  ["Reading Traditions Historically", "0%", "Methods", "A practical introduction to source criticism, historical context, genre, and transmission."],
  ["Community & Discernment", "0%", "Formation", "Practices for disagreement, communal reasoning, conscience, and accountable decision-making."],
];

export default function LearnPage() {
  return <div className="dashboard"><header className="dashboardHeader"><div><span className="eyebrow">Learning</span><h1>Your learning path</h1><p>Courses, reading programs, guided practices, and facilitated cohorts.</p></div></header><div className="directoryGrid">{courses.map(([name,progress,tag,desc]) => <article className="groupCard" key={name}><span className="recordTag">{tag}</span><h2>{name}</h2><p>{desc}</p><div className="progressTrack"><span style={{width:progress}}/></div><div className="groupFoot"><span>{progress} complete</span><button className="quietButton">Continue →</button></div></article>)}</div></div>;
}
