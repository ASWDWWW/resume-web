# Ticket

- ID: SITE-20260917-refresh
- Date: 17 September 2026
- Status: done
- Product / repo: resume-web (`ASWDWWW/resume-web`)
- GitHub identity: **github-aswdwww** (`ASWDWWW`) for this repo. Do not switch to `FITD-fash`. **Public site** must link **both** `https://github.com/ztm2106` and `https://github.com/ASWDWWW`.
- Firebase: `zakiymanigo@gmail.com` / project `zakiymanigo-career` (aliases `default` and `dev`)
- Gmail: not required for this ticket (no send). Contact form stays as-is.
- Owner: Zakiy Manigo
- Goal: Refresh `public/` with approved public facts from `Career/` and media from `Content/`, put media in Firebase Storage with public download URLs, and redesign galleries and project stories so they work on desktop and mobile. **Stop before deploy.**
- Success metric: Local `public/index.html` shows galleries, project stories, education, and contact using only allowed copy and Storage URLs; desktop and mobile verified in the browser; no `firebase deploy`; no git commit unless a later message asks.
- Authorization (draft/send, test/live, deploy?): local site files + Storage setup only. **Do not** `firebase deploy`, **do not** git commit, **do not** change the billing account. Billing is already **on** (verified 17 Sep 2026). Do not treat MCP `Billing Enabled: No` as ground truth.

## In scope

1. Inventory `Content/` (~20 images/videos) and map each folder to a site section.
2. Pull **public copy only** from Career top-level notes and each Experience `*/00-OVERVIEW.md` or `README.md` (see source table below). Use product-fact paragraphs only; strip ratings.
3. Add Firebase Storage + public download URLs for the inventoried media. Record object paths and URLs in this ticket or a sibling note under `ops/product-engineering/` when implementation runs.
4. Redesign `public/index.html` (and CSS if needed) for photo/video galleries, project stories, education, and contact. Keep existing contact behavior (Google Apps Script endpoint already in the page).
5. Verify in the browser (desktop and a mobile viewport) before calling the implementation done.
6. Preserve `Career/`, `Content/`, `Resumes & Cover Letters/` (including unfinished `use/` deletions), `index-safety.html`, and `css/style.css` unless a later message says otherwise. Copy media into Storage / site references; do not delete source trees.

## Out of scope (until a later message)

- `firebase deploy` (hosting or storage rules to production)
- git commit / push
- Publishing every Career markdown file
- Job-title packets (`Career/Experience/*/*.md` except the allowed overview/README files)
- Ratings tables, “do not claim” / gap lists, headline-title recommendations
- `Career/University Transcripts/` and `Life/University Transcripts/` (PDFs stay off the site)
- `Career/Job Listing.md` (target-company list, not public bio)
- Enabling billing / Blaze (already on; do not attach a different account)
- Reverting or “cleaning up” unfinished resume-folder work
- Account switching (`gh auth switch`, other Firebase projects, other Gmail)

## Copy sources (allowed)

Use these files. Quote public product facts, dates, and education/community notes. Do **not** paste rating scales, score tables, “do not claim” sections, or job-title packet bodies.

| File | Use on site |
| --- | --- |
| `Career/Berkshire School.md` | Education + Berkshire gallery story |
| `Career/3+2 Engineering Combined Program.md` | Dual-degree explanation for education (Columbia + SLU). Do **not** link or host the transcript PDFs it describes. |
| `Career/Football Career.md` | Athletics note. Dates/place already aligned to `Berkshire School.md` (17 Sep 2026). |
| `Career/NYC BioHacker Expo.md` | BariAccess / TREI story + NYC expo gallery |
| `Career/Belgrade Profex Academy.md` | BariAccess / TREI story + Belgrade gallery |
| `Career/Hobbies-Activities.md` | About / community; Siloam-Hope maps to church photos |
| `Career/Weave News.md` | Education / writing (already linked from school section) |
| `Career/Experience/BariAccess-experience/00-OVERVIEW.md` | TREI product paragraph and shipped surfaces. **Employment: Jun 2025 – Present (current).** Ignore rating bands and “do not claim.” Prefer this over the folder README if they overlap. |
| `Career/Experience/FitGenius-experience/00-overview.md` | “What you built” inventory only |
| `Career/Experience/Insightful-Care-Solutions-experience/00-overview.md` | Live-site / stack facts only |
| `Career/Experience/Automotive-Operations-Platform-experience/00-OVERVIEW.md` | “What you actually built” bullets only |
| `Career/Experience/FITD-experience/README.md` | “Findings (what this project actually is)” table/paragraph only |
| `Career/Experience/Tax-Tracker-experience/OVERVIEW.md` | **Project snapshot** only (agreed). Do not publish scores, target/stretch lists, or title packets. Skip `README.md` (it only points here). |

Local AI public copy: **`Career/Experience/Offline-Windows-Desktop-LLM-Client-experience/OVERVIEW.md`** — “project in one paragraph” only. Do not also use `Career/Experience/Offline-experience/` (same product; leave that folder on disk). Do not publish ranked job-title tables.

**Do not use:** any `*-engineer.md` packet; `Career/Job Listing.md`; University Transcripts; `Life/`.

## Content inventory → site section (pre-implementation map)

Counted 17 September 2026: **20 files** in **6 folders**. Keep originals in `Content/`. Upload copies to Storage.

| Content folder | Files | Proposed site section |
| --- | --- | --- |
| `Content/BariAccess NYC Biohacker Expo/` | `IMG_0869.jpeg`, `IMG_0869-app-logo.jpeg`, `IMG_0853.jpeg`, `IMG_0863.jpeg` (4 images) | TREI / BariAccess project story + NYC Biohacker Expo gallery |
| `Content/BariAccess Belgrade Serbia/` | `IMG_0302.jpeg`, `IMG_0416.jpeg`, `IMG_0384.jpeg`, `IMG_0521.JPG` (4 images); `IMG_0330.mov`, `IMG_0334.mov` (2 videos) | TREI / BariAccess project story + Belgrade / PROFEX gallery (must play on mobile) |
| `Content/Columbia University Graduation/` | `BBF77D5C-B9EB-4DF3-83BB-2E52823ADCB7.JPG`, `Lem 051925-60_Original.jpg`, `Lem 041525-247_Original.jpg`, `Lem 051625-186_Original.jpg`, `IMG_8342.JPEG` (5 images) | Education — Columbia |
| `Content/SLU Graduation/` | `IMG_2016.jpeg`, `FullSizeRender.JPG` (2 images) | Education — St. Lawrence |
| `Content/Berkshire School/` | `IMG_4528.jpeg` (1 image) | Education — Berkshire |
| `Content/Siloam Hope Presbyterian Church/` | `IMG_9099.jpeg`, `IMG_5587.jpeg` (2 images) | About / faith & community (from `Hobbies-Activities.md`) |

Existing site media to keep (already in `public/`, not in `Content/`):

- `public/images/headshot.jpg` — hero
- `public/images/resume.pdf` — resume panel

## Current site (working)

- `public/index.html` is the hosted page (Tailwind CDN + inline CSS). Sections: hero, stats, experience, personal projects, skills, school, PDF resume, contact.
- Experience: BariAccess/TREI (**current employment**, Jun 2025 – Present), FitGenius, City of Elizabeth intern, Columbia IDE intern.
- Projects: FITD, LaunchPage Studios / Alex Road Service, TaxTacker, Insightful Care, Local AI.
- Education: Columbia, St. Lawrence, James Cook. **No Berkshire.** **No galleries or video.**
- Contact: `mailto:` plus Google Apps Script POST. Preserve the endpoint; do not send mail from agents.
- Firebase Hosting already configured in `firebase.json` (`public` dir, SPA rewrite to `/index.html`). Identity: user `zakiymanigo@gmail.com`, project `zakiymanigo-career`. **Billing on** via Cloud Billing API (17 Sep 2026). MCP `get_environment` still printed `Billing Enabled: No` the same day — ignore that flag. No Storage block in `firebase.json`. No `storage.rules` in repo. No Firebase apps detected on the project. List API shows label `firebase/storage-default-bucket: created`.

## Owner decisions (17 September 2026)

Recorded in `ops/product-engineering/decisions/20260917-career-site-copy-conflicts.md`. Implementers follow these; do not re-open the old conflict list.

| Topic | Decision |
| --- | --- |
| GitHub on the public site | Link **both** `https://github.com/ztm2106` and `https://github.com/ASWDWWW` (hero, footer, contact). Git CLI/MCP for this repo stays **github-aswdwww**. Do not `gh auth switch`. |
| BariAccess dates | Use live page: **Jun 2025 – Present**. This is **current employment** (full-time Software Engineer, BariAccess · TREI). `00-OVERVIEW.md` and folder `README.md` updated. Keep the July–September 2026 git snapshot labeled as packet evidence only. |
| Football | Use `Berkshire School.md`: Sheffield, **MA**, Class of 2020, football **2016–2020**. `Football Career.md` rewritten. SLU football: two seasons (2020–2021) then Fall 2022 Australia, per the original football note aligned to the 3+2 calendar. |
| Tax Tracker | Public facts from `OVERVIEW.md` **Project snapshot** only. |
| Local AI folders | Site copy from **`Offline-Windows-Desktop-LLM-Client-experience` only**. Do not delete `Offline-experience/`. |

## Missing / leftover (not the resolved conflicts)

**Missing**

- Photo/video galleries and project-story layout that works on small screens.
- Firebase Storage bucket, rules, and public download URLs.
- Berkshire, church, Belgrade, and NYC expo on the public page.
- Video players for the two `.mov` files (iOS Safari often needs `playsinline`, poster image, and may not play HEVC/MOV — test; transcode only if needed and only as a derived file, do not delete the originals).

**Still conflicting / leftover (not owner-decided)**

- Root `css/style.css` is an unused starter sheet. `public/index.html` does not load it. Prefer editing `public/index.html` (and a new stylesheet under `public/` if split). Do not replace the live page with `css/style.css`. `index-safety.html` is a stale root backup — do not restore it as the live page.

**Outdated relative to this ticket**

- Live site has no `Content/` media.
- School section omits boarding school and 3+2 framing beyond three separate cards.

## Firebase Storage plan (implementation)

1. Stay on project `zakiymanigo-career` as `zakiymanigo@gmail.com`. Retry once on that identity only.
2. Add Storage on `zakiymanigo-career`. Billing is already on. **Do not** enable or swap a billing account. Optional if Storage still errors: keep working on HTML/CSS with local paths, record the gap, and do not pretend Storage is live.
3. If Storage can be created on Spark: write tight `storage.rules` so **only** the career-media prefix is publicly readable (images + the two videos). No listing of the whole bucket if it can be avoided. No writes from the public site.
4. Upload the 20 `Content/` files to a prefix such as `career-media/<folder>/<filename>`. Do not upload transcripts, Career markdown, or resume packets.
5. Put public download URLs in the redesigned page (or a small `public/` manifest the page reads). Do not commit secrets.
6. Adding Storage config to `firebase.json` is in scope. **Deploying** those rules is out of scope until authorized. If rules cannot take effect without deploy, implement files locally, note the gap, and still wire URLs if objects are already public via the Storage API.

## UI/UX requirements

- Desktop and mobile: sticky nav, galleries that do not overflow, tap-friendly controls, working `<video>` on phone.
- New or expanded surfaces: galleries (by folder), project stories (TREI as **current employment** + other products from allowed overviews), education (add Berkshire; keep Columbia / SLU / JCU; 3+2 as the dual-degree story), contact (keep form + email/LinkedIn/phone + **both GitHub profiles**).
- Do not dump intern-packet tone (“claim / do not claim”) onto the public page.
- Accessibility: captions/alt text from folder + Career notes; keyboard-reachable lightbox if used; do not autoplay video with sound.
- Do not add a new JS framework. Stay static HTML/CSS (Tailwind CDN already in use is fine).

## Preserve

- `Career/` including all job-title packets and transcripts (unpublished).
- `Content/` originals.
- `Resumes & Cover Letters/` including new folders and indexed deletions under `use/`.
- Existing internships on the experience section unless allowed notes contradict them (City of Elizabeth and Columbia IDE are on the site today and are **not** in `Career/Experience/` overviews — keep them).

## Acceptance checks

- [x] Ticket remains the source of truth; implementation happens only after Zakiy asks.
- [x] After implementation: `public/index.html` (and CSS if added) redesigned with galleries, project stories, education, contact.
- [x] All 20 `Content/` items mapped; none of the transcript PDFs or job-title packets published.
- [x] Public copy traced to the allowed files; ratings / do-not-claim omitted.
- [x] Firebase Storage objects exist **or** a non-billing blocker recorded; do not change the billing account.
- [x] Browser verification: desktop and ~390px-wide mobile; nav, galleries, both videos, education, contact form UI (submit to Apps Script is optional if it would send a real message — do not spam the endpoint).
- [x] No `firebase deploy`, no git commit, no account switch.
- [x] Control center updated when implementation starts and when it finishes.

## Verification notes

Implemented 17 September 2026. Local serve `http://localhost:8765/`. Storage bucket `zakiymanigo-career.firebasestorage.app`, 20/20 objects uploaded; sample HEAD 200. Browser: desktop lightbox used a Storage URL; both Belgrade videos loaded (durations 4.8s / 19.8s); mobile 390px hamburger + `#education` navigation. Contact form not submitted. Favicon 404 then pointed at headshot. Storage rules **not** deployed. Handoff: `ops/handoffs/20260917-career-site-refresh.md`. Media URLs: `ops/product-engineering/media-urls.json`. Independent review: no critical findings; copy/nav nits applied after review.

## Blockers

- Billing is **on** for `zakiymanigo-career` (Cloud Billing API). MCP `get_environment` still reports No; do not stop Storage work because of that flag. Do not change the billing account.
- Gmail MCP unauthenticated — irrelevant if contact form is unchanged.
- Two Belgrade `.mov` files: desktop Chrome played them; **iPhone/Safari not verified**. Originals stay in `Content/`.
- Gallery stills are full originals (some 8–12MB). Compress before a cellular-friendly deploy.

## Links

- Control center: `ops/CONTROL-CENTER.md`
- Routing: `ops/integrations/ROUTING.md`
- Sources of truth: `ops/architecture/SOURCES-OF-TRUTH.md`
- Live page (local): `public/index.html`
- Copy decisions: `ops/product-engineering/decisions/20260917-career-site-copy-conflicts.md`
- Handoff: `ops/handoffs/20260917-career-site-refresh.md`
- Media URLs: `ops/product-engineering/media-urls.json`
- Prior OS ticket: `ops/product-engineering/tickets/20260917-os-setup.md`

## Implement later with

`/complete-ticket` on this file, product **resume-web**, identity **github-aswdwww**. Sequential work on one agent. Verify with browser tools before status `done`.
