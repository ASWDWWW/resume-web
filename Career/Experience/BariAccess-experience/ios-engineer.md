# iOS Engineer

**Project-experience rating: 6.4 / 10** (Adjacent)

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

Native iOS: Swift, SwiftUI/UIKit, Combine, Apple frameworks, App Store, and device APIs at the native layer.

## What you did on TREI that maps here

You shipped an iPhone product through Expo: bundle identifier com.bariatricassociates.bariaccess, Apple Sign-In, associated domains, APS environment, camera-purpose plist copy, microphone permission, EAS TestFlight, and public-client token redemption that must not send Origin. Voice uses a native WebRTC session.

## How that experience applies to this job

This counts as iOS product delivery, which many 'iOS Engineer' jobs actually need. It does not count as native iOS engineering. You will lose a SwiftUI architecture loop unless the team accepts React Native.

## Evidence from this repository

- app.json iOS entitlements, associated domains, Apple Sign-In
- eas.json testflight submit with ascAppId
- fix: redeem staging Apple HTTPS codes as a public client
- Voice conversation on physical iPhone path (proof still called out as open in docs)

## Strengths you can claim honestly

You have fought real Apple identity and release issues, which many RN developers skip.

## Gaps a hiring manager will still probe

No Swift/Obj-C code ownership. No UIKit, Core Data, CloudKit, or App Intents. Android-first iOS teams will still want native samples.

## How to talk about it

Apply to iOS-using product teams that list React Native. For native-only iOS, treat this as adjacent evidence and study Swift.

## Bottom line

Good iOS *product* experience. Incomplete iOS *platform* experience.
