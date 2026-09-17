# AI/Search Engineer

**Experience rating:** 4.8 / 10 — Weak / stretch  
**Application guidance:** Unlikely — only if posting is unusually broad  
**Family:** ML / data  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Builds retrieval and ranking: inverted indexes, embeddings, query understanding, relevance metrics. Often overlapping with information retrieval.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You proxied Google Places (New) for gym search with type filters, matched exercises by catalog name, and matched GPS routes to segments by haversine radius. That is search-*adjacent* product work, not an IR platform.

## How that work applies to **AI/Search Engineer**

Do not apply to search-infra roles. You can discuss filtering and geometric matching. You did not build ranking, embeddings, or query pipelines.

## Strengths a hiring manager can credit

- Places proxy with domain filters
- Catalog name matching
- Segment matching as a retrieval problem (tiny)

## Gaps versus a typical hiring bar

- No Elasticsearch/OpenSearch/vector DB
- No relevance evaluation
- No query planner

## How to talk about it

Skip unless the posting is 'search' meaning 'call Places and filter.'

## Repo evidence

`functions/src/places.ts`, `libraryExerciseMatch.ts`, `functions/src/outdoor/segments.ts`

## Rating rationale

Small retrieval tasks, not a search system.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
