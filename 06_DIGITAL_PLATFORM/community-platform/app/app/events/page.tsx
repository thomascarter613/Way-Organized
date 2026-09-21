const events = [
  { day: "20", month: "SEP", title: "Weekly Assembly", time: "10:30 AM–12:00 PM", place: "Main Hall", type: "Gathering" },
  { day: "22", month: "SEP", title: "Origins Reading Circle", time: "7:00–8:30 PM", place: "Online", type: "Study" },
  { day: "24", month: "SEP", title: "Community Table", time: "6:30–8:00 PM", place: "Commons", type: "Meal" },
  { day: "27", month: "SEP", title: "Contemplative Practice", time: "9:00–10:00 AM", place: "Quiet Room", type: "Practice" },
];

export default function EventsPage() {
  return <div className="dashboard"><header className="dashboardHeader"><div><span className="eyebrow">Calendar</span><h1>Gatherings & events</h1><p>Public gatherings, learning, service, and community life in one calendar.</p></div><button className="button small">Add to calendar</button></header><div className="filterRow"><button className="filter active">All</button><button className="filter">Gatherings</button><button className="filter">Learning</button><button className="filter">Service</button><button className="filter">Online</button></div><section className="panel eventDirectory">{events.map(event => <article key={event.title} className="directoryEvent"><div className="dateBlock"><span>{event.month}</span><strong>{event.day}</strong></div><div><span className="recordTag">{event.type}</span><h2>{event.title}</h2><p>{event.time} · {event.place}</p></div><button className="button secondary small">RSVP</button></article>)}</section></div>;
}
