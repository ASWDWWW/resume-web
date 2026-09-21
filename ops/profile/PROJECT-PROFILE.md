# Project profile

Last updated: 20 September 2026.  
Owner: Zakiy T. Manigo.  
This file is the reusable intake. Mark every statement as **confirmed**, **assumed**, or **unresolved**.

## Business, products, customers, revenue

**Confirmed (from this repo, Firebase, GitHub, and career packets):**

- Legal/personal name used across git, LinkedIn, and Firebase: Zakiy Manigo (`zakiymanigo@gmail.com`).
- This repository is the public career site (“personal website dev”) on GitHub `ASWDWWW/resume-web`, Firebase project `zakiymanigo-career`.
- Product work evidenced in career packets includes: TREI/BariAccess (clinic-embedded GLP-1 / metabolic care for Bariatric Associates; trei.care; Azure staging); FITD (fashion AI consumer/brand hub; fitdai.com; Firebase FITD apps); FitGenius (pre-launch fitness); Insightful Care Solutions (NJ telepsychiatry site); Alex Road Service / LaunchPage Studios (shop ops + marketing sites); Tax Tracker; plus other ASWDWWW repos.
- Customers differ by product (clinic/care team, consumers, brands, a psychiatric practice, auto shops). This OS does not hold a CRM.

**Assumed:**

- You want one owner OS covering the portfolio, not only the resume site.
- Revenue is mixed (founder products, contract/FDE-style delivery, possible future fundraising). No books are in this repo.

**Unresolved:**

- Legal entities, ownership splits, and which product is “the” company for this OS.
- Current revenue model and prices per product.

## Goals, priorities, success metrics

**Assumed (needs confirmation):** keep the career site current; ship TREI work honestly; keep FITD/FitGenius moving; use this OS so agents do not need one permanent persona per function.

**Unresolved:** numeric targets, hiring plan, fundraising target.

## Team and decision owners

| Area | Owner | Notes |
| --- | --- | --- |
| All decisions in this workspace | Zakiy Manigo | Sole git collaborator on `resume-web` |
| TREI engineering | Zakiy and Andrei | Andrei is the other primary engineer per BariAccess overview |
| FITD | Zakiy | `FITD-fash` GitHub user exists |
| Legal/finance approval | Unresolved | Do not treat agent drafts as approval |

## Repositories, applications, infrastructure, environments

Default for **this** workspace: GitHub `ASWDWWW`, Firebase alias `default`/`dev` → `zakiymanigo-career`, environment = local files. Production deploy is not authorized by OS setup.

See `ops/architecture/SOURCES-OF-TRUTH.md` and `ops/integrations/INVENTORY.md` for the wider map (14 Firebase projects visible to `zakiymanigo@gmail.com`; 30+ ASWDWWW repos; FITD-fash public: `cursor-zoom-oauth-callback` only, without switching accounts).

## Budgets, constraints, sensitive information, access

- Firebase billing **enabled** on the career project (`zakiymanigo-career`, verified 17 September 2026 via Cloud Billing API). Do not change the billing account unless asked.
- No budget numbers in-repo.
- Secrets must not be committed. `ops/restricted/` is gitignored except policy files and is **not** a security boundary.
- Do not use this public repo for investor models, payroll, or PHI/PII dumps.

## Confirmed / assumed / unresolved index

Confirmed facts, assumptions, and questions also live in `ops/records/`. Update those files when a decision is made.
