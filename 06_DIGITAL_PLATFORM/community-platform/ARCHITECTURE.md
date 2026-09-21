# Architecture baseline

## Principle

The platform is a modular monolith. Public web, member experience, staff workspace, and admin control plane share one identity system, organization model, permission model, and PostgreSQL database.

## Bounded modules

- Identity & access
- Organization & communities
- People & households
- Gatherings & events
- Groups
- Learning
- Content & media
- Giving
- Research / HTERP
- Communications
- Volunteer service
- Governance & transparency
- Safeguarding/private cases
- Audit & system administration

## Authorization

Use capabilities rather than broad account classes. A role grants capabilities inside an organization. Resource/ownership predicates still apply. Sensitive-case access should be separately delegated and must not be inherited automatically by ordinary administrators.

## Data classification

- Public: published pages, public events, public groups, public research records.
- Member: member-specific registrations, group memberships, private community content.
- Staff: operational CRM, internal work queues, unpublished content.
- Restricted: giving details, personnel data, governance drafts.
- Highly restricted: safeguarding/incident cases and similar sensitive records; keep server-only in private schema.

## Deployment topology

```text
Browser / PWA
   |
Next.js modular monolith
   |-- public routes
   |-- member routes
   |-- staff routes
   |-- admin routes
   |-- server actions / route handlers
   |
Supabase
   |-- Auth
   |-- PostgreSQL + RLS
   |-- Storage (later)
   |-- Realtime where justified
   |
External providers (later)
   |-- Stripe
   |-- email/SMS
   |-- observability
```
