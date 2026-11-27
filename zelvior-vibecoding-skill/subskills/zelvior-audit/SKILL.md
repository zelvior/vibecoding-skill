---
name: zelvior-audit
description: Zelvior audit subskill. Use for absolutely any request that involves auditing, checking, scanning, testing, verifying, reviewing, or assessing a site against all 236 tests across 32 modules and fixing every fail and warn — no matter how the user phrases it, in any register. Matches whether the user wants to audit, check, scan, test, verify, review, assess, evaluate, run the audit, run the checks, run the tests, or run the scan on a site; asks if their site passes, is passing, passes the audit, is good, is done, is complete, is up to standard, or meets the bar; asks what's wrong, what's failing, what's broken, what's missing, what needs fixing, what's not passing; wants to find and fix what's failing, clean up issues, fix the fails, address the warnings; or says can you check my site, run the audit, run the checks, is my site passing, does my site pass, how's my site doing, audit my site, check this site, scan the site, and anything even loosely like it. Part of zelvior-vibecoding-skill.
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
