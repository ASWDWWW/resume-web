# Infrastructure Engineer

**Evidence source:** Insightful Care Solutions LLC — production telepsychiatry website for a New Jersey psychiatric practice  
**Live site:** https://insightfulcare.solutions/  
**Your role on the work:** Solo engineer (Zakiy Manigo), Oct 2025 – Jul 2026  
**What shipped:** React + Vite + Tailwind SPA, Firebase Hosting, Google Apps Script contact backend, ChARM Health booking integration, SEO/AI-crawler assets, accessibility and responsive UX, client-facing ops docs


## Experience rating (this project only)

**2 / 10 — Weak adjacency**

A few related decisions, not role-shaped experience.

Ratings are not a prediction of whether you can *learn* the job. They measure how much **this repository** already looks like the work that title is hired to do.

## What this role typically requires

Servers, networks, IAM, Terraform, Kubernetes, capacity, patching, reliability of the substrate others run on.

## What you have done in this project

Firebase Hosting for a static SPA, SPA rewrite, cache headers (long for assets, no-cache for `index.html`), HTTPS via the host, custom domain `insightfulcare.solutions`. Manual CLI deploy documented in `DEPLOYMENT_GUIDE.md`.

## How that work applies to Infrastructure Engineer

You touched the serving layer and cache policy — infrastructure that users feel (stale HTML vs hashed assets). You kept production hosting config at repo root, separate from app source.

## Gaps versus a typical hiring bar

No VMs, containers, IaC, load balancers you configured, no monitoring, no HA design. Firebase abstracted almost all infrastructure.

## How to talk about it

Describe it as managed hosting, not infrastructure engineering.

## Bottom line

Not a match beyond basic hosting literacy.
