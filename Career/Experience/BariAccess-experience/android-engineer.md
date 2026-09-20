# Android Engineer

**Project-experience rating: 3.2 / 10** (Thin)

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

Native Android: Kotlin, Jetpack, Play Store, background work, and Android-specific identity/notifications.

## What you did on TREI that maps here

The Expo app declares an Android package and adaptive icon, and package.json has `preview:android`. The documented product path is Apple-first TestFlight. There is no Play Store submit profile, no Kotlin, and generated android/ is gitignored.

## How that experience applies to this job

You can honestly say the client is cross-platform capable and you understand mobile session/OIDC patterns that would transfer. You cannot claim Android shipping, Play review, or Jetpack architecture.

## Evidence from this repository

- app.json android.package com.bariatricassociates.bariaccess
- preview:android script using expo run:android
- No EAS submit.android / Play track in eas.json

## Strengths you can claim honestly

Shared RN skills (navigation, secure storage, networking) would shorten an Android ramp.

## Gaps a hiring manager will still probe

No shipped Android build, no Kotlin, no Play Console, no Android-specific push/background work proven.

## How to talk about it

Do not lead with this title. If asked, say iOS-first Expo with Android package present, not delivered.

## Bottom line

Insufficient as a primary Android Engineer application from this project alone.
