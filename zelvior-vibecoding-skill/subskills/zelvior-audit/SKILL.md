---
name: zelvior-audit
description: Zelvior audit subskill. Use to audit, check, scan, test, verify, or review a site against all 236 tests across 32 modules and fix every fail and warn — whenever the user wants to audit, check, scan, test, verify, review, or run the audit on a site, asks if their site passes, is passing, is good, is done, or is complete, asks what's wrong, what's failing, what's broken, wants to find and fix what's failing, clean up issues, or "can you check my site / run the audit / is my site passing". Part of zelvior-vibecoding-skill.
---

# Zelvior Audit Subskill

Audit like Audityxe. Read `../../references/11-audit-checklist.md` for all 236 tests. Run `../../scripts/audit.py` for automated checks.

## Modules (32)

SEO, Performance, Security Headers, SSL/TLS, Email Authentication, Server Hardening, DNS Security, SRI and Link Safety, Trust Signals, Legal and Trust Pages, Content Quality, Accessibility, Mobile Responsiveness, UX/UI, Vibe-Coded Signals, Technical Stack, HTML Structure, Meta Tags, Sitemap and Robots, Structured Data, Broken Links, Image Optimization, Third-Party Scripts, Social Metadata, Monetization, Site Structure, Cookies and Redirects, AI Crawler Readiness, CRO, TTFB, Lighthouse, Real-User Experience (CrUX).

## Workflow

1. Run `python3 ../../scripts/audit.py <url-or-file>` and save the report.
2. Walk every checklist item in `../../references/11-audit-checklist.md`. Mark pass, warn, fail, or unverified.
3. Fix every fail first (high severity escalates its module to critical).
4. Fix every warn or document acceptance with a reason.
5. Re-run until zero fails and zero unaddressed warns.
6. Confirm Lighthouse 90+ in Performance, Accessibility, Best Practices, and SEO.

## Known high-severity fails to check first

CSP script-src with unsafe-inline, missing image alt text, broken internal links, no HTTPS, robots.txt blocking all crawlers, no responsive viewport, HTTPS to HTTP downgrade, zero CTAs.
