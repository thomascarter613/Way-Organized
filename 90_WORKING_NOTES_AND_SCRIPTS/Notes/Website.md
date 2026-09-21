We do however need a website, not just a brochure site, a functional site that people, admins, staff, donors, etc. can and will actually use. It should be fully featured

---

Yes. What we need is not really a “church website.” We need a **digital institutional platform** whose public website is only its outermost layer.

I would design it so that someone can discover the community, create an account, attend gatherings, learn, donate, volunteer, participate in groups, access research, communicate with others, and eventually take organizational responsibilities—all without leaving the same system.

## The product

Internally, I would think of it as something like the **Community Platform** or **Digital Commons** until the religious vocabulary settles.

The fundamental model would be:

**Public Web → Identity → Community → Participation → Giving → Learning → Research → Service → Governance → Administration**

One person can occupy several roles simultaneously. Someone might be a participant, recurring donor, volunteer, research contributor, and group leader, for example. We should therefore assign **capabilities to people**, rather than creating completely separate classes of accounts.

### Major product areas

| Area              | Capabilities                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Public website    | Mission, beliefs/worldview, practices, history, research, locations, gatherings, events, articles, teachings, media, FAQs, contact |
| Accounts          | Registration, login, MFA, profile, privacy preferences, notification preferences, account recovery                                 |
| Community         | Member directory where opted in, profiles, households, local communities, groups, discussion, announcements                        |
| Gatherings        | Locations, recurring assemblies, calendars, registration, RSVP, check-in, attendance                                               |
| Events            | Public/private events, tickets where appropriate, capacity, waitlists, reminders, calendars                                        |
| Giving            | One-time gifts, recurring giving, funds, campaigns, pledges, donor dashboard, receipts, statements                                 |
| Groups            | Study groups, local circles, committees, teams, online groups, leaders, membership, schedules                                      |
| Learning          | Courses, reading programs, study guides, classes, cohorts, progress tracking                                                       |
| Research          | HTERP materials, sources, traditions, encounters, bibliography, annotations, claims, evidence                                      |
| Library           | Books, articles, documents, recordings, videos, manuscripts, collections, searchable catalog                                       |
| Practice          | Practices, guided material, calendars, personal programs, journals where appropriate                                               |
| Volunteer         | Opportunities, applications, skills, scheduling, teams, service hours                                                              |
| Community support | Requests for assistance, mutual aid, referrals, resource coordination                                                              |
| Communications    | Email, SMS if enabled, in-app notifications, newsletters, audience segmentation                                                    |
| Staff CRM         | People, interactions, follow-ups, visitors, participation history, notes with strict permissions                                   |
| Governance        | Governing documents, policies, board/leadership information, resolutions, meeting records                                          |
| Transparency      | Financial summaries, annual reports, policies, safeguarding, complaints procedures                                                 |
| Staff operations  | Internal dashboard, work queues, events, publishing, communications, volunteer coordination                                        |
| Finance           | Donation reconciliation, funds, campaigns, donor records, receipts, exports, reporting                                             |
| Admin             | Users, permissions, roles, locations, settings, integrations, audit logs                                                           |
| Safeguarding      | Restricted incident/reporting workflows, escalation, case access controls, retention                                               |
| Developer/system  | Audit logs, feature flags, jobs, webhooks, integrations, observability                                                             |

The important point is that these are **modules of one platform**, not seventeen unrelated products.

## The account experience

After signing in, a normal participant might see:

**Home**
Personalized upcoming gatherings, announcements, courses, group activity and volunteer commitments.

**Explore**
Teachings, research, practices, library and community resources.

**Community**
Groups, people, local community and conversations.

**Calendar**
Assemblies, events, courses and volunteer commitments.

**Learn**
Courses, reading programs, study material and progress.

**Serve**
Volunteer opportunities and assignments.

**Give**
Donation history, recurring contributions, receipts and supported funds.

**Profile**
Personal information, household, privacy and communication preferences.

Staff would see additional sections. Finance staff would see finance capabilities. Researchers would see research-authoring capabilities. Administrators would see system administration.

No need for four different logins.

---

# Public website

The public side still needs to be excellent.

I would eventually expect an information architecture approximately like:

`/`
`/about`
`/our-way`
`/beliefs`
`/practice`
`/traditions`
`/research`
`/library`
`/teachings`
`/gatherings`
`/locations`
`/events`
`/learn`
`/community`
`/serve`
`/give`
`/governance`
`/transparency`
`/safeguarding`
`/faq`
`/contact`

The language can change as our terminology emerges.

The website should also have excellent global search. Someone should eventually be able to search something such as **“Melchizedek”** and get relevant research records, articles, source texts, teachings, library materials and discussions rather than just ordinary webpage matches.

---

# Research should be a first-class feature

This is one place where our platform can become very different from conventional religious websites.

HTERP shouldn't eventually live as a pile of PDFs.

We should be able to represent relationships like:

**Encounter → claimant/witness → date → location → testimony → source → manuscript/document → interpretation → tradition → scholarly assessment → evidence**

For example, a record could eventually represent:

**Moses → burning bush → Exodus tradition → textual witnesses → historical context → interpretations → related encounter motifs → bibliography**

Users could explore this as ordinary readable content while researchers work with the underlying structured information.

That could eventually become one of the site's defining capabilities.

---

# Governance should also be first-class

Because of the kind of institution we're designing, I would make governance unusually visible.

There should eventually be a **Transparency Center** containing things like governing documents, leadership structure, financial disclosures, conflict-of-interest policy, safeguarding policy, grievance procedure, leadership-removal procedure, doctrinal/change procedures, whistleblower channels and institutional safeguards.

Some records would obviously remain confidential, but the architecture of authority should not be mysterious.

That supports the anti-coercion principles we've already been discussing.

---

# Giving system

I would build giving directly into the platform but use **Stripe as the payment processor**, rather than trying to handle payment-card data ourselves.

Stripe currently supports both one-time and recurring nonprofit donations, including donor-controlled amounts and recurring contributions. ([Stripe][1])

Our own database would retain the institutional record:

`donor`
`gift`
`transaction`
`fund`
`campaign`
`designation`
`pledge`
`recurring_plan`
`receipt`
`statement`
`refund`

Stripe remains the payment processor; **our system remains the donor system of record**.

This matters because eventually we may accept other forms of giving or change processors without losing institutional history.

It also allows a donor portal such as:

> 2026 giving: $1,240
> Monthly contribution: $100
> General Fund: $800
> Community Assistance: $240
> Research Project: $200
> Download annual statement
> Manage recurring gift

Whether a particular contribution is described as tax-deductible would be determined by the legal/tax status and applicable rules, not assumed by the software.

---

# Community structure

The architecture should support more than one physical congregation from the beginning.

I would use something like:

```text
Organization
 ├── Region
 │    ├── Local Community
 │    │    ├── Gathering
 │    │    ├── Group
 │    │    ├── Volunteer Team
 │    │    └── Members
 │    └── Local Community
 └── Online Community
```

That way we're not rebuilding everything if this eventually becomes more than one local gathering.

A gathering could be physical, online or hybrid.

---

# Permission architecture

This part needs to be taken very seriously.

A simplistic:

`admin = true`

would be a terrible design.

We want combinations of **role-based and resource-based authorization**.

For example:

| Person               | Can do                                   |
| -------------------- | ---------------------------------------- |
| Participant          | Manage own profile                       |
| Donor                | See own donation history                 |
| Group leader         | Manage assigned group                    |
| Editor               | Draft content                            |
| Publisher            | Approve/publish content                  |
| Local leader         | Manage assigned community                |
| Staff                | Access assigned organizational functions |
| Finance              | Access financial records                 |
| Researcher           | Edit research records                    |
| Safeguarding officer | Access assigned safeguarding records     |
| Governance officer   | Manage governance records                |
| Administrator        | Configure system                         |
| System administrator | Technical operations                     |

Even administrators should not automatically receive unrestricted access to highly sensitive case information.

Supabase is particularly useful here because authentication can integrate directly with PostgreSQL Row Level Security. Supabase explicitly recommends RLS for exposed data and warns that merely identifying someone as `authenticated` is **not** sufficient authorization; ownership/resource predicates still need to be enforced. ([Supabase][2])

That maps extremely well to what we're building.

---

# Data sensitivity

This system deserves a higher privacy bar than an ordinary SaaS application.

A person's participation in a religious organization can itself reveal sensitive information. Then we potentially add household information, donations, private messages, pastoral/community-support information and information about children.

So I would architect around:

**data minimization**, **least privilege**, **explicit consent**, **segregated sensitive records**, **audit logging**, **exportability**, **retention policies**, **account deletion workflows**, and **administrator-access auditing**.

Supabase specifically warns against putting authorization decisions in user-editable metadata and recommends protecting every exposed table through appropriate grants plus RLS. ([Supabase][3])

For especially sensitive data, I would probably use private database schemas and server-only access rather than exposing those tables through the normal client Data API at all.

---

# Children and families

If children participate, I would make this a deliberate subsystem rather than treating children as ordinary user accounts.

A household could contain adults and dependents.

Minors would have carefully restricted profiles. Child check-in/out could eventually use authorized guardians. Direct adult-to-minor messaging should have strong restrictions. Volunteer eligibility/background-screening status can be tracked without unnecessarily storing the underlying sensitive report.

This is one of those features that should be designed correctly before it is needed.

---

# Content management

I would **not** initially bolt a completely separate WordPress-style CMS onto the system.

Content should be another native domain:

```text
Content
 ├── Pages
 ├── Articles
 ├── Teachings
 ├── Practices
 ├── Research
 ├── Courses
 ├── Policies
 └── Media
```

Each item gets:

draft → review → approved → scheduled → published → archived

with version history and attribution.

Staff members receive editorial capabilities through the same account they use for everything else.

That gives us a real institutional publishing platform rather than a separate CMS bolted onto an application.

---

# Technical architecture

I would keep the architecture surprisingly simple at first: a **modular monolith**, not microservices.

```text
Browser / PWA
      │
      ▼
Next.js Application
      │
      ├── Public Web
      ├── Member App
      ├── Staff App
      └── Admin App
      │
      ▼
Application Services
      │
      ├── Identity
      ├── Community
      ├── Content
      ├── Events
      ├── Groups
      ├── Giving
      ├── Learning
      ├── Research
      ├── Communications
      ├── Governance
      └── Administration
      │
      ▼
Supabase / PostgreSQL
```

I would use **Next.js 16 Active LTS**, App Router, React and TypeScript. Next.js 16.x is currently the Active LTS line; the August 2026 security release specifically required upgrading to at least 16.3.3 for two critical fixes. ([Next.js][4])

For production I would keep us on the latest patched Active-LTS release rather than pinning ourselves permanently to 16.3.3.

Infrastructure would look roughly like:

| Function                | Technology                                     |
| ----------------------- | ---------------------------------------------- |
| Web/application         | Next.js                                        |
| Language                | TypeScript                                     |
| Runtime/package tooling | Bun                                            |
| Database                | PostgreSQL                                     |
| Backend platform        | Supabase                                       |
| Authentication          | Supabase Auth                                  |
| Authorization           | PostgreSQL RLS + application capabilities      |
| Files/media             | Supabase Storage                               |
| Realtime                | Supabase Realtime where actually useful        |
| Payments                | Stripe                                         |
| Rich text               | Tiptap-style structured editor                 |
| Search                  | PostgreSQL full-text initially                 |
| Email                   | Transactional email provider                   |
| SMS                     | Optional communications provider               |
| Hosting                 | Vercel initially                               |
| Monitoring              | Application/error monitoring + database health |
| Tests                   | unit + integration + Playwright E2E            |
| Deployment              | preview → staging → production                 |

Vercel provides first-class Next.js deployment support, including its rendering/caching model. ([Vercel][5])

Supabase gives us Postgres, Auth, Storage, Realtime and server-side capabilities while remaining fundamentally PostgreSQL-based rather than locking our data into some proprietary document model. ([Supabase][6])

That combination fits this application unusually well.

---

# Route architecture

Behind the public site I would separate the authenticated interfaces cleanly:

```text
/app
    /home
    /calendar
    /community
    /groups
    /learn
    /research
    /library
    /serve
    /giving
    /notifications
    /profile
    /settings

/staff
    /dashboard
    /people
    /communities
    /events
    /groups
    /volunteers
    /communications
    /content
    /research
    /governance
    /giving
    /reports

/admin
    /organization
    /users
    /roles
    /permissions
    /locations
    /integrations
    /audit
    /security
    /settings
```

Same application. Same identity. Different permissions.

---

# The database becomes the real backbone

Eventually I expect the major domain model to contain entities such as:

```text
Person
User
Profile
Household
Organization
Community
Location
Membership
Role
Capability
Group
GroupMembership
Gathering
Event
Registration
Attendance
VolunteerRole
VolunteerAssignment
Content
Publication
Media
Course
Enrollment
ResearchRecord
Source
Encounter
Claim
Evidence
Annotation
Donation
Fund
Campaign
Pledge
Transaction
Receipt
Communication
Notification
GovernanceDocument
Policy
Resolution
Case
AuditEvent
```

That means the architecture is already capable of growing into something far larger than a small congregation website.

---

# How I would build it

I would not try to implement all of those modules simultaneously. I would build the **complete architecture incrementally**:

1. **Foundation** — repository, design system, database, authentication, permissions, organization model, audit system and deployment pipeline.
2. **Public + identity** — public site, CMS, accounts, profiles, search and media.
3. **Participation** — communities, gatherings, events, groups, calendars, registrations and attendance.
4. **Giving + communications** — donations, funds, recurring gifts, donor portal, email, notifications and segmentation.
5. **Community application** — member dashboard, learning, volunteering, directory, household management and notifications.
6. **Institutional operations** — staff CRM, publishing workflow, finance, reporting, governance, transparency, safeguarding and administration.
7. **Research platform** — HTERP data model, structured sources, encounter records, claims/evidence, annotations, bibliography and public research explorer.
8. **Maturity** — accessibility audit, security audit, privacy tooling, data retention, backups, disaster recovery, performance work, multilingual support and PWA/mobile capabilities.

The distinction is important: **we architect for the whole system now while shipping it vertically in usable increments**.

That prevents us from producing a gigantic half-working application, while also preventing the early “website” from becoming technical debt that has to be thrown away.

## What I think we are actually building

At maturity, this becomes something considerably more interesting than a religious organization's website:

> **a digital operating system for the religious community.**

The public site is its front door.

The member application is its community space.

The staff application runs the institution.

The giving system sustains it.

The research system preserves and investigates its intellectual foundations.

The governance system makes its authority visible and accountable.

And all of them share **one identity system, one organizational model, one permission model and one coherent body of data**.

That is the architecture I would commit to.

[1]: https://stripe.com/resources/more/how-to-handle-recurring-donations-in-nonprofit-payments?utm_source=chatgpt.com "Nonprofit payments: How to handle recurring donations | Stripe"
[2]: https://supabase.com/docs/guides/auth?utm_source=chatgpt.com "Auth | Supabase Docs"
[3]: https://supabase.com/docs/guides/database/postgres/row-level-security?utm_source=chatgpt.com "Row Level Security | Supabase Docs"
[4]: https://nextjs.org/blog?utm_source=chatgpt.com "Next.js by Vercel - The React Framework | Next.js by Vercel - The React Framework"
[5]: https://vercel.com/frameworks/nextjs?utm_source=chatgpt.com "Next.js on Vercel"
[6]: https://supabase.com/docs/guides/database/overview?utm_source=chatgpt.com "Database | Supabase Docs"

