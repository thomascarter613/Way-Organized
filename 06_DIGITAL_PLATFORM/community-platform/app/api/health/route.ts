export async function GET() {
  return Response.json({ ok: true, service: "community-platform", time: new Date().toISOString() });
}
