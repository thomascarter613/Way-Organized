-- Community Platform foundation
-- Public-facing data lives in public with RLS.
-- Sensitive operational data belongs in private and is server-only.

create extension if not exists pgcrypto;
create schema if not exists private;
revoke all on schema private from public, anon, authenticated;

create table public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  display_name text,
  first_name text,
  last_name text,
  avatar_path text,
  bio text,
  directory_visible boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.organizations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text not null unique,
  status text not null default 'active' check (status in ('active','archived')),
  created_at timestamptz not null default now()
);

create table public.organization_memberships (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  membership_status text not null default 'active' check (membership_status in ('invited','active','inactive')),
  joined_at timestamptz not null default now(),
  unique (organization_id, user_id)
);

create table public.roles (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  key text not null,
  name text not null,
  description text,
  unique (organization_id, key)
);

create table public.capabilities (
  id uuid primary key default gen_random_uuid(),
  key text not null unique,
  description text not null
);

create table public.role_capabilities (
  role_id uuid not null references public.roles(id) on delete cascade,
  capability_id uuid not null references public.capabilities(id) on delete cascade,
  primary key (role_id, capability_id)
);

create table public.member_roles (
  organization_membership_id uuid not null references public.organization_memberships(id) on delete cascade,
  role_id uuid not null references public.roles(id) on delete cascade,
  primary key (organization_membership_id, role_id)
);

create table public.communities (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  parent_id uuid references public.communities(id) on delete set null,
  name text not null,
  slug text not null,
  kind text not null default 'local' check (kind in ('local','regional','online','special_interest')),
  description text,
  is_public boolean not null default true,
  created_at timestamptz not null default now(),
  unique (organization_id, slug)
);

create table public.community_memberships (
  community_id uuid not null references public.communities(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  status text not null default 'active' check (status in ('active','inactive')),
  joined_at timestamptz not null default now(),
  primary key (community_id, user_id)
);

create table public.events (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  community_id uuid references public.communities(id) on delete set null,
  title text not null,
  slug text not null,
  description text,
  kind text not null default 'event',
  starts_at timestamptz not null,
  ends_at timestamptz,
  timezone text not null default 'America/New_York',
  venue_name text,
  address_text text,
  online_url text,
  capacity integer check (capacity is null or capacity > 0),
  visibility text not null default 'public' check (visibility in ('public','members','staff')),
  status text not null default 'scheduled' check (status in ('draft','scheduled','cancelled','completed')),
  created_at timestamptz not null default now(),
  unique (organization_id, slug)
);

create table public.event_registrations (
  id uuid primary key default gen_random_uuid(),
  event_id uuid not null references public.events(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  status text not null default 'registered' check (status in ('registered','waitlisted','cancelled','attended','no_show')),
  registered_at timestamptz not null default now(),
  unique (event_id, user_id)
);

create table public.groups (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  community_id uuid references public.communities(id) on delete set null,
  name text not null,
  slug text not null,
  kind text not null default 'group',
  description text,
  visibility text not null default 'public' check (visibility in ('public','members','private')),
  created_at timestamptz not null default now(),
  unique (organization_id, slug)
);

create table public.group_memberships (
  group_id uuid not null references public.groups(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  membership_role text not null default 'member' check (membership_role in ('member','facilitator','leader')),
  status text not null default 'active' check (status in ('requested','active','inactive')),
  joined_at timestamptz not null default now(),
  primary key (group_id, user_id)
);

create table public.content (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  content_type text not null check (content_type in ('page','article','teaching','practice','policy','course','resource')),
  slug text not null,
  title text not null,
  summary text,
  body jsonb not null default '{}'::jsonb,
  status text not null default 'draft' check (status in ('draft','review','approved','scheduled','published','archived')),
  visibility text not null default 'public' check (visibility in ('public','members','staff')),
  published_at timestamptz,
  author_user_id uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (organization_id, slug)
);

create table public.research_sources (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  title text not null,
  citation text,
  source_type text not null default 'text',
  date_from date,
  date_to date,
  language text,
  url text,
  notes text,
  visibility text not null default 'public' check (visibility in ('public','members','researchers')),
  created_at timestamptz not null default now()
);

create table public.research_encounters (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  title text not null,
  encounter_type text not null,
  claimant_name text,
  occurred_from date,
  occurred_to date,
  location_text text,
  summary text,
  confidence_note text,
  visibility text not null default 'public' check (visibility in ('public','members','researchers')),
  created_at timestamptz not null default now()
);

create table public.research_encounter_sources (
  encounter_id uuid not null references public.research_encounters(id) on delete cascade,
  source_id uuid not null references public.research_sources(id) on delete cascade,
  relationship text not null default 'attests',
  primary key (encounter_id, source_id)
);

create table public.funds (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  name text not null,
  slug text not null,
  description text,
  is_active boolean not null default true,
  is_public boolean not null default true,
  unique (organization_id, slug)
);

create table public.donations (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references public.organizations(id) on delete cascade,
  donor_user_id uuid references auth.users(id) on delete set null,
  fund_id uuid references public.funds(id) on delete set null,
  provider text,
  provider_payment_id text unique,
  amount_cents integer not null check (amount_cents > 0),
  currency text not null default 'USD',
  status text not null default 'pending' check (status in ('pending','succeeded','failed','refunded','partially_refunded')),
  donated_at timestamptz,
  created_at timestamptz not null default now()
);

create table private.audit_events (
  id bigint generated always as identity primary key,
  organization_id uuid,
  actor_user_id uuid,
  action text not null,
  resource_type text not null,
  resource_id text,
  metadata jsonb not null default '{}'::jsonb,
  occurred_at timestamptz not null default now()
);

create table private.cases (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null,
  case_type text not null,
  status text not null default 'open',
  summary text,
  opened_by_user_id uuid,
  assigned_user_id uuid,
  opened_at timestamptz not null default now(),
  closed_at timestamptz
);

-- User profile provisioning lives in a non-exposed schema and cannot be called by clients.
create or replace function private.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public, auth, private
as $$
begin
  insert into public.profiles (user_id, display_name)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'display_name', split_part(new.email, '@', 1)))
  on conflict (user_id) do nothing;
  return new;
end;
$$;
revoke all on function private.handle_new_user() from public, anon, authenticated;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
after insert on auth.users
for each row execute procedure private.handle_new_user();

-- RLS
alter table public.profiles enable row level security;
alter table public.organizations enable row level security;
alter table public.organization_memberships enable row level security;
alter table public.roles enable row level security;
alter table public.capabilities enable row level security;
alter table public.role_capabilities enable row level security;
alter table public.member_roles enable row level security;
alter table public.communities enable row level security;
alter table public.community_memberships enable row level security;
alter table public.events enable row level security;
alter table public.event_registrations enable row level security;
alter table public.groups enable row level security;
alter table public.group_memberships enable row level security;
alter table public.content enable row level security;
alter table public.research_sources enable row level security;
alter table public.research_encounters enable row level security;
alter table public.research_encounter_sources enable row level security;
alter table public.funds enable row level security;
alter table public.donations enable row level security;

create policy "profiles_read_self" on public.profiles for select to authenticated using ((select auth.uid()) = user_id);
create policy "profiles_update_self" on public.profiles for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);

create policy "organizations_public_read" on public.organizations for select to anon, authenticated using (status = 'active');
create policy "memberships_read_self" on public.organization_memberships for select to authenticated using ((select auth.uid()) = user_id);

create policy "communities_public_read" on public.communities for select to anon, authenticated using (is_public = true);
create policy "community_memberships_read_self" on public.community_memberships for select to authenticated using ((select auth.uid()) = user_id);

create policy "events_public_read" on public.events for select to anon, authenticated using (visibility = 'public' and status <> 'draft');
create policy "registrations_read_self" on public.event_registrations for select to authenticated using ((select auth.uid()) = user_id);
create policy "registrations_insert_self" on public.event_registrations for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "registrations_update_self" on public.event_registrations for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "registrations_delete_self" on public.event_registrations for delete to authenticated using ((select auth.uid()) = user_id);

create policy "groups_public_read" on public.groups for select to anon, authenticated using (visibility = 'public');
create policy "group_memberships_read_self" on public.group_memberships for select to authenticated using ((select auth.uid()) = user_id);
create policy "group_memberships_insert_self" on public.group_memberships for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "group_memberships_update_self" on public.group_memberships for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);

create policy "content_public_read" on public.content for select to anon, authenticated using (status = 'published' and visibility = 'public');
create policy "sources_public_read" on public.research_sources for select to anon, authenticated using (visibility = 'public');
create policy "encounters_public_read" on public.research_encounters for select to anon, authenticated using (visibility = 'public');
create policy "encounter_sources_public_read" on public.research_encounter_sources for select to anon, authenticated using (
  exists (select 1 from public.research_encounters e where e.id = encounter_id and e.visibility = 'public')
  and exists (select 1 from public.research_sources s where s.id = source_id and s.visibility = 'public')
);
create policy "funds_public_read" on public.funds for select to anon, authenticated using (is_active = true and is_public = true);
create policy "donations_read_self" on public.donations for select to authenticated using ((select auth.uid()) = donor_user_id);

-- Client API grants. RLS remains the authorization boundary.
grant usage on schema public to anon, authenticated;
grant select on public.organizations, public.communities, public.events, public.groups, public.content,
  public.research_sources, public.research_encounters, public.research_encounter_sources, public.funds to anon;
grant select on public.profiles, public.organizations, public.organization_memberships, public.communities,
  public.community_memberships, public.events, public.event_registrations, public.groups, public.group_memberships,
  public.content, public.research_sources, public.research_encounters, public.research_encounter_sources,
  public.funds, public.donations to authenticated;
grant update on public.profiles to authenticated;
grant insert, update, delete on public.event_registrations to authenticated;
grant insert, update on public.group_memberships to authenticated;

-- Seed capabilities; role assignments remain organization-specific.
insert into public.capabilities (key, description) values
  ('people.read', 'View permitted people records'),
  ('people.manage', 'Manage permitted people records'),
  ('events.manage', 'Create and manage events'),
  ('groups.manage', 'Create and manage groups'),
  ('content.write', 'Create and edit content'),
  ('content.publish', 'Approve and publish content'),
  ('research.write', 'Create and edit research records'),
  ('giving.read', 'View permitted giving records'),
  ('governance.manage', 'Manage governance records'),
  ('admin.access', 'Access administrative configuration')
on conflict (key) do nothing;
