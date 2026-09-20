# Full-Stack Engineer

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## Experience rating (this project only)

**5 / 10 — Partial match**

Relevant skills exist, but a typical hiring bar for this title is broader than what this repo contains.

Ratings are not a prediction of whether you can *learn* the job. They measure how much **this repository** already looks like the work that title is hired to do.

## What this role typically requires

Own UI and server: data models, APIs, auth, and the client that consumes them. Comfortable in at least one frontend framework and one backend stack, plus a database.

## What you have done in this project

Frontend is substantial (React 18 production, React 19 redesign, Tailwind, Vite). Backend is a real but narrow slice: Google Apps Script web app that validates POST JSON and sends two emails. Hosting/config (Firebase, headers, SPA rewrite) is the “ops” third of a small full-stack deploy. EmailJS was evaluated and documented even though GAS won.

## How that work applies to Full-Stack Engineer

You did cross the stack boundary: the form is not a `mailto:` link; it is a client-server contract with error handling. You also integrated a third-party system (ChARM) instead of building scheduling. That is full-stack thinking at small-business scale: UI + API + vendor + deploy.

## Gaps versus a typical hiring bar

No SQL/NoSQL, no session/auth, no REST framework, no ORMs, no background jobs beyond GAS’s request lifetime. Most Full-Stack Engineer listings mean Node/Django/Rails + Postgres. This is full-stack-lite.

## How to talk about it

Call yourself full-stack only with the qualifier “frontend-heavy.” Describe GAS as a serverless handler, not as “I built a backend platform.” Mention what you would add (Node API, DB, auth) if the practice needed a patient portal.

## Bottom line

Honest junior full-stack-lite. Competitive when the job is React-first with light backend; weak when the job is API/database-first.
