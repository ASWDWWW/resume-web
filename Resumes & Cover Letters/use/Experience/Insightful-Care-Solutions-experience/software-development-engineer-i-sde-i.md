# Software Development Engineer I (SDE I)

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## Experience rating (this project only)

**6 / 10 — Solid adjacent / junior**

Enough real work to claim the title at junior level if you are honest about scope.

Ratings are not a prediction of whether you can *learn* the job. They measure how much **this repository** already looks like the work that title is hired to do.

## What this role typically requires

Amazon-style SDE I: write production code, understand time/space basics, own small features, work in a service-oriented environment. Interviews overweight algorithms plus a simple design question.

## What you have done in this project

You wrote and shipped production JavaScript/React, a GAS `doPost` handler with validation and dual email send, and static SEO/crawler contracts (`robots.txt`, `sitemap.xml`, `llms.txt`, JSON-LD). You operated a cloud hosting pipeline (Vite build → Firebase Hosting rewrite to `index.html`).

## How that work applies to Software Development Engineer I (SDE I)

SDE I cares that you can implement a spec and put it in production. The contact form is a mini service: JSON in, validate, side effects (two emails), JSON out, error path. The SPA rewrite and cache headers are a small taste of “how the thing actually runs.” Healthcare content constraints show you can work inside rules.

## Gaps versus a typical hiring bar

SDE I loops will not be impressed by a marketing SPA alone. No algorithms practice is evidenced here. No Java/C++/typed backend, no distributed design, no on-call. GAS is not a typical SDE service.

## How to talk about it

Map GAS `doPost` to an API handler. Map Firebase rewrite/caching to “how we serve a CSR app.” Then pivot to LeetCode/system-design prep as a separate track — this repo will not carry the SDE interview.

## Bottom line

Reasonable SDE I portfolio story if paired with strong interview prep. Not an SDE I resume by itself at Amazon-scale companies.
