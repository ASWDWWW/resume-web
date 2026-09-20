# Backend Engineer

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## Experience rating (this project only)

**3 / 10 — Adjacent only**

Transferable habits, not the core craft of the role.

Ratings are not a prediction of whether you can *learn* the job. They measure how much **this repository** already looks like the work that title is hired to do.

## What this role typically requires

Services, APIs, data stores, reliability, authz, queues, and business logic that lives off the client. Interviews assume you have designed schemas and reasoned about consistency, latency, and failure.

## What you have done in this project

You implemented `GAS_CODE.js`: `doPost` parses JSON, rejects missing name/email/message, sends a staff notification with `replyTo`, sends a patient confirmation, and returns `{success, message|error}`. You documented OAuth/deploy for that web app. You configured Firebase Hosting rewrites and cache headers.

## How that work applies to Backend Engineer

That is an HTTP handler with validation, side effects, and a JSON contract — the smallest unit of backend work. Thinking about reply-to headers and dual-send UX is backend product sense. Choosing a serverless host instead of standing up Express is a valid (if limited) backend decision.

## Gaps versus a typical hiring bar

No persistent storage, no auth, no idempotency, no rate limits, no tests, no observability, no schema. PHI/PII going to email is an operational concern a backend engineer would flag. This will not pass a backend-focused screen on its own.

## How to talk about it

Use it as “I have written a production webhook-style endpoint,” then show other backend work if you have it. If you do not, treat backend as a learning goal, not a claim.

## Bottom line

Not a Backend Engineer profile. Keep the GAS story as a supporting anecdote.
