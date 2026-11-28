---
name: zelvior-security
description: Zelvior security subskill. Use for absolutely any request that involves, touches, or concerns security, vulnerability, vulnerabilities, auth, authentication, login, hardening, safety, protection, or defense — no matter the wording or register. Matches whether the user wants to secure, harden, lock down, protect, defend, guard, shield, fix, check, audit, review, scan for, assess, or fix up security; set up authentication, auth, login, sign-in, or access control; validate inputs, prevent attacks, or stop bad input; or find vulnerabilities, bugs, weak spots, holes, or risks — or says is this secure, secure this, secure the site, lock this down, lock it down, check my security, check security, how do I harden this, how do I secure this, help me secure the site, help me with security, is there a vulnerability, is this vulnerable, and anything even loosely like it. Part of zelvior-vibecoding-skill.
---

# Zelvior Security Subskill

Harden every response, route, and webhook. Read `../../references/06-security.md` for full detail.

## Headers (every response)

HSTS with preload, CSP without unsafe-inline on script-src and style-src, object-src 'none', base-uri restricted, frame-ancestors set, X-Frame-Options, X-Content-Type-Options nosniff, Referrer-Policy, Permissions-Policy, COOP, COEP, CORP, no wildcard CORS, no Server or X-Powered-By exposure, no public caching on sensitive paths, Secure HttpOnly SameSite cookies, no mixed content, no HTTP form posts, no HTTPS downgrade.

## Transport and DNS

HTTPS only, TLS 1.2 minimum, strong ciphers, 2048-bit keys, CAA records, DNSSEC, no dangling CNAMEs, two nameservers, SPF/DKIM/DMARC where email is sent.

## Application checks

XSS escaping, CSRF tokens plus SameSite, file upload validation by content, path traversal prevention, SSRF allow-lists, Argon2id passwords, strong JWT secrets, explicit CORS allow-lists, signed webhooks, rate limits, IDOR/BOLA authorization, server-side input validation, no exposed logs, no exposed source maps, no dangerous HTTP methods, no exposed config files, no directory listing, SRI on cross-origin assets, rel="noopener" on target="_blank", security.txt, favicon, manifest.

## Rules

- CSP script-src with unsafe-inline is a high-severity fail. Use nonces or hashes.
- Never expose source maps, logs, secrets, or stack traces.
- Never trust client-supplied IDs. Authorize every object server-side.
