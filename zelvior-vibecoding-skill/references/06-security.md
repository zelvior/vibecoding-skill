# Security: Headers, Transport, DNS, and Application Checks

Apply every check. Every item is an audit test or a security requirement.

## Security headers (every response)

- Strict-Transport-Security: max-age=63072000 (2 years), includeSubDomains, preload. Eligible for hstspreload.org.
- HSTS includeSubDomains: set. HSTS preload-list eligibility: max-age at least 1 year plus includeSubDomains plus preload.
- Content-Security-Policy script-src: present WITHOUT unsafe-inline. This is the highest-severity header check. Use nonces or hashes for inline scripts. Never allow unsafe-inline on script-src.
- Content-Security-Policy style-src: present WITHOUT unsafe-inline. Use nonces or hashes. Lower severity than script-src but still required.
- CSP object-src: 'none'. Blocks legacy plugin content.
- CSP base-uri: restricted. Blocks base href injection.
- CSP frame-ancestors: set. Modern replacement for X-Frame-Options.
- X-Frame-Options: present.
- X-Content-Type-Options: nosniff.
- Referrer-Policy: privacy-conscious value (strict-origin-when-cross-origin or stricter).
- Permissions-Policy: present. Disable unused features.
- Cross-Origin-Opener-Policy: present.
- Cross-Origin-Embedder-Policy: present. Missing is a medium-severity warn.
- Cross-Origin-Resource-Policy: present.
- CORS configuration: no wildcard Access-Control-Allow-Origin on credentialed endpoints. Explicit allow-list.
- Server header exposure: do not reveal platform. Remove or genericize.
- X-Powered-By: never exposed. Remove it.
- Cache-Control on sensitive path: no public caching on sensitive paths. Private and no-store where needed.
- Cookie security: Secure, HttpOnly, SameSite on every cookie. Classify every cookie.
- Cookie classification: no unclassified cookies. No cookies on responses that do not need them.
- Mixed content: none. No HTTP resources on HTTPS pages.
- Form action security: no form submits over plain HTTP.
- HTTPS: site served over HTTPS. Redirect downgrade: no HTTPS to HTTP downgrade.
- Force HTTPS: HSTS with preload. HTTP redirects to HTTPS in one hop.

## SSL and TLS

- Certificate expiration: valid, monitored, auto-renewed. Alert at 30 days.
- Certificate issuer: trusted CA. Hostname and SAN match the domain.
- TLS protocol version: TLS 1.2 minimum, TLS 1.3 preferred. No SSLv3 or TLS 1.0/1.1.
- Cipher suite: strong modern ciphers only (TLS_AES_128_GCM_SHA256 and equivalents).
- Key strength: at least 2048 bits. ECDSA P-256 or RSA 2048 minimum.

## Email authentication

- SPF record: present where email is sent. No SPF means mail can be spoofed.
- DMARC policy: present where email is sent. Enforced (quarantine or reject), not just monitored.
- DKIM: present where email is sent. Check common selectors (default, google, selector1, selector2, k1, s1, mail) plus custom selectors.

## Server hardening

- Dangerous HTTP methods: TRACE, CONNECT, and other unsafe methods disabled.
- Exposed configuration files: block .env, .git, backups, and config files at the server.
- Directory listing: disabled everywhere.
- Exposed logs: never expose logs, debug endpoints, or stack traces. Error pages are generic.
- Exposed source maps: never ship .js.map files to production.
- Source map exposure: sampled scripts have no public .js.map files.

## DNS security

- CAA record: restricts which CAs can issue certificates. Missing means any public CA can issue.
- DNSSEC: enabled where the registrar supports it. Protects against cache poisoning and spoofing.
- Dangling CNAME and subdomain takeover: no dangling records. Remove stale DNS entries.
- Nameserver records: at least two nameservers for redundancy.
- SOA record: present.
- MX records: correct where email is received.

## Link and asset safety

- Script SRI: integrity hashes on cross-origin scripts.
- Stylesheet SRI: integrity hashes on cross-origin stylesheets.
- target="_blank" safety: every target="_blank" link includes rel="noopener".
- Vulnerability disclosure (security.txt): present with valid contact and expiry date.
- Favicon: resolves correctly. Web app manifest: linked and resolves. Safari pinned-tab icon: optional mask-icon.
- Apple touch icon and theme color declared for mobile.

## Application security checks

- XSS: escape all output. Sanitize rich text. Never use dangerouslySetInnerHTML with user data.
- CSRF: anti-CSRF tokens plus SameSite cookies on all state-changing requests.
- Insecure file uploads: validate type by content, not extension. Store outside web root. Scan and resize images. Limit size.
- Path traversal: never build file paths from user input without canonicalization and allow-listing.
- SSRF: allow-list outbound URLs. Block private IP ranges. Timeouts on every fetch.
- Weak password management: Argon2id hashing, minimum length, breach-list check, rate-limited login, MFA for sensitive accounts.
- Hashed passwords and secrets: Argon2id for passwords. Secrets in a vault, never in code, logs, or client bundles.
- JWT secrets: strong random secrets in a vault. Short expiry. Algorithm pinned, never none.
- Permissive CORS: explicit origin allow-list. Never reflect arbitrary origins with credentials.
- Unsigned webhooks: verify signatures on every webhook. Reject unsigned or replayed events. Timestamps plus nonce.
- Rate limits: on auth, forms, APIs, and webhooks. Return 429 with Retry-After.
- IDOR and BOLA: authorize every object access server-side. Never trust client-supplied IDs.
- User input validation: validate and sanitize every input server-side. Allow-list, never deny-list.
- SQL injection protection: parameterized queries only. Never string-concatenate SQL.
- Bot protection: rate limits, honeypots, challenge only on detected abuse. Never block real users.
- Session expirations: short access tokens, rotating refresh tokens, absolute session lifetime, server-side revocation.
- Kill switch: global and per-feature switches without a deploy.
- GPC (Global Privacy Control): respect Sec-GPC server-side. Treat as opt-out of sale and sharing.
