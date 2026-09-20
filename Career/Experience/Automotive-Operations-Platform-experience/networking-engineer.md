# Networking Engineer

**Project:** Alex Road Service (LaunchPage Studios)  
**Evidence fit:** **1.4 / 10** · **Band:** Minimal / not a fit  
**How to use this in hiring:** Do not claim this project as experience for this title

> This score measures how strongly *this repository* maps to a typical **Networking Engineer** hiring bar. It is not years of experience, a compensation band, or a prediction that you would receive an offer.

## What this role is hired to do

Networking engineers design and operate networks: routing, switching, firewalls, DNS, VPN, load balancing, and packet-level troubleshooting.

## What you actually built

Alex Road Service is a production-shaped **marketing website plus internal shop operations platform** for a 24/7 commercial roadside and truck repair business in Keasbey, NJ. You were the **sole builder** from first commit (March 2026) through repo split (September 2026): public site, 20+ ops screens, Firebase Auth/Firestore/Functions/Storage/Hosting, Stripe Checkout with webhook-recorded payments and refunds, RBAC, encrypted staff messaging, VIN decode, i18n, CI/CD, security rules tests, runbooks, and a LaunchPage Studios closed-sales / delivery packet so the same platform can be duplicated for other shops.

## How that work maps to Networking Engineer

You set HTTP security headers, Hosting/CDN via Firebase, and CSP `connect-src` allowlists (including NHTSA and Google APIs). That is web security configuration, not networking engineering.

## Concrete evidence from this project

- CSP, HSTS, Referrer-Policy, Permissions-Policy on Hosting.
- Clean URLs / HTTPS by platform default.

## Gaps versus a typical hiring bar

No BGP, no firewall policy design, no packet captures. Minimal.

## How to talk about this

- Do not apply to Networking Engineer roles with this as evidence.

## Repo pointers

- `dev/firebase.json` headers
