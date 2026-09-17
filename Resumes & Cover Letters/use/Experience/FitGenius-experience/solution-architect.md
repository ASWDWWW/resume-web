# Solution Architect

**Experience rating:** 7.1 / 10 — Solid match  
**Application guidance:** Apply with framing  
**Family:** Customer-facing  
**Evidence window:** FitGenius founding technical partner, May–September 2026 (pre-launch consumer product)

---

## What this role usually means

Solution architects design how a product lands in a customer's environment: identity, data flows, security, integration, non-functional requirements. Often senior, often enterprise.

## What you actually did on FitGenius

FitGenius is a pre-launch consumer fitness product: iOS and Android (Expo / React Native), Firebase backend (~64 Cloud Functions, Firestore rules, IAP verification, Gemini AI), marketing site (Vite/React), app/legal/admin hosting, store-submission runbooks, and a legal/compliance suite. You were the founding technical partner — one person owning product, code, cloud, QA packets, and founder enablement from roughly May through September 2026.

You architected FitGenius as a system: mobile clients, Cloud Functions, rules as authorization, IAP as billing plane, Vertex as AI plane, health platforms as sensor plane. You wrote security logging, subprocessors, and store privacy mapping. That is solution architecture for *one* product, not for many customer estates.

## How that work applies to **Solution Architect**

Apply to mid-level SA roles that want you to design the deployment of a SaaS. Stretch for enterprise SA (VNet, SSO to Okta, data residency). Prefer pairing this title with FDE if the posting is hybrid.

## Strengths a hiring manager can credit

- Clear system decomposition
- Security/privacy as architecture, not afterthought
- Written architecture for counsel and founder

## Gaps versus a typical hiring bar

- No multi-cloud customer landing
- No enterprise IAM integrations
- Title often expects 5–10 years customer-facing architecture

## How to talk about it

Use architecture diagrams in words: client → callables → Firestore; stores → webhooks → entitlements; Gemini sees allowlisted context only.

## Repo evidence

`firestore.rules`, `company/legal/protection-suite/md/11_third-party-services.md`, `firebase.json`

## Rating rationale

Real architecture, limited customer-variety/seniority signal.

---

*This document is one of a set. See [00-overview.md](./00-overview.md) for all titles, scores, and method.*
