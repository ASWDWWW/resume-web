# AI/Search Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **2.0 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **AI/Search Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Search engineers build retrieval: indexing, ranking, query understanding, sometimes embeddings. AI/Search blends classic IR with ML.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to AI/Search Engineer

You specified client-side global search over customers, WO IDs, and invoice IDs with a 300ms UX target. That is product search, not information retrieval engineering.

## Concrete evidence from this project

- Planned/implemented in-app search for staff (cross-cutting epic E10).
- No inverted index service, no ranking, no embeddings.

## Gaps versus a typical hiring bar

Lucene/Elasticsearch/OpenSearch, query pipelines, evaluation (nDCG) — absent.

## How to talk about this

- Call it application search, not Search Engineer experience.

## Repo pointers

- `dev/docs/IMPLEMENTATION_PLAN.md` US-E10-01 Global search
