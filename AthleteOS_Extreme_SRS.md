# AthleteOS — Master Software Requirements Specification (SRS)

**Document Version:** 1.0  
**Status:** Development Blueprint  
**Primary Audience:** GitHub Copilot, AI coding agents, software developers, product designers, QA engineers, technical founders  
**Initial Sport:** Baseball  
**Primary Product Type:** Mobile-first remote athlete development, recruiting, performance testing, video coaching, and coach monetization platform  
**Recommended Initial Stack:** Python, FastAPI, PostgreSQL, React, TypeScript, Supabase, Stripe, S3-compatible storage, OpenAI API  
**Repository Name:** `athleteos-platform`

---

# 0. Instructions for AI Coding Agents

This document is the authoritative source of truth for the AthleteOS project.

Any AI coding assistant working on this repository must follow these rules:

1. Read this document before generating architecture, database migrations, API routes, UI components, tests, or deployment files.
2. Do not invent features that conflict with this specification.
3. Build the platform incrementally according to the implementation phases.
4. Preserve role-based permissions at every layer:
   - UI
   - API
   - database
   - storage
5. Every major feature must include:
   - database schema
   - backend service
   - API endpoint
   - frontend UI
   - validation
   - authorization
   - error handling
   - tests
6. Do not hard-code user IDs, organization IDs, pricing, plan limits, email addresses, URLs, API keys, or secrets.
7. Every tenant-owned database record must include an `organization_id`.
8. Every auditable record must include:
   - `created_at`
   - `updated_at`
   - `created_by`
9. Use UUIDs for primary keys.
10. All timestamps must be stored in UTC.
11. User-facing dates must be displayed in the user’s configured timezone.
12. Use soft deletion where specified.
13. Never expose private athlete, parent, medical, payment, or recruiting information to unauthorized users.
14. AI outputs must be treated as suggestions until approved by a coach.
15. No AI recommendation may be represented as medical advice.
16. Every generated workout, analysis, or recruiting recommendation must maintain an audit trail.
17. Build the MVP before advanced AI, computer vision, marketplace, or multi-sport expansion.
18. Prefer readable, modular, testable code over clever abstractions.
19. Generate documentation for every public API and major service.
20. Do not mark a feature complete until acceptance criteria and tests pass.

---

# 1. Product Overview

## 1.1 Product Name

Working product name: **AthleteOS**

The name may be changed later. The codebase should avoid embedding the brand name in business logic.

## 1.2 Product Vision

AthleteOS is a platform that enables coaches to remotely manage, train, evaluate, communicate with, and support athletes while monetizing services that are frequently performed manually or for free.

The platform centralizes:

- athlete profiles
- performance testing
- ArmCare data
- strength data
- throwing programs
- workout assignments
- drill libraries
- athlete video uploads
- coach video feedback
- recruiting workflows
- college contact tracking
- offers and commitments
- messaging
- subscriptions
- invoices
- progress reports
- AI-assisted programming
- AI-assisted recruiting communication
- organization operations

The first implementation must focus on baseball athletes and baseball development professionals.

## 1.3 Core Problem

Many private coaches, trainers, recruiters, and baseball development professionals provide significant unpaid support outside scheduled training sessions.

Typical unpaid activities include:

- reviewing video
- answering athlete questions
- writing workouts
- adjusting throwing programs
- interpreting testing data
- communicating with parents
- assisting with recruiting
- building player profiles
- contacting colleges
- tracking offers
- preparing athletes for showcases
- helping athletes transition to college
- monitoring athlete progress remotely

These activities are spread across text messages, spreadsheets, email, notes, social media, cloud drives, and memory.

AthleteOS must convert these fragmented activities into structured, trackable, billable services.

## 1.4 Primary Business Objective

Allow a coach to turn expertise and athlete support into recurring revenue without reducing coaching quality.

## 1.5 Secondary Business Objectives

- Help coaches serve more athletes remotely.
- Improve athlete accountability.
- Improve parent visibility.
- Create a structured recruiting process.
- Preserve athlete history and development data.
- Reduce administrative work.
- Generate measurable athlete progress reports.
- Establish clear service tiers.
- Support future expansion to teams and organizations.

---

# 2. Scope

## 2.1 MVP Scope

The MVP must include:

1. Authentication
2. Organization setup
3. Coach dashboard
4. Athlete onboarding
5. Athlete profiles
6. Parent linkage
7. Workout templates
8. Workout assignment
9. Workout completion tracking
10. Throwing program assignment
11. Testing data entry
12. ArmCare testing entry
13. Progress charts
14. Video upload
15. Coach feedback
16. Recruiting CRM
17. Messaging
18. Subscription plans
19. Stripe checkout
20. Billing status
21. Notifications
22. Progress reports
23. Basic AI workout drafting
24. Basic AI recruiting message drafting
25. Audit logging
26. Admin panel
27. Mobile-responsive web interface

## 2.2 Explicitly Out of Scope for MVP

The MVP must not require:

- native iOS application
- native Android application
- automated biomechanics diagnosis
- medical diagnosis
- automated injury prediction
- automated college coach outreach
- wearable integrations
- marketplace payments to multiple independent coaches
- live video calling
- full social network
- public athlete rankings
- verified college coach portal
- advanced computer vision
- multi-language support
- multi-sport support
- white-label franchise deployment
- NCAA compliance certification
- HIPAA certification

These may be added after the MVP.

---

# 3. Users and Roles

## 3.1 Platform Super Admin

A platform super admin manages the entire SaaS platform.

Permissions:

- view all organizations
- suspend organizations
- manage platform-wide feature flags
- view platform health
- manage support cases
- view subscription status
- impersonate users only through a logged and audited support process
- manage global content templates
- view aggregate analytics
- manage system configuration

A super admin must not casually access athlete private data.

## 3.2 Organization Owner

The organization owner is the primary business account holder.

Permissions:

- configure organization
- invite staff
- assign roles
- manage plans
- manage pricing
- manage branding
- manage billing
- manage athletes
- manage parent access
- view all organization data
- manage organization settings
- export organization data
- manage integrations

## 3.3 Head Coach / Director

Permissions:

- manage athletes
- assign staff
- view all athlete data
- create programs
- approve AI outputs
- view recruiting data
- review videos
- message athletes and parents
- run reports
- manage testing
- view organization-level analytics

## 3.4 Coach / Trainer

Permissions depend on athlete assignment.

A coach can:

- view assigned athletes
- assign workouts
- review videos
- enter testing data
- leave notes
- send messages
- update recruiting tasks if permission is granted
- create personal templates
- view permitted progress data

A coach cannot:

- manage organization billing
- manage unrelated athletes
- change platform-level configuration
- view private parent billing details unless explicitly authorized

## 3.5 Recruiting Advisor

A recruiting advisor can:

- view assigned athlete recruiting profiles
- manage school targets
- log coach contacts
- update recruiting pipeline
- draft recruiting emails
- track visits
- track offers
- create recruiting tasks
- update commitment status

## 3.6 Athlete

An athlete can:

- view assigned workouts
- view throwing program
- mark activities complete
- submit results
- upload video
- view coach feedback
- message assigned staff
- view progress
- maintain allowed profile fields
- view recruiting tasks
- approve public recruiting profile
- manage notification preferences

An athlete cannot:

- view other athletes
- edit coach-entered test results unless permitted
- see internal coach-only notes
- edit billing
- contact unrelated users

## 3.7 Parent / Guardian

A parent can:

- view linked athlete summary
- view progress reports
- view schedules
- view billing
- manage payment method
- communicate with staff
- view recruiting milestones
- receive notifications

Parent visibility must be configurable for adult athletes.

## 3.8 Organization Administrator

An organization administrator can:

- invite users
- manage account access
- assign roles
- manage basic organization settings
- view billing if granted
- help maintain records

---

# 4. Multi-Tenant Architecture

The application must be multi-tenant.

Each customer business is an organization.

Every organization-owned table must contain:

```sql
organization_id UUID NOT NULL
```

All queries must be scoped by organization.

The backend must never rely solely on a client-provided organization ID. The authenticated user’s membership must be validated.

## 4.1 Tenant Isolation Rules

- Users may belong to multiple organizations.
- Users must select an active organization.
- Every API request using organization data must validate membership.
- Role checks must occur server-side.
- Storage paths must include organization ID.
- Background jobs must include organization context.
- Audit logs must include organization ID.
- Database row-level security may be used in addition to backend authorization.

---

# 5. Functional Modules

# 5.1 Authentication and Account Management

## 5.1.1 Required Features

- email/password signup
- email verification
- login
- logout
- forgot password
- reset password
- session refresh
- optional Google login
- optional Apple login later
- MFA for organization owners and admins
- user profile
- timezone
- notification preferences
- terms acceptance
- privacy policy acceptance

## 5.1.2 Account States

- invited
- active
- suspended
- deactivated
- pending_verification
- locked

## 5.1.3 Acceptance Criteria

- Users cannot access private routes without authentication.
- Suspended users cannot log in.
- Invitations expire.
- Password reset tokens expire.
- Role permissions are verified by the backend.
- Login failures do not reveal whether an account exists.

---

# 5.2 Organization Setup

## 5.2.1 Organization Fields

- organization name
- legal business name
- slug
- logo
- primary color
- secondary color
- website
- support email
- support phone
- address
- timezone
- currency
- tax settings
- default waiver
- default privacy consent
- default athlete agreement
- active status

## 5.2.2 Onboarding Flow

1. Create account.
2. Verify email.
3. Create organization.
4. Select business type.
5. Enter basic business details.
6. Choose subscription plan.
7. Configure services.
8. Invite staff.
9. Add first athlete.
10. Complete onboarding checklist.

---

# 5.3 Coach Dashboard

## 5.3.1 Dashboard Purpose

The coach dashboard is the primary workspace.

## 5.3.2 Dashboard Widgets

- active athletes
- athletes requiring review
- incomplete workouts
- videos awaiting feedback
- unread messages
- expiring subscriptions
- upcoming tests
- recruiting tasks due
- recent athlete improvements
- workload alerts
- scheduled sessions
- monthly recurring revenue
- overdue invoices
- recent activity

## 5.3.3 Required Filters

- date range
- coach
- athlete
- team
- service plan
- graduation year
- position
- recruiting status

## 5.3.4 Dashboard Actions

- add athlete
- assign workout
- create program
- enter test result
- review video
- send message
- create recruiting task
- create report

---

# 5.4 Athlete Management

## 5.4.1 Athlete Profile Fields

### Identity

- first name
- preferred name
- middle name
- last name
- profile image
- date of birth
- gender
- email
- phone
- address
- timezone

### Baseball Information

- primary position
- secondary positions
- bats
- throws
- team
- school
- graduation year
- jersey number
- level
- height
- weight

### Recruiting Information

- NCAA ID
- GPA
- weighted GPA
- class rank
- SAT
- ACT
- intended major
- geographic preferences
- school size preferences
- division preferences
- scholarship preferences
- recruiting status
- commitment status
- committed school
- signing date
- adviser notes

### Emergency and Guardian Information

- guardian names
- guardian emails
- guardian phones
- emergency contact
- emergency contact relationship

### Health and Readiness

Only collect what is necessary.

- participation restrictions
- coach-visible readiness notes
- waiver status
- injury disclosure acknowledgment
- physician clearance document
- emergency action notes

The platform must not represent itself as a medical record system.

## 5.4.2 Athlete Status

- prospect
- trial
- active
- paused
- alumni
- inactive
- archived

## 5.4.3 Athlete Tags

Examples:

- pitcher
- catcher
- high_school
- college
- draft_prospect
- remote
- in_person
- recruiting
- velocity_program
- armcare

Tags must be organization-configurable.

---

# 5.5 Parent and Guardian Management

- Link multiple guardians to an athlete.
- Allow one guardian to pay for multiple athletes.
- Allow configurable access.
- Allow guardian consent.
- Allow communication preferences.
- Log guardian changes.
- Do not expose athlete private messages unless policy permits.

---

# 5.6 Team and Group Management

The platform must allow athletes to be organized into:

- teams
- training groups
- cohorts
- graduation classes
- programs
- camps

A group may have:

- name
- description
- coach
- start date
- end date
- roster
- default program
- communication channel

---

# 5.7 Exercise and Drill Library

## 5.7.1 Exercise Fields

- title
- category
- sport
- skill area
- description
- instructions
- coaching cues
- common mistakes
- equipment
- difficulty
- duration type
- default sets
- default reps
- default distance
- default load
- video URL
- thumbnail
- progression
- regression
- contraindication note
- organization visibility
- created by
- active status

## 5.7.2 Categories

- warm-up
- mobility
- arm care
- throwing
- pitching
- hitting
- catching
- fielding
- speed
- agility
- strength
- power
- conditioning
- recovery
- mental performance
- recruiting task

---

# 5.8 Workout Template Builder

## 5.8.1 Template Structure

A workout template contains:

- name
- description
- objective
- target athlete type
- estimated duration
- difficulty
- sections
- exercises
- notes
- completion rules
- coach instructions
- athlete instructions

## 5.8.2 Section Examples

- readiness check
- warm-up
- movement prep
- arm care
- throwing
- strength
- conditioning
- recovery
- reflection

## 5.8.3 Exercise Prescription Fields

- exercise ID
- sets
- reps
- duration
- distance
- load
- intensity
- RPE
- tempo
- rest
- side
- coaching note
- required video
- required result
- completion criteria

---

# 5.9 Workout Assignment

A coach must be able to assign a workout to:

- one athlete
- multiple athletes
- a team
- a group

Assignment fields:

- assigned date
- due date
- start time
- athlete
- template
- customized exercises
- coach note
- status
- priority
- reminder settings

## 5.9.1 Workout Status

- scheduled
- available
- in_progress
- completed
- partially_completed
- skipped
- overdue
- cancelled
- reviewed

## 5.9.2 Athlete Completion Flow

1. Athlete opens assignment.
2. Athlete completes readiness check.
3. Athlete views exercise.
4. Athlete logs result.
5. Athlete optionally uploads video.
6. Athlete marks exercise complete.
7. Athlete submits workout.
8. Coach receives notification if review is required.
9. Coach reviews.
10. Coach approves or comments.

---

# 5.10 Throwing Program Module

Throwing programs must be a specialized program type.

## 5.10.1 Fields

- program name
- objective
- phase
- start date
- end date
- throwing days
- recovery days
- distance
- volume
- intensity
- mound work
- pulldown work
- long toss
- command work
- pitch count
- RPE target
- soreness rules
- progression criteria
- regression rules
- coach approval status

## 5.10.2 Required Safeguards

- no automatic medical diagnosis
- configurable workload limits
- coach approval before athlete assignment
- athlete soreness reporting
- warning when athlete reports pain
- escalation prompt to contact coach
- audit history of changes

---

# 5.11 Readiness and Recovery Check-In

Before selected workouts, the athlete may complete:

- sleep quality
- sleep hours
- soreness
- arm soreness
- energy
- stress
- motivation
- pain flag
- notes
- optional resting heart rate
- optional HRV

The system may calculate a readiness score.

The readiness score is informational and must not be presented as medical advice.

---

# 5.12 Testing and Assessments

## 5.12.1 Testing Categories

- velocity
- exit velocity
- launch angle
- bat speed
- rotational acceleration
- pop time
- catcher exchange
- 60-yard dash
- 10-yard split
- vertical jump
- broad jump
- med ball throw
- grip strength
- body weight
- body composition
- mobility
- range of motion
- strength
- power
- ArmCare
- custom assessment

## 5.12.2 Test Definition Fields

- name
- category
- unit
- lower is better or higher is better
- valid minimum
- valid maximum
- protocol
- equipment
- instructions
- organization-specific benchmark
- age benchmark
- position benchmark
- active status

## 5.12.3 Test Result Fields

- athlete
- test definition
- result
- unit
- date
- evaluator
- facility
- conditions
- source
- device
- video
- notes
- verified status

## 5.12.4 Progress Charts

The platform must support:

- line charts
- best result
- latest result
- percentage change
- date range comparison
- benchmark comparison
- position comparison
- age comparison
- testing session comparison

---

# 5.13 ArmCare Module

The ArmCare module must support manual entry first.

Potential future integrations may import data.

## 5.13.1 Data Fields

- arm strength metrics
- range of motion
- shoulder metrics
- fatigue score
- recovery score
- workload score
- date
- device source
- evaluator
- notes
- session type

## 5.13.2 Rules

- Store original values.
- Preserve units.
- Record source.
- Allow CSV import.
- Flag extreme changes.
- Require coach review for alerts.
- Do not diagnose injury.

---

# 5.14 Video Coaching

## 5.14.1 Upload Requirements

Athletes and coaches may upload:

- bullpen video
- hitting video
- fielding video
- catching video
- strength video
- mobility video
- recruiting highlight
- test video

## 5.14.2 Supported File Types

- MP4
- MOV
- WEBM

## 5.14.3 Video Metadata

- athlete
- category
- title
- description
- captured date
- uploaded date
- camera angle
- drill
- associated workout
- associated test
- duration
- file size
- processing status
- privacy status
- review status

## 5.14.4 Video Processing

- validate file type
- validate size
- upload directly to object storage
- generate secure URL
- generate thumbnail
- transcode if needed
- store duration
- support adaptive playback later

## 5.14.5 Coach Feedback

Feedback may include:

- text comment
- timestamped comment
- voice note
- drawing overlay later
- rating
- drill recommendation
- follow-up assignment
- review status

## 5.14.6 Video Review Status

- uploaded
- processing
- ready
- awaiting_review
- in_review
- feedback_sent
- revision_requested
- archived
- failed

---

# 5.15 Recruiting CRM

The recruiting CRM is a core differentiator.

## 5.15.1 Recruiting Pipeline Stages

- profile_building
- video_development
- target_school_research
- initial_outreach
- active_conversations
- evaluation
- camp_or_showcase
- visit_scheduled
- offer_received
- negotiation
- committed
- signed
- closed_no_offer

Organizations must be able to customize stages.

## 5.15.2 School Records

- school name
- city
- state
- conference
- division
- level
- website
- baseball website
- roster link
- recruiting questionnaire
- camp link
- academic notes
- size
- public/private
- target status

## 5.15.3 College Coach Contact Fields

- first name
- last name
- title
- school
- email
- phone
- social profile
- preferred contact method
- notes
- verified date
- data source

## 5.15.4 Athlete School Target Fields

- athlete
- school
- priority
- fit score
- athletic fit
- academic fit
- geographic fit
- financial fit
- interest level
- staff interest
- last contact
- next action
- pipeline stage
- notes

## 5.15.5 Recruiting Interaction Log

- athlete
- school
- coach contact
- interaction type
- direction
- date
- summary
- outcome
- follow-up date
- attachment
- created by

Interaction types:

- email
- call
- text
- direct message
- in-person
- camp
- showcase
- visit
- evaluation
- offer
- other

## 5.15.6 Offer Tracking

- school
- athlete
- offer type
- roster spot
- scholarship amount
- academic aid
- housing
- books
- conditions
- offer date
- expiration date
- status
- notes
- document

## 5.15.7 Commitment Tracking

- athlete
- school
- commitment date
- commitment type
- signing date
- scholarship amount
- announcement status
- verified status
- notes

## 5.15.8 Recruiting Tasks

Examples:

- update highlight video
- email coach
- complete questionnaire
- register for camp
- send transcript
- request recommendation
- schedule visit
- follow up
- update metrics
- post recruiting content

---

# 5.16 Public Recruiting Profile

An athlete may optionally publish a recruiting profile.

## 5.16.1 Public Fields

- athlete name
- graduation year
- position
- height
- weight
- bats
- throws
- school
- team
- GPA if athlete approves
- verified metrics
- highlight videos
- schedule
- coach contact
- social links
- commitment status

## 5.16.2 Privacy Rules

- disabled by default
- athlete approval required
- parent approval required for minors
- coach approval configurable
- private fields never exposed
- unique public slug
- ability to disable immediately
- view analytics

---

# 5.17 Messaging

## 5.17.1 Conversation Types

- direct message
- athlete-coach
- parent-coach
- group message
- team announcement
- support message

## 5.17.2 Features

- text
- attachments
- images
- links
- read receipts
- notifications
- conversation mute
- search
- message reporting
- retention policy

## 5.17.3 Safety

- communication involving minors must be organization-policy aware
- parent visibility options
- audit logs
- block inappropriate content
- report function
- no disappearing messages in MVP

---

# 5.18 Scheduling

## 5.18.1 Event Types

- training session
- remote consultation
- testing session
- video review
- recruiting call
- parent meeting
- camp
- showcase
- visit
- deadline

## 5.18.2 Fields

- title
- start
- end
- timezone
- location
- video link
- attendees
- coach
- athlete
- recurrence
- reminder
- status
- notes

Google Calendar integration may be added later.

---

# 5.19 Notifications

## 5.19.1 Channels

MVP:

- in-app
- email

Later:

- push
- SMS

## 5.19.2 Notification Events

- workout assigned
- workout due
- workout overdue
- workout submitted
- video uploaded
- feedback available
- message received
- test result added
- subscription payment failed
- invoice paid
- recruiting task due
- visit scheduled
- offer logged
- report available
- user invited

## 5.19.3 Preferences

Users may configure:

- channel
- event type
- quiet hours
- digest frequency
- timezone

---

# 5.20 Billing and Monetization

Stripe is the recommended payment provider.

## 5.20.1 Product Types

- monthly subscription
- annual subscription
- one-time video review
- testing package
- recruiting package
- consultation
- camp registration
- custom service

## 5.20.2 Example Service Plans

### Program Only

- workout access
- throwing program
- progress tracking
- limited messaging

### Remote Coaching

- program access
- weekly adjustments
- messaging
- monthly video reviews

### Premium Development

- full programming
- weekly video review
- testing dashboard
- recruiting support
- monthly consultation

### Recruiting Advisory

- recruiting profile
- target school list
- outreach planning
- communication templates
- offer tracking
- commitment support

## 5.20.3 Billing Records

- customer
- Stripe customer ID
- subscription
- plan
- status
- amount
- currency
- billing interval
- next billing date
- cancellation date
- trial end
- invoice history
- payment method summary

## 5.20.4 Subscription Status

- trialing
- active
- past_due
- unpaid
- paused
- cancelled
- expired

## 5.20.5 Required Stripe Webhooks

- checkout.session.completed
- customer.subscription.created
- customer.subscription.updated
- customer.subscription.deleted
- invoice.paid
- invoice.payment_failed
- charge.refunded

All webhook events must be verified and idempotent.

---

# 5.21 Reports

## 5.21.1 Athlete Progress Report

Sections:

- athlete summary
- reporting period
- attendance
- workout completion
- readiness trends
- testing improvements
- ArmCare trends
- coach notes
- video feedback summary
- recruiting progress
- upcoming goals
- action items

## 5.21.2 Recruiting Report

- target schools
- current stage
- communication activity
- upcoming camps
- offers
- next actions
- profile completeness
- testing gaps

## 5.21.3 Business Report

- active athletes
- new athletes
- churn
- MRR
- failed payments
- service utilization
- video review turnaround
- coach workload
- athlete engagement

Reports must support PDF export later. MVP may first support printable HTML.

---

# 5.22 AI Assistant

AI must assist coaches, not replace them.

## 5.22.1 AI Features in MVP

- draft workout
- draft throwing session
- summarize athlete progress
- draft coach feedback
- draft recruiting email
- summarize recruiting history
- suggest follow-up tasks
- convert notes into structured records

## 5.22.2 AI Approval Workflow

1. User requests AI output.
2. Backend gathers permitted context.
3. Prompt is generated.
4. AI response is stored as draft.
5. Coach reviews.
6. Coach edits.
7. Coach approves.
8. Approved content is assigned or sent.
9. Audit log records all steps.

## 5.22.3 AI Guardrails

- Never diagnose an injury.
- Never state certainty about injury risk.
- Never send messages automatically in MVP.
- Never publish public profile content automatically.
- Never modify billing.
- Never contact colleges automatically.
- Never expose another athlete’s data.
- Do not use private data beyond the authorized organization context.
- Clearly label AI-generated suggestions.
- Store prompt version and model metadata.
- Allow coaches to report poor output.

## 5.22.4 AI Context Inputs

Potential inputs:

- athlete age
- position
- training age
- goals
- recent workouts
- completion rate
- readiness
- testing history
- coach notes
- equipment
- time available
- restrictions
- program phase

## 5.22.5 AI Output Schema

AI-generated workouts should return structured JSON:

```json
{
  "title": "Pitcher Recovery and Arm Care",
  "objective": "Reduce fatigue and restore movement quality",
  "estimated_minutes": 45,
  "sections": [
    {
      "name": "Warm-Up",
      "exercises": [
        {
          "exercise_id": "uuid",
          "sets": 2,
          "reps": 8,
          "duration_seconds": null,
          "rest_seconds": 30,
          "notes": "Move under control"
        }
      ]
    }
  ],
  "coach_review_notes": [
    "Confirm athlete has no pain before assignment."
  ]
}
```

The backend must validate all AI JSON before storing it.

---

# 6. System Architecture

## 6.1 Recommended Architecture

### Frontend

- React
- TypeScript
- Vite or Next.js
- Tailwind CSS
- component library such as shadcn/ui
- TanStack Query
- React Hook Form
- Zod

### Backend

- Python 3.12+
- FastAPI
- SQLAlchemy 2.x
- Pydantic 2.x
- Alembic
- Celery, Dramatiq, or RQ for background jobs
- Redis

### Database

- PostgreSQL

### Authentication

- Supabase Auth or Clerk

### Storage

- AWS S3
- Cloudflare R2
- Supabase Storage

### Payments

- Stripe

### AI

- OpenAI API

### Hosting

MVP:

- Vercel for frontend
- Render, Railway, Fly.io, or AWS for backend
- managed PostgreSQL
- managed Redis
- object storage

## 6.2 High-Level Components

```text
Web Browser / Mobile Browser
        |
        v
React Frontend
        |
        v
FastAPI REST API
        |
        +--> PostgreSQL
        |
        +--> Redis / Background Jobs
        |
        +--> Object Storage
        |
        +--> Stripe
        |
        +--> Email Provider
        |
        +--> OpenAI API
```

---

# 7. Repository Structure

```text
athleteos-platform/
├── README.md
├── SRS.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── package.json
├── pyproject.toml
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   ├── product/
│   ├── security/
│   ├── testing/
│   └── decisions/
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── features/
│   │   │   ├── auth/
│   │   │   ├── athletes/
│   │   │   ├── workouts/
│   │   │   ├── testing/
│   │   │   ├── videos/
│   │   │   ├── recruiting/
│   │   │   ├── messaging/
│   │   │   ├── billing/
│   │   │   └── reports/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── stores/
│   │   └── types/
│   └── tests/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── permissions/
│   │   ├── integrations/
│   │   ├── tasks/
│   │   └── utils/
│   ├── migrations/
│   └── tests/
├── scripts/
├── infrastructure/
├── prompts/
└── fixtures/
```

---

# 8. Database Requirements

## 8.1 Core Tables

The initial database should include at minimum:

- users
- organizations
- organization_memberships
- invitations
- roles
- permissions
- athletes
- athlete_guardians
- guardian_relationships
- teams
- team_memberships
- tags
- athlete_tags
- exercises
- workout_templates
- workout_template_sections
- workout_template_items
- workout_assignments
- workout_assignment_items
- workout_logs
- workout_item_logs
- readiness_checkins
- throwing_programs
- throwing_program_days
- test_definitions
- testing_sessions
- test_results
- armcare_sessions
- videos
- video_feedback
- schools
- college_contacts
- athlete_school_targets
- recruiting_interactions
- recruiting_tasks
- offers
- commitments
- conversations
- conversation_members
- messages
- events
- notifications
- notification_preferences
- service_plans
- subscriptions
- invoices
- payments
- reports
- ai_requests
- ai_outputs
- audit_logs
- files
- feature_flags

## 8.2 Common Columns

Most tables should include:

```sql
id UUID PRIMARY KEY
organization_id UUID
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL
created_by UUID
updated_by UUID
```

## 8.3 Soft Deletion

Use:

```sql
deleted_at TIMESTAMPTZ NULL
deleted_by UUID NULL
```

for athletes, workouts, exercises, videos, schools, contacts, and other recoverable records.

## 8.4 Indexing

Create indexes for:

- organization_id
- user_id
- athlete_id
- coach_id
- status
- due_date
- created_at
- school_id
- conversation_id
- external provider IDs
- public profile slug

## 8.5 Data Validation

Examples:

- graduation year within reasonable range
- test result within configured valid range
- email normalized
- phone normalized
- subscription amount nonnegative
- workout due date not before assignment date
- offer expiration not before offer date
- signing date not before commitment date unless overridden

---

# 9. API Requirements

## 9.1 API Standards

- REST JSON API
- versioned routes: `/api/v1`
- authenticated routes require bearer token
- pagination
- filtering
- sorting
- consistent error responses
- OpenAPI documentation
- idempotency for payment and selected create operations
- request IDs
- structured logging

## 9.2 Error Format

```json
{
  "error": {
    "code": "ATHLETE_NOT_FOUND",
    "message": "The requested athlete could not be found.",
    "details": {},
    "request_id": "uuid"
  }
}
```

## 9.3 Example Endpoint Groups

### Auth

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/logout`
- `POST /api/v1/auth/forgot-password`
- `POST /api/v1/auth/reset-password`

### Organizations

- `GET /api/v1/organizations`
- `POST /api/v1/organizations`
- `GET /api/v1/organizations/{organization_id}`
- `PATCH /api/v1/organizations/{organization_id}`

### Athletes

- `GET /api/v1/athletes`
- `POST /api/v1/athletes`
- `GET /api/v1/athletes/{athlete_id}`
- `PATCH /api/v1/athletes/{athlete_id}`
- `DELETE /api/v1/athletes/{athlete_id}`

### Workouts

- `GET /api/v1/workout-templates`
- `POST /api/v1/workout-templates`
- `POST /api/v1/workout-assignments`
- `GET /api/v1/workout-assignments/{id}`
- `POST /api/v1/workout-assignments/{id}/start`
- `POST /api/v1/workout-assignments/{id}/submit`
- `POST /api/v1/workout-assignments/{id}/review`

### Testing

- `GET /api/v1/test-definitions`
- `POST /api/v1/testing-sessions`
- `POST /api/v1/test-results`
- `GET /api/v1/athletes/{athlete_id}/progress`

### Videos

- `POST /api/v1/videos/upload-url`
- `POST /api/v1/videos`
- `GET /api/v1/videos/{video_id}`
- `POST /api/v1/videos/{video_id}/feedback`

### Recruiting

- `GET /api/v1/schools`
- `POST /api/v1/athletes/{athlete_id}/school-targets`
- `POST /api/v1/recruiting/interactions`
- `POST /api/v1/recruiting/tasks`
- `POST /api/v1/offers`
- `POST /api/v1/commitments`

### Billing

- `GET /api/v1/plans`
- `POST /api/v1/billing/checkout-session`
- `POST /api/v1/billing/customer-portal`
- `POST /api/v1/webhooks/stripe`

### AI

- `POST /api/v1/ai/workouts/draft`
- `POST /api/v1/ai/recruiting-email/draft`
- `POST /api/v1/ai/progress-summary/draft`
- `POST /api/v1/ai/outputs/{id}/approve`

---

# 10. Frontend Requirements

## 10.1 General UX

- mobile-first
- responsive
- accessible
- fast
- simple navigation
- clear loading states
- clear empty states
- clear validation
- autosave drafts where appropriate
- confirmation for destructive actions
- readable charts
- no hidden critical actions

## 10.2 Navigation

### Coach Navigation

- Dashboard
- Athletes
- Teams
- Workouts
- Testing
- Videos
- Recruiting
- Messages
- Calendar
- Reports
- Billing
- Settings

### Athlete Navigation

- Today
- Program
- Progress
- Videos
- Recruiting
- Messages
- Calendar
- Profile

### Parent Navigation

- Overview
- Progress
- Recruiting
- Billing
- Messages
- Calendar

## 10.3 Athlete Detail Tabs

- Overview
- Program
- Testing
- ArmCare
- Videos
- Recruiting
- Messages
- Reports
- Billing
- Notes
- Files

## 10.4 Empty States

Every page must explain:

- what the page is for
- why no data exists
- what action the user should take

---

# 11. Security Requirements

## 11.1 Authentication

- secure tokens
- expiration
- refresh tokens
- MFA for sensitive roles
- session invalidation
- brute-force protection

## 11.2 Authorization

- role-based access control
- organization scoping
- athlete assignment scoping
- parent relationship scoping
- backend enforcement

## 11.3 Data Protection

- TLS
- encrypted managed database
- encrypted object storage
- signed URLs
- short-lived upload URLs
- no secrets in frontend
- secret manager for production
- sanitized logs

## 11.4 Audit Logging

Log:

- user login
- failed login
- role change
- athlete creation
- athlete archive
- private record access where appropriate
- report export
- subscription change
- payment action
- AI approval
- public profile change
- data export
- impersonation

## 11.5 Minor Athlete Considerations

- guardian consent
- configurable communication policy
- public profile disabled by default
- limited data exposure
- consent history
- age-aware terms

---

# 12. Non-Functional Requirements

## 12.1 Performance

- common API requests under 500 ms excluding external services
- dashboard initial usable state under 3 seconds on normal broadband
- large video upload must use direct-to-storage upload
- pagination for large lists
- background processing for video and reports

## 12.2 Availability

MVP target: 99.5% monthly availability.

## 12.3 Scalability

Initial target:

- 100 organizations
- 10,000 users
- 5,000 athletes
- 100,000 workout records
- 50,000 videos

Architecture must support scaling without full rewrite.

## 12.4 Accessibility

Target WCAG 2.1 AA where practical.

Requirements:

- keyboard navigation
- labels
- focus states
- contrast
- screen reader support
- captions or text alternative for instructional videos where available

## 12.5 Maintainability

- type checking
- linting
- formatting
- modular services
- automated migrations
- test coverage
- CI pipeline
- ADRs for major decisions

---

# 13. Testing Requirements

## 13.1 Backend Testing

- unit tests
- service tests
- repository tests
- API integration tests
- permission tests
- tenant isolation tests
- webhook tests
- AI schema validation tests

## 13.2 Frontend Testing

- component tests
- form validation tests
- route permission tests
- end-to-end workflows
- responsive testing

## 13.3 Critical End-to-End Tests

1. Owner creates organization.
2. Owner invites coach.
3. Coach adds athlete.
4. Parent accepts invitation.
5. Coach assigns workout.
6. Athlete completes workout.
7. Athlete uploads video.
8. Coach reviews video.
9. Coach enters test result.
10. Athlete views progress.
11. Coach creates recruiting target.
12. Coach logs outreach.
13. Parent purchases plan.
14. Stripe webhook activates subscription.
15. AI drafts workout.
16. Coach edits and approves draft.

## 13.4 Security Tests

- unauthorized tenant access
- IDOR
- role escalation
- signed URL expiration
- webhook replay
- invalid file upload
- rate limits
- SQL injection
- XSS
- CSRF where relevant

---

# 14. DevOps and Deployment

## 14.1 Environments

- local
- test
- staging
- production

## 14.2 CI Pipeline

On pull request:

- lint frontend
- typecheck frontend
- test frontend
- lint backend
- typecheck backend
- test backend
- migration validation
- dependency security scan
- build containers

## 14.3 Deployment Rules

- staging deploy after merge
- production deploy through approved release
- database backup before risky migration
- reversible migrations when possible
- feature flags for major features

## 14.4 Environment Variables

Examples:

```env
DATABASE_URL=
REDIS_URL=
AUTH_SECRET=
OPENAI_API_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
S3_BUCKET=
S3_REGION=
S3_ACCESS_KEY_ID=
S3_SECRET_ACCESS_KEY=
EMAIL_PROVIDER_API_KEY=
FRONTEND_URL=
BACKEND_URL=
```

Never commit real secrets.

---

# 15. Implementation Phases

## Phase 0 — Foundation

Deliverables:

- repository
- frontend shell
- backend shell
- database
- authentication
- organization model
- memberships
- role system
- CI
- local Docker setup
- environment documentation

## Phase 1 — Athlete Management

Deliverables:

- coach dashboard
- athlete list
- athlete profile
- guardian linkage
- teams
- tags
- notes
- files
- permissions

## Phase 2 — Workouts

Deliverables:

- exercise library
- workout templates
- workout assignment
- athlete completion
- readiness check-in
- coach review
- completion analytics

## Phase 3 — Testing

Deliverables:

- test definitions
- testing sessions
- test results
- ArmCare entry
- progress charts
- athlete reports

## Phase 4 — Video Coaching

Deliverables:

- upload flow
- video processing
- coach review queue
- timestamp comments
- feedback notifications
- service limits

## Phase 5 — Recruiting CRM

Deliverables:

- schools
- contacts
- target lists
- pipeline
- interactions
- tasks
- offers
- commitments
- public profile

## Phase 6 — Billing

Deliverables:

- plans
- checkout
- subscriptions
- webhooks
- billing portal
- invoices
- access limits
- failed payment handling

## Phase 7 — AI Assistance

Deliverables:

- workout draft
- progress summary
- recruiting email draft
- output review
- approval workflow
- prompt versioning
- AI usage tracking

## Phase 8 — Reporting and Admin

Deliverables:

- athlete report
- recruiting report
- business analytics
- platform admin
- support tools
- audit viewer

---

# 16. MVP Definition of Done

The MVP is complete only when:

- organization owners can create an account
- coaches can be invited
- athletes can be added
- guardians can be linked
- workouts can be created and assigned
- athletes can complete workouts
- test results can be recorded
- progress can be charted
- videos can be uploaded
- coaches can leave feedback
- recruiting schools and interactions can be tracked
- subscriptions can be purchased
- Stripe status controls service access
- messages and notifications work
- AI drafts require coach approval
- permissions prevent unauthorized access
- core workflows have tests
- staging and production deployment instructions exist

---

# 17. Coding Standards

## 17.1 Python

- Python 3.12+
- Ruff
- Black-compatible formatting
- MyPy
- Pytest
- type hints
- async where useful
- dependency injection
- service/repository separation
- no business logic in route handlers

## 17.2 TypeScript

- strict mode
- ESLint
- Prettier
- typed API client
- Zod validation
- no `any` unless justified
- feature-based organization
- reusable UI components

## 17.3 Git

Branch examples:

- `feature/athlete-profile`
- `feature/workout-assignment`
- `fix/video-upload-timeout`
- `chore/update-dependencies`

Commit examples:

- `feat: add athlete onboarding flow`
- `fix: enforce organization scope on video endpoint`
- `test: add subscription webhook idempotency tests`

---

# 18. Sample User Stories

## Athlete Management

**As a coach, I want to create an athlete profile so that I can organize all development and recruiting information in one place.**

Acceptance criteria:

- required fields are validated
- athlete belongs to active organization
- duplicate warning appears for matching email/name
- coach assignment can be selected
- guardian invitation can be sent
- audit log is created

## Workout Assignment

**As a coach, I want to assign a workout to an athlete so that the athlete knows exactly what to complete remotely.**

Acceptance criteria:

- coach can select template
- coach can modify assignment
- athlete receives notification
- athlete sees due date
- athlete logs results
- coach can review submission

## Video Review

**As an athlete, I want to upload a bullpen video so that my coach can review it remotely.**

Acceptance criteria:

- supported file validates
- upload progress displays
- video is private
- coach is notified
- athlete can see review status
- athlete receives feedback notification

## Recruiting

**As a recruiting advisor, I want to track each school contact so that no follow-up opportunity is missed.**

Acceptance criteria:

- interaction includes date, contact, summary, and next action
- target school pipeline updates
- follow-up task can be created
- athlete recruiting timeline displays interaction
- only authorized users can view internal notes

---

# 19. Future Roadmap

## Version 2

- native mobile app
- push notifications
- advanced video annotation
- calendar integrations
- e-sign waivers
- CSV import
- organization branding
- advanced reports
- team subscriptions

## Version 3

- computer vision
- pose estimation
- movement comparison
- wearable integrations
- ArmCare API integration
- TrackMan integration
- Rapsodo integration
- Blast Motion integration
- WHOOP integration
- Apple Health integration

## Version 4

- college coach portal
- scout portal
- verified recruiting network
- public showcase pages
- team recruiting dashboards
- athlete marketplace
- multi-coach organizations
- revenue sharing

## Version 5

- softball
- football
- basketball
- golf
- soccer
- volleyball
- tennis
- hockey

---

# 20. Initial Build Prompt for GitHub Copilot or Coding Agent

Use the following prompt when beginning implementation:

> You are the lead software engineer for AthleteOS. Read `SRS.md` completely before changing code. Build the project in the implementation order defined in the SRS. Start with Phase 0 only. Use React and TypeScript for the frontend, Python FastAPI for the backend, PostgreSQL for the database, SQLAlchemy and Alembic for persistence, and Docker Compose for local development. Implement multi-tenant organization isolation, authentication integration interfaces, role-based permissions, structured logging, consistent API errors, testing, and documentation. Do not begin athlete, workout, video, recruiting, billing, or AI features until the foundation is tested. After each task, update `docs/BUILD_STATUS.md` with completed work, remaining work, setup steps, migrations, tests, and known issues. Never commit secrets. Never bypass authorization. Ask for human review before any major architectural change that conflicts with `SRS.md`.

---

# 21. Required Supporting Documents

The coding agent should create and maintain:

- `README.md`
- `SRS.md`
- `docs/BUILD_STATUS.md`
- `docs/ARCHITECTURE.md`
- `docs/DATABASE.md`
- `docs/API.md`
- `docs/SECURITY.md`
- `docs/DEPLOYMENT.md`
- `docs/TESTING.md`
- `docs/ROADMAP.md`
- `docs/decisions/ADR-001-technology-stack.md`
- `.env.example`
- `CONTRIBUTING.md`

---

# 22. Final Product Principle

AthleteOS must make the coach’s expertise scalable without removing the coach from the decision.

The platform succeeds when:

- athletes know what to do
- coaches know what needs attention
- parents understand the value being delivered
- recruiting activity is organized
- athlete progress is measurable
- remote support becomes billable
- the business can grow without losing quality
