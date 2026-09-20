# Mobile Engineer

**Project-experience rating: 8.0 / 10** (Strong)

## How to read the rating

The score is **experience this project gave you for this title**, not a career-total grade.

| Band | Score | Meaning |
| --- | --- | --- |
| Direct match | 8.5–10 | You already did this job on TREI. Interviews should lead with this work. |
| Strong | 7.0–8.4 | Substantial overlapping ownership. Name the gaps; do not overclaim seniority. |
| Adjacent | 5.5–6.9 | Real transferable work, but it is not the center of this title. |
| Partial | 4.0–5.4 | Some relevant pieces. Use as supporting evidence, not the headline. |
| Thin | 2.5–3.9 | Indirect overlap only. |
| Minimal | 0–2.4 | This project barely touches the role. |

Scope of evidence: 17 July 2026 – 16 September 2026. You are one of two primary engineers on TREI (BariAccess), with about 203 commits, ~99k lines added, and 658 files touched. Andrei remains the other primary author and owns more of the domain-engine and production-estate volume. Do not claim sole authorship of the whole platform.



## Project in one paragraph

**TREI** is the patient and care-team product in this repository. It is a wellness-first GLP-1 and metabolic-care platform for Bariatric Associates. You helped build a TypeScript monorepo with a Fastify API, PostgreSQL as system of record, a worker plus transactional outbox, an Expo iPhone app, a React staff console, and the public/patient site at trei.care. Staging runs on Azure Container Apps with Entra/External ID, Key Vault, Service Bus, Stripe sandbox, Calendly, Spike wearable adapters, and a guarded Azure OpenAI assistant named Aba.


## What this role typically owns

Ships a phone application: navigation, offline/session, store release, device APIs, and mobile-specific performance/UX.

## What you did on TREI that maps here

You built the TREI iPhone experience in Expo/React Native: application frame, Today, Plan, Progress, Aba text/voice, connected health, session storage, OIDC, push-related session boundaries, and TestFlight-oriented release wiring. Physical-device identity (Apple public client, associated domains) was part of your work.

## How that experience applies to this job

Mobile Engineer means you understand that a phone is not a small browser. You handled OS-secure session storage, request timeouts, stale refresh, microphone gating, WebRTC voice, and App Store / TestFlight constraints. The product is Apple-first and has a real bundle id and ASC app id.

## Evidence from this repository

- apps/patient-mobile Expo app, EAS profiles, TestFlight submit config
- Apple Sign-In entitlements, associated domains for www.trei.care
- Aba native WebRTC voice path with backend-checked speech
- Connected-health Oura return controller and unified source shelf

## Strengths you can claim honestly

Production-minded mobile: identity, permissions copy, release profiles, honest network failure.

## Gaps a hiring manager will still probe

Android is configured, not shipped. Little native module authorship. No long history of store reviews, crashlytics at scale, or offline-first sync engines.

## How to talk about it

Lead with TestFlight + Apple identity + voice. Say Expo/RN explicitly so they do not assume Swift.

## Bottom line

Strong cross-platform mobile engineer for an iOS-first product. Call the Android gap yourself.
