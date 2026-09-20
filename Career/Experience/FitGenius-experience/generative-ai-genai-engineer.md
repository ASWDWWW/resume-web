# Generative AI / GenAI Engineer

**Experience rating:** 8.1 / 10 — Strong match  
**Application guidance:** Apply now  
**Family:** Product / AI product  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

GenAI engineers ship generation features: text, images, sometimes video. They handle prompts, safety, fallbacks, and UX of generated content.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

Text generation (coach, plans, motivation, food macros) plus `generateImage` that uses curated Unsplash IDs rather than a generative image model. Daily scheduled generation for users. Structured JSON generation for workouts/meals.

## How that work applies to **Generative AI / GenAI Engineer**

Apply for GenAI *feature* roles. Be honest that image generation is a curated fallback, not Imagen/SD in production. Text GenAI is real and user-facing.

## Strengths a hiring manager can credit

- Multiple generation surfaces in one product
- Scheduled generation job
- Fallbacks when generation is the wrong tool

## Gaps versus a typical hiring bar

- Image path is not generative
- No media-model pipeline
- Limited prompt-eval tooling

## How to talk about it

Emphasize structured generation + fallbacks. Do not claim you built a media model stack.

## Repo evidence

`fitgeniusAi` actions, `generateDailyContentScheduled`, Unsplash fallback in functions

## Rating rationale

Real GenAI product work; image claim must stay honest.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
