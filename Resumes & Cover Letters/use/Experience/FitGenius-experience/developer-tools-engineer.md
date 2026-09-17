# Developer Tools Engineer

**Experience rating:** 6.4 / 10 — Credible adjacent  
**Application guidance:** Stretch only  
**Family:** Cloud / platform  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Builds tools developers use: CLIs, codegen, linters, build systems, editors, internal apps. Mix of product sense and systems.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

Substantial tooling: legal HTML generator from in-app JSON, locale translation/override pipeline (including Python batch translate), Firestore dump catalog extract, PDF generators for company docs, health inventory dumper, Firebase project migration helper, native release configure script, Xcode team alignment.

## How that work applies to **Developer Tools Engineer**

Apply when the job is product-minded tools (internal apps, codegen, repo automation). Skip compiler/runtime jobs. Your tools exist to keep a product consistent (legal, i18n, store types), which is a good tools-engineer story.

## Strengths a hiring manager can credit

- Multiple real tools with documented npm scripts
- Policy encoded in generators (legal freshness tests)
- Mixed JS/Python tooling

## Gaps versus a typical hiring bar

- Tools are repo-local, not distributed products
- No IDE extension / compiler work

## How to talk about it

Story: 'legal pages cannot drift from in-app copy because CI regenerates and tests them.'

## Repo evidence

`scripts/generate-legal-hosting.mjs`, `scripts/generate-locale-translations.mjs`, `web/tests/pages.test.mjs`

## Rating rationale

Credible tools work; not a tools-product company depth.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
