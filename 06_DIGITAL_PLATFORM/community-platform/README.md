# Community Platform

A functional foundation for a religious/community institution whose permanent public name is intentionally not yet fixed. The same application supports public discovery, member participation, staff operations, research, giving, governance, and administration.

## What is implemented

- Public homepage plus About, Research, and Governance pages
- Member application shell and dashboard
- Gatherings/events, groups, learning, and giving surfaces
- Staff operations dashboard
- Admin control plane shell
- Supabase SSR client integration and magic-link sign-in route
- Next.js 16 `proxy.ts` session refresh pattern
- PostgreSQL/Supabase foundation migration with RLS
- Capability-oriented authorization schema
- Private schema for audit/sensitive-case records
- Responsive UI and health endpoint
- Biome lint/format configuration

The UI contains demo data so the product can be reviewed before a backend is connected. Once Supabase variables are present, the sign-in flow becomes live.

## Stack

- Next.js 16.3.5 / App Router
- React 19.3
- TypeScript
- Supabase Auth + PostgreSQL + RLS
- Plain CSS design system to keep the foundation dependency-light
- Biome

## Run locally

```bash
cp .env.example .env.local
npm install
npm run dev
```

Open `http://localhost:3000`.

The project is package-manager neutral; `bun install && bun dev` can be used instead when Bun is available.

## Configure Supabase

1. Create a Supabase project.
2. Copy `.env.example` to `.env.local` and set the project URL and **publishable** key.
3. Apply `supabase/migrations/0001_foundation.sql` through the Supabase CLI/MCP migration workflow.
4. In Auth URL configuration, add your local and deployed `/auth/callback` URLs.
5. Create an organization and organization membership seed before enabling staff authorization.

Never put a Supabase secret/service-role key in a `NEXT_PUBLIC_*` variable.

## Security model

- Every exposed `public` table has RLS enabled.
- Authenticated does **not** mean authorized: self-service tables use `auth.uid()` ownership predicates.
- Highly sensitive records are placed under `private`, which is revoked from client roles.
- User authorization is modeled with organizations, memberships, roles, capabilities, and role-capability links rather than an `admin = true` flag.
- The auth user provisioning function lives in the private schema and has client execution revoked.

Before production, add organization-scoped staff authorization policies, server-only privileged actions, automated security tests, MFA requirements for staff, and formal retention/privacy rules.

## Product map

```text
/                 Public front door
/about            Institutional orientation
/research         HTERP/research explorer foundation
/governance       Transparency and safeguards
/sign-in          Supabase magic-link auth
/app              Member home
/app/events       Gatherings/events
/app/groups       Groups/circles
/app/learn        Learning
/app/giving       Donor portal foundation
/staff            Staff operations
/admin            Administrative control plane
/api/health       Health check
```

## Immediate next implementation slices

1. Connect a real Supabase project and generate typed database definitions.
2. Replace demo dashboard data with authenticated queries.
3. Implement organization-scoped capability checks on the server and in RLS.
4. Add content authoring/review/publishing workflows.
5. Add Stripe Checkout + webhook-backed donation ledger.
6. Implement event RSVP/check-in and group membership actions.
7. Add the structured HTERP source/encounter/claim/evidence model.
8. Add communications, volunteer scheduling, reporting, governance records, privacy tooling, and audit viewers.
