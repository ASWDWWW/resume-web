# Sensor Algorithm Engineer

**Project-experience rating: 5.4 / 10** (Partial)

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

Algorithms on raw sensor streams: IMU, PPG, sleep staging, on-device or near-device DSP.

## What you did on TREI that maps here

You consumed vendor-processed metrics (sleep duration, deep sleep, steps, HRV RMSSD) and implemented product rules such as minimum observations and sleep regularity *evidence* gates. You did not stage sleep from PPG or write a step-count algorithm.

## How that experience applies to this job

Sensor algorithm teams at Oura/Whoop would not count this as peer work. Digital-health teams that integrate sensors might.

## Evidence from this repository

- Oura sleep product scope and daily observations
- Garmin/Polar minimum-observation staging path
- Whoop sleep + Withings/Samsung steps and sleep pulls
- packages/domain/src/decision/rr/sleep-regularity.ts exists as productized evidence

## Strengths you can claim honestly

You know vendor metrics are not ground truth and you keep units/native meaning.

## Gaps a hiring manager will still probe

No raw sensor DSP, no labeled lab protocol, no on-device models.

## How to talk about it

Position as sensor-*integration* algorithms, not sensor-*invention*.

## Bottom line

Partial. Stronger as Connected-Device than as Sensor Algorithm Engineer.
