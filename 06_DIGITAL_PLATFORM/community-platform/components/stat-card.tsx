export function StatCard({ label, value, detail }: { label: string; value: string; detail: string }) {
  return <article className="statCard"><span>{label}</span><strong>{value}</strong><small>{detail}</small></article>;
}
