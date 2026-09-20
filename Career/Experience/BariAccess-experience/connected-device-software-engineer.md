# Connected-Device Software Engineer

**Project-experience rating: 7.4 / 10** (Strong)

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

The software around devices: pairing/OAuth, cloud sync, device identity, telemetry, companion apps, privacy.

## What you did on TREI that maps here

This is one of your strongest specialized stories. You implemented Spike as a post-login adapter, Oura as the production-shaped wearable, gated Garmin/Polar, then Whoop/Withings/Samsung through cloud custody. Offer, connect, callback, disconnect, erase, minimum observations, and a unified patient/staff shelf are the companion-app + cloud job.

## How that experience applies to this job

Connected-device companies (wearables, home health, IoT apps) hire people who keep vendor APIs from becoming the identity authority and who handle missing/stale/zero as different states. That is written into TREI architecture and your recent SELECT_MANY work.

## Evidence from this repository

- Spike webhook adapter, data contract, live path, application 11922 cutover docs
- Provider integration authorization/status/delete plus sleep and daily queries
- SELECT_MANY custody: one active source per provider, refuse SELECT_ONE rollback while multiple live
- Staff source strip + phone connected-health shelf
- Erasure reconciliation script and privacy-safe staff copy on outage vs disconnect

## Strengths you can claim honestly

Consent, provenance, vendor failure modes, multi-provider product design.

## Gaps a hiring manager will still probe

No BLE pairing, no device firmware, no on-device signal processing. Cloud-and-app side of connected devices.

## How to talk about it

Lead with 'devices are adapters, not identity.' Walk Oura vs cloud providers and erasure.

## Bottom line

Excellent fit for companion-app / device-cloud roles. Do not pretend you wrote watch firmware.
