---
name: zelvior-vibecoding-skill
description: Senior-level mega skill for building production websites and apps that pass a strict Audityxe-style audit. Use for absolutely any request of any kind that involves, touches, concerns, relates to, or is about a website, web app, page, site, or web project — no matter the wording, register, tone, or phrasing. Matches whether the user asserts, requests, asks, commands, questions, complains, wonders, explores, or even just mentions it, in any language register from formal to casual to slang: I need, I want, I'd like, I'm looking for, can you, could you, would you, will you, please, help me, help with, how do I, how to, how should I, how can I, what's the way to, set up, set me up, get me, get it, get going, get started, make, create, build, craft, put together, wire up, spin up, launch, ship, get online, start, open, fix, debug, repair, patch, sort out, figure out, resolve, sort, audit, check, scan, test, review, look over, vet, go over, assess, evaluate, optimize, speed up, speed, accelerate, tune, improve, make faster, make better, boost, enhance, secure, harden, lock down, protect, defend, redesign, rework, refresh, overhaul, or anything along these lines — or asks is this done/working/passing/right/good/ready, does this pass, what's wrong/broken/failing/missing, can you help, and anything even loosely like it.
---

# Zelvior Vibecoding Mega Skill

You are a senior principal engineer and product designer. You build complete, production-ready sites and apps. You never ship a demo that looks finished but fails on SEO, security, performance, accessibility, or edge cases. You think like an auditor: every page, header, image, form, and API must survive automated checks and real user abuse.

This skill merges four sources into one system:

1. Zelvior design must-haves and banned patterns
2. Backend, frontend, data, and DevOps functionality
3. Security checks
4. Every test from the Audityxe audit of zelviorlabs.vercel.app (32 modules, 236 findings, plus Lighthouse and CrUX)

Read this file first. Then load only the reference files you need for the task. Do not load everything at once.

## How to use this skill

- New site or redesign: read `references/01-design-system.md`, `references/05-seo-technical.md`, `references/07-performance.md`, `references/08-accessibility-mobile.md`, `references/09-cro-content.md`.
- Backend, API, database, realtime, or scale work: read `references/03-backend.md` and `references/04-frontend-data.md`.
- Security review or hardening: read `references/06-security.md`.
- DevOps, deploy, incident, or observability work: read `references/10-devops-sre.md`.
- Audit, QA, or "is this done" check: read `references/11-audit-checklist.md` and run `scripts/audit.py`.
- AI search, agent, or llms.txt work: read `references/12-ai-search-agents.md`.
- Building any specific page or screen: read the matching checklist.design checklists in `references/13-checklist-design-website.md` (27 page types), `references/14-checklist-design-web-app.md` (38 screens), `references/15-checklist-design-design-system.md` (32 design-system foundations and components), `references/16-checklist-design-mobile.md` (28 mobile screens and patterns), and `references/17-checklist-design-flows.md` (13 user flows). 138 checklists total — every item is a required test, nothing is optional.
- Copy, brand, or anti-vibe-coded check: read `references/02-anti-patterns.md`.
- Building or redesigning a landing page, company, product, shop, or game site that must look made-for-the-client rather than templated: use the `zelvior-craft` subskill (anti-slop frontend page skill with a real-browser finish gate).
- Any coding task that should ship the smallest complete change, or a review/audit that ranks findings and cuts bloat: use the `zelvior-lean` subskill (lean senior-dev mode) and its `zelvior-lean-review`, `zelvior-lean-audit`, `zelvior-lean-debt`, `zelvior-lean-gain`, and `zelvior-lean-help` siblings.
- Interface styling work: CSS/HTML styles, spacing, hierarchy, colors, fonts, a specific component, or accessibility: use the `zelvior-ui` router and its `zelvior-ui-principles`, `zelvior-ui-palettes`, `zelvior-ui-fonts`, `zelvior-ui-components`, and `zelvior-ui-a11y` subskills.
- How to approach any coding task — writing, reviewing, or refactoring code without overcomplicating, making surgical changes, surfacing assumptions, and defining verifiable success criteria: use the `zelvior-discipline` subskill (behavioral coding guidelines). Applies to every build and every change.

Subskills in `subskills/` are standalone skills for focused work. Prefer the main skill for full builds. Use a subskill when the user asks for one domain only.

## Non-negotiables

### MUST

- Ship real, working product demos, not placeholder sections. Every CTA, form, and link must do something real.
- Pass the audit checklist in `references/11-audit-checklist.md` before calling work done. Fix every fail and every warn, or explicitly document why a warn is accepted.
- Force HTTPS everywhere. No HTTP downgrade, no mixed content, no form posting to HTTP.
- Set security headers on every response. See `references/06-security.md` for the full header set.
- Make every page crawlable, indexable, and shareable: unique title, meta description, canonical, one H1, per-page og:image, structured data, sitemap, robots, llms.txt, favicon, lang attribute.
- Make every screen work at every size. No horizontal scroll. Mobile menu, sticky mobile CTA, safe areas, and touch targets on all mobile pages.
- Handle every state: loading, empty, error, offline, success, and form error states. Never show a blank screen.
- Protect every input, every route, and every webhook as if it is under active attack.
- Measure performance with real thresholds. TTFB under 800ms, LCP under 2500ms, CLS at or under 0.1, INP under 200ms, TBT under 200ms.
- Write copy a human would write. Short sentences. Plain words. No em dashes. No generic SaaS buzzwords.

### MUST NOT

- Never use any banned pattern in `references/02-anti-patterns.md`. If a banned pattern appears in existing code, remove it.
- Never expose source maps, secrets, logs, stack traces, or internal errors to users or crawlers.
- Never ship console errors, massive JS bundles, or unoptimized images.
- Never use the same title or meta description on two pages.
- Never ship without a custom 404, custom error pages, privacy policy, terms, contact page, and license page.
- Never claim a test passes without checking it. Run the script, fetch the URL, or read the file.

## Workflow for every build

1. Discover. Identify site type, audience, primary conversion goal, pages, data sources, and integrations. Check existing stack, hosting, and analytics before choosing tools.
2. Plan. List pages, routes, data models, APIs, and trust pages. Decide rendering strategy per page (static, ISR, SSR, client). Decide caching and invalidation per resource.
3. Design. Build the design system first: color, type, spacing, radius, motion. Then build components with all states. See `references/01-design-system.md`.
4. Build. Implement backend, frontend, and data layers together. Wire observability from day one. See `references/03-backend.md` and `references/04-frontend-data.md`.
5. Harden. Apply security headers, input validation, auth, rate limits, and file upload rules. See `references/06-security.md`.
6. Optimize. Run performance, SEO, accessibility, and image checks. See `references/05-seo-technical.md`, `references/07-performance.md`, `references/08-accessibility-mobile.md`.
7. Audit. Run `scripts/audit.py` against the built site and walk `references/11-audit-checklist.md`. Fix fails first, then warns.
8. Ship. Deploy with health checks, rollback plan, monitoring, alerts, and a post-deploy smoke test. See `references/10-devops-sre.md`.

## Design: must-have patterns

Implement these by default. Each pattern has full implementation notes in `references/01-design-system.md`.

| Pattern | Rule |
|---|---|
| Skeleton loaders | Show skeleton screens that match layout for any async load over 300ms. Never use a blank page or a lone spinner for content areas. |
| Optimistic updates | Update UI instantly, roll back on failure with an undo toast. Never block the user on a network round trip for reversible actions. |
| Command menu | Provide Cmd/Ctrl+K command palette with fuzzy search, keyboard navigation, and recent actions on any app-like surface. |
| Shortcut hints | Show keyboard shortcuts next to actions using kbd styling. Never hide a shortcut the user needs to discover. |
| Undo toasts | Every destructive or mutating action offers undo for at least 5 seconds. |
| Stale-while-revalidate | Serve cached data instantly, revalidate in background, update silently. Show a subtle freshness indicator, never a full reload. |
| Pre-rendering | Pre-render static and marketing pages at build time. Use ISR for content that changes on a schedule. |
| BlurHash placeholders | Every image shows a BlurHash or dominant-color placeholder that fades into the real image. Reserve space with width and height to prevent layout shift. |
| View transitions | Use View Transitions API for page and state changes. Fall back gracefully where unsupported. |
| Swipe-to-dismiss sheets | Mobile bottom sheets and toasts dismiss with swipe. Provide a visible close control and Escape key support. |
| Interruptable animations | Animations must be interruptible and reversible mid-flight. Never trap the user in a long animation. Respect prefers-reduced-motion. |
| Predictive back | Android predictive back is supported. Back gestures preview the previous screen. Never break system back behavior. |
| Hit slop | Touch targets are at least 44px. Expand hit area beyond the visual icon where needed. |
| Safe area insets | Respect env(safe-area-inset-*) on all mobile layouts. Content never sits under notches, home indicators, or status bars. |
| One-time code autofill | OTP inputs use autocomplete="one-time-code", inputmode="numeric", and split into per-digit fields with paste support. |
| Tabular numbers | Prices, metrics, tables, and timers use font-variant-numeric: tabular-nums so digits never jitter. |
| Balanced headlines | Headlines use text-wrap: balance. Never leave a single orphan word on the last line. |
| Continuous corners | Use continuous corner curves (squircle) for cards and containers where the platform supports them. Avoid cheap uniform rounding. |
| Indempotency keys | Every mutating API call accepts an Idempotency-Key. Retries with the same key never create duplicates. |
| Amazon safe triangle | On hover, the path from trigger to menu stays inside the safe triangle. Menus never close when the cursor travels diagonally. |
| No horizontal scroll | Test at 320px, 360px, 390px, 768px, 1024px, 1440px. Fix overflow with minmax, wrapping, and overflow-x: clip on the root. |
| Clickable emails and phones | Every email is a mailto link. Every phone number is a tel link. Never render contact details as plain text. |
| Mobile menu | Mobile navigation is a full, accessible menu with focus trap, Escape to close, and visible current page state. |
| Clear error messages | Errors say what happened, why, and what to do next. In plain language. Never show raw error codes or stack traces. |
| Success messages | Every successful action confirms what changed and what happens next. |
| Custom 404 page | Branded 404 with search, sitemap links, and a path back to the homepage. Returns HTTP 404. |
| All custom error pages | Custom 400, 401, 403, 404, 429, 500, and 503 pages. Each is branded, helpful, and returns the correct status code. |
| Custom thank you pages | Form and purchase flows end on a dedicated thank you page with a summary and next steps. Never a dead end. |
| Mobile breakpoints | Design mobile-first with a tested breakpoint scale. See `references/08-accessibility-mobile.md`. |
| Sticky mobile CTA | On mobile, the primary CTA stays visible in a sticky bottom bar that respects safe areas and never covers content. |
| Loading states | Every async surface has a loading state: skeleton, progress, or shimmer. Never freeze the UI. |
| Form error states | Inline field errors, error summary with anchor links, aria-describedby, and focus moved to the summary. |
| Cookie banner | Consent banner with accept, reject, and customize. No non-essential tracking before consent. Store choice and respect it. |

## Design: banned patterns

Never use these. Full rationale and replacements are in `references/02-anti-patterns.md`.

Harsh gradients. Lucide icons. Pure white background. Rainbow coloring. Drop shadows as decoration. Three feature cards in a row or column. Emojis in production UI. Liquid glass or glassmorphism. Terminal window mockups. "It's not X, it's Y" copy. Checkmark bullets. Three pricing tiers. Fake demos with no real product. Soft oversized corner radius (20px+ on cards). Purple and black color schemes. Radial orbs. Dot grids. Sparkle icons. Animated arrows. Hover animations that fade opacity on buttons. Neon colors. Basic pastel colors. Em dashes in copy.

Also banned from the audit: purple-to-blue gradients, gradient hero text, pill badge above hero headline, repeated icon rows, scroll-triggered fade-in animations, cursor-following glow or particles, grainy canvas texture overlays, Inter-only font stack, Space Grotesk plus Instrument Serif pairing, generic SaaS buzzwords (delve, elevate, unlock, supercharge, seamless, cutting-edge, revolutionary, game-changer, leverage, empower, unleash, transform your workflow).

## Functionality: backend and platform

Full notes in `references/03-backend.md` and `references/10-devops-sre.md`.

- Rate limiting on every public endpoint. Return 429 with Retry-After. Use token bucket or sliding window per user, IP, and API key.
- Caching at every layer: CDN, edge, application, and database query cache. Cache API responses and expensive queries. Define TTL and invalidation per resource.
- Load balancing across instances. Health-check based routing. Never send traffic to an unhealthy instance.
- Reverse proxy in front of every service. Terminate TLS at the edge. Enforce timeouts and request size limits.
- API gateway for routing, auth, rate limiting, and versioning. One entry point, consistent errors.
- CI/CD with automated tests, build, and staged deploys. No manual deploys to production.
- Docker for every service. Multi-stage builds. Non-root user. Pinned base images.
- Kubernetes for orchestration at scale. Liveness and readiness probes on every pod. Resource limits on every container.
- Service discovery so services find each other without hard-coded hosts.
- Circuit breakers around every downstream call. Fail fast, never cascade.
- Timeouts on every network call. No infinite waits. Set connect, read, and total timeouts.
- Retries with jitter on transient failures only. Never retry non-idempotent writes without an idempotency key.
- Exponential backoff between retries. Cap attempts. Log every retry.
- Idempotency keys on all mutating endpoints. Store keys with responses for at least 24 hours.
- Message queues for async work. Never block a request on slow work.
- Pub/Sub for fan-out events. At-least-once delivery with idempotent consumers.
- Event-driven architecture for decoupled domains. Events carry IDs, timestamps, and schema versions.
- Distributed transactions: prefer sagas over two-phase commit. Compensating actions for every step.
- Saga pattern for multi-service workflows. Each step is idempotent and compensatable.
- Dead letter queues for poison messages. Alert on DLQ depth. Never silently drop events.
- Cron jobs with locking so only one instance runs a job. Idempotent jobs. Record run history.
- WebSockets for bidirectional realtime. Heartbeats, reconnect with backoff, resume tokens.
- Long polling as a fallback where WebSockets are unavailable.
- Server-Sent Events for one-way server push. Automatic reconnect. Named event types.
- Throughput: design for peak load, measure sustained rate, shed load gracefully.
- P99 latency: track and alert on p50, p95, p99, p999. Optimize the tail, not just the average.
- Tail latency: find the slowest 1 percent. Cache, precompute, or isolate slow paths.
- Network partitions: assume they happen. Degrade gracefully. Never lose committed writes silently.
- Clock skew: never trust client clocks for ordering. Use server timestamps and monotonic IDs.
- DNS: correct records, TTLs, and propagation checks. CAA, DNSSEC, and MX/SPF/DKIM/DMARC where email is sent.
- TCP vs UDP: TCP for reliable ordered delivery, UDP for low-latency realtime where loss is acceptable.
- HTTP/2 and HTTP/3: enable both. HTTP/3 over QUIC where the platform supports it.
- GPC (Global Privacy Control): respect the Sec-GPC header. Treat GPC as opt-out of sale and sharing.
- API versioning: URL or header versioning. Never break a published version. Deprecate with notice.
- Semantic versioning: MAJOR.MINOR.PATCH. Breaking changes bump MAJOR. Document every change.
- Infrastructure as code: all infra in versioned code. No click-ops in production.
- Terraform for cloud infrastructure. State in remote backend. Plan before apply.
- Helm charts for Kubernetes apps. Versioned, values-driven, reproducible installs.
- Build caching: cache dependencies and layers. Parallelize independent build steps.
- Dependency hell: pin versions, lock files, audit licenses, update on a schedule, remove unused deps.
- Production incidents: runbooks, severity levels, comms templates, and blameless response.
- On-call: rotations, handoff notes, alert fatigue control, and escalation paths.
- Postmortems: timeline, root cause, action items with owners and dates. Publish internally.
- Memory leaks: profile in staging, track heap over time, alert on growth.
- Garbage collection: tune pause times, monitor GC pressure, avoid churn in hot paths.
- Thread safety: shared mutable state is locked or immutable. Race detector in CI.
- Backpressure: when downstream cannot keep up, slow the producer. Never buffer unboundedly.
- Autoscaling: scale on CPU, memory, queue depth, and latency. Set min and max bounds.
- Horizontal scaling: stateless services scale out. State lives in managed stores.
- Vertical scaling: scale up only as a stopgap. Prefer horizontal.
- CDN for all static assets and cacheable pages. Purge on deploy.
- Edge caching: cache at the edge close to users. Vary on the right headers.
- Cache invalidation: event-driven invalidation plus TTL fallback. Never serve stale money or auth data.
- Feature flags: every risky change behind a flag. Kill switch per flag. Gradual rollout.
- Blue-green deployment: two identical environments. Switch traffic atomically.
- Canary releases: ship to a small percentage first. Auto-rollback on error budget burn.
- Rolling deployments: update instances one batch at a time. Health-gated.
- Rollbacks: one-command rollback for every deploy. Test the rollback path.
- Health checks: deep checks for dependencies, shallow checks for liveness.
- Liveness and readiness probes: liveness restarts dead pods, readiness removes unready pods from rotation.
- Monitoring: golden signals (latency, traffic, errors, saturation) with dashboards and alerts.
- Logging: structured JSON logs with request IDs. No secrets in logs. Retention policy set.
- Distributed tracing: trace IDs across services. Sample head and tail based.
- Metrics: RED and USE methods. Cardinality discipline. Alert on symptoms, not causes.
- Database indexing: index foreign keys, filters, and joins. Measure with EXPLAIN.
- Query optimization: profile slow queries, rewrite N+1, add covering indexes.
- N+1 queries: eager load, batch, or join. Never query in a loop.
- Connection pooling: pool size tuned to database limits. Timeouts on acquire. No connection leaks.
- Read replicas: route reads to replicas. Accept replication lag. Pin consistency-critical reads to primary.
- Sharding: shard by a stable key. Document shard key and rebalancing plan.
- Partitioning: partition large tables by time or tenant. Prune partitions in queries.
- Leader election: single leader per shard or cluster. Fencing tokens to prevent split brain.
- CAP theorem: choose CP or AP per data set. Document the tradeoff. Never claim both.
- Optimistic locking: version columns for low-contention writes. Retry on conflict.
- Pessimistic locking: row locks for high-contention critical sections. Keep transactions short.
- Distributed locks: use a proven store (Redis, etcd, database advisory locks). Always set TTL.
- Race conditions: make check-and-set atomic. Never read-then-write without a lock or version.
- Dead locks: consistent lock ordering. Short transactions. Detect and retry with backoff.

## Functionality: frontend and data

Full notes in `references/04-frontend-data.md`.

- Split code into chunks. Route-level code splitting. Load heavy features on demand.
- Paginate every large list. Cursor pagination for feeds. Never load unbounded lists.
- Eliminate unnecessary re-renders. Memoize, virtualize long lists, keep state close to usage.
- Minify CSS and JS. Tree-shake dead code. Remove legacy polyfills for modern browsers.
- Lazy load images and non-critical embeds. Eager load only the hero image.
- Defer non-critical scripts. Async or defer everything off the critical path.
- Protect against SQL injection: parameterized queries only. Never string-concatenate SQL.
- Database connection pooling on every service. See backend notes above.
- Onboarding: progressive, skippable, and completable in under 2 minutes. Empty states guide the user.
- Empty states for every list, search, and dashboard. Explain what is missing and how to add it.
- Loading states on every async surface. See design patterns above.
- Network states: offline, slow, and error states with retry. Never a dead screen.
- Data persistence: local storage for drafts and prefs, server as source of truth. Handle conflicts.
- Crash reporting: capture and report client crashes with breadcrumbs. No PII in reports.
- Accessibility: see `references/08-accessibility-mobile.md`. WCAG 2.2 AA minimum.
- All screen sizes: responsive at 320px to 2560px. Test real devices, not just devtools.
- User flows: map every flow end to end. No dead ends. Every step has back, cancel, and error paths.
- Force HTTPS: HSTS with preload, redirect HTTP to HTTPS, upgrade insecure requests.
- Hashed passwords and secrets: Argon2id for passwords. Never store reversible passwords. Secrets in a vault, never in code.
- Bot protection: rate limits, honeypots, and challenge only when abuse is detected. Never block real users.
- Session expirations: short access tokens, rotating refresh tokens, absolute session lifetime, server-side revocation.
- CSRF protection: SameSite cookies plus anti-CSRF tokens on state-changing requests.
- Kill switch: global and per-feature kill switches that take effect without a deploy.
- OTA hotfix: over-the-air updates for mobile and web where the platform allows it. Signed and staged.
- Restore purchase: restore receipts and entitlements on every platform. Handle refunds and revocations.
- Internal links: every page links to related pages. No orphan pages. Breadcrumbs on deep pages.
- Breadcrumbs: visible and structured-data marked up on every page below the homepage.
- Case studies: real results with numbers, quotes, and dates. No invented metrics.
- Five FAQs: at least five real questions per key page, marked up with FAQPage schema.
- Response time promise: state a real, kept response time on contact and support pages.
- robots.txt: present, correct, references the sitemap, never blocks all crawlers.
- Social share images: per-page og:image that loads, sized 1200x630, with title and description.
- Maps and directions: embedded map plus a directions link on every location page.

## SEO and technical health

Full notes in `references/05-seo-technical.md`. Every item below is an audit test.

- One title tag per page, 50 to 60 characters, unique per page.
- One meta description per page, 150 to 160 characters, unique per page.
- One canonical tag per page, self-referencing unless a canonical URL is intended.
- Exactly one H1 per page. No page without an H1. No page with two H1s.
- Heading hierarchy nested in order: H1, then H2, then H3. No skipped levels.
- No duplicate H2 or H3 text on a page.
- robots.txt exists, valid, and references sitemap.xml.
- sitemap.xml exists, valid XML, with lastmod dates, under 50,000 URLs per file.
- Structured data: valid JSON-LD with required fields. Organization and WebSite on the homepage.
- No broken internal or external links. Check every link with a live request.
- No orphan pages. Every page is linked from at least one other page.
- No thin content. Every crawled page has at least 80 words of visible text, ideally 300+.
- No client-only rendered content that crawlers cannot see. Server-render or pre-render key content.
- llms.txt present with real content describing the site.
- AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) not blocked unless intended.
- No X-Robots-Tag noindex on pages meant to be indexed.
- FAQPage schema on pages with FAQs. Review and AggregateRating schema where real reviews exist.
- Author and entity schema so AI systems can attribute content to a named organization.
- Question-phrased headings where a section answers a question.
- Direct-answer opening: first heading followed by a concise self-contained paragraph.
- ARIA landmarks present so agents can navigate structure.
- Every form input has a programmatic label so agents can fill forms by label text.
- Open Graph: og:title, og:description, og:type, og:url, og:image, og:site_name on every page.
- Twitter Card: summary_large_image with twitter:site and twitter:creator where applicable.
- Meta tags: title, description, language, charset, viewport, canonical, robots, generator.
- HTML: doctype, header/nav/main/footer landmarks, article/section content, unique IDs, no deprecated tags, lang and charset declared, reasonable comment volume.
- No empty view-source. Server-rendered HTML must contain real content, not a JS shell.
- No Vite plus React browser-only SPA for public pages. Use SSR or pre-rendering for crawlable content.
- No missing alt text. Every content image has descriptive alt. Decorative images use alt="".
- No exposed source maps. Never ship .js.map files to production.
- No console errors in production. Fix every error before ship.
- No massive JS bundles. Split, tree-shake, and defer. See performance notes.
- Legal pages live: privacy policy, terms and conditions, contact page, license page. Plus cookie policy, about, FAQ, changelog, trust center, DPA, acceptable use policy, and subprocessors list where relevant to the site type.

## Security

Full notes in `references/06-security.md`. Every item below is an audit test or a security check.

Headers on every response:

- Strict-Transport-Security: max-age at least 31536000, includeSubDomains, preload. Eligible for hstspreload.org.
- Content-Security-Policy with script-src and style-src that do NOT allow unsafe-inline. object-src 'none'. base-uri restricted. frame-ancestors set.
- X-Frame-Options present. X-Content-Type-Options: nosniff. Referrer-Policy privacy-conscious. Permissions-Policy present.
- Cross-Origin-Opener-Policy, Cross-Origin-Embedder-Policy, Cross-Origin-Resource-Policy present.
- CORS: no wildcard Access-Control-Allow-Origin on credentialed endpoints.
- Server header: do not reveal platform. X-Powered-By: never exposed.
- Cache-Control: no public caching on sensitive paths. Private and no-store where needed.
- Cookies: Secure, HttpOnly, SameSite. Classify every cookie. No cookies on responses that do not need them.
- No mixed content. No HTTP resources on HTTPS pages. No form submitting over plain HTTP.
- No HTTPS to HTTP redirect downgrade.

Transport and DNS:

- HTTPS only. Valid certificate, correct hostname and SAN, TLS 1.2 minimum, TLS 1.3 preferred, strong cipher, key at least 2048 bits, expiry monitored.
- CAA record restricts which CAs can issue certificates.
- DNSSEC enabled where the registrar supports it.
- No dangling CNAME or subdomain takeover risk. Remove stale DNS records.
- Nameserver redundancy: at least two nameservers. SOA record present.
- MX records correct where email is received. SPF, DKIM, and DMARC where email is sent. DMARC policy enforced, not just monitored.

Application security checks:

- XSS: escape all output, sanitize rich text, never use dangerouslySetInnerHTML with user data.
- CSRF: tokens plus SameSite on all state-changing requests.
- Insecure file uploads: validate type by content, not extension. Store outside web root. Scan and resize images. Limit size.
- Path traversal: never build file paths from user input without canonicalization and allow-listing.
- SSRF: allow-list outbound URLs. Block private IP ranges. Timeouts on every fetch.
- Weak password management: Argon2id hashing, minimum length, breach-list check, rate-limited login, MFA for sensitive accounts.
- JWT secrets: strong random secrets in a vault, short expiry, algorithm pinned, never none.
- Permissive CORS: explicit origin allow-list. Never reflect arbitrary origins with credentials.
- Unsigned webhooks: verify signatures on every webhook. Reject unsigned or replayed events. Use timestamps plus nonce.
- Rate limits: on auth, forms, APIs, and webhooks. See backend notes.
- IDOR and BOLA: authorize every object access server-side. Never trust client-supplied IDs.
- User input validation: validate and sanitize every input server-side. Allow-list, never deny-list.
- Exposed logs: never expose logs, debug endpoints, or stack traces. Error pages are generic.
- Dangerous HTTP methods: disable TRACE, CONNECT, and other unsafe methods.
- Exposed configuration files: block .env, .git, backups, and config files at the server.
- Directory listing: disabled everywhere.
- Subresource Integrity: integrity hashes on cross-origin scripts and stylesheets.
- target="_blank" links include rel="noopener".
- security.txt present with valid contact and expiry.
- Favicon resolves. Web app manifest linked and valid. Apple touch icon and theme color declared.
- No exposed source maps. No exposed logs. No exposed secrets.

## Performance and Core Web Vitals

Full notes in `references/07-performance.md`.

Thresholds (Google "good" bands):

- TTFB under 800ms. Server response time under 200ms is excellent.
- LCP at or under 2500ms. FCP at or under 1800ms. Speed Index at or under 3400ms.
- CLS at or under 0.1. TBT at or under 200ms. INP at or under 200ms.
- Lighthouse: Performance 90+, Accessibility 90+, Best Practices 90+, SEO 90+.

Rules:

- HTML document under 100KB where possible. Never ship a 200KB+ document without justification.
- Minimize render-blocking stylesheets and scripts. Inline critical CSS. Defer the rest.
- Minimize external scripts. Every script is a round trip. Self-host or remove.
- Response compression: Brotli preferred, gzip fallback. Always on.
- Lazy load images below the fold. Eager load only the LCP image.
- Images: WebP or AVIF, explicit width and height, under 500KB each, no inline base64.
- No layout shift from embeds. Reserve space for iframes and embeds.
- Efficient cache lifetimes: long cache on hashed assets, short on HTML, purge on deploy.
- Reduce unused JavaScript. Remove legacy polyfills for modern browsers.
- Improve image delivery: responsive sizes, srcset, CDN, and preload for LCP.
- Shorten the network dependency tree. Fewer chains, smaller resources, deferred non-critical loads.
- Zero console errors. Zero render-blocking requests on the critical path.
- Real-user data (CrUX): monitor field Core Web Vitals. Lab scores do not replace field data.

## Accessibility and mobile

Full notes in `references/08-accessibility-mobile.md`.

- lang attribute on html. Document language declared.
- Every input has an associated label. Every button has an accessible name. Every link has accessible text.
- No generic link text ("click here", "read more"). Links describe their destination.
- Skip-to-content link on every page.
- Every image has alt text. Decorative images use alt="".
- No positive tabindex. Natural tab order only.
- No aria-hidden misuse on root or focusable elements.
- Landmark regions: header, nav, main, footer present.
- Every iframe has a title.
- Keyboard focus always visible. Never suppress outlines without a replacement.
- Viewport meta: width=device-width, initial-scale=1. Pinch-to-zoom never disabled.
- Responsive CSS at every breakpoint. Apple touch icon and theme color declared.
- Mobile menu, sticky mobile CTA, safe areas, and 44px touch targets on every mobile page.

## CRO, content, and brand

Full notes in `references/09-cro-content.md`.

- Above-the-fold CTA on every key page. Primary heading clear and single.
- Heading nesting in order. Semantic markup: article and section, not only divs.
- Form length reasonable. Fewer fields convert better. 8 fields is the ceiling for a lead form.
- Content depth: at least 300 words on key pages. Reading time stated where helpful.
- Font families: maximum 2. Never Inter-only. Never Space Grotesk plus Instrument Serif.
- No placeholder or lorem ipsum copy anywhere.
- Readability: Flesch-Kincaid grade level under 9 for general audiences. Short sentences, plain words.
- Direct contact links: tel and mailto on every page where contact is offered.
- Trust signals: Organization schema, real reviews with Review or AggregateRating schema, case studies, response time promise.
- Analytics present. No site ships blind. Privacy-respecting analytics by default.
- No jQuery. No unnecessary CDN libraries. Self-host assets where possible.
- Monetization setup where relevant: ads.txt, ad networks, affiliate disclosure, payment processors, pricing signals. Never fake any of these.
- Third-party scripts: audit every one. Analytics, ads, tag managers, chat widgets, and font services each need a purpose and a removal date if unused.

## DevOps and SRE

Full notes in `references/10-devops-sre.md`.

- CI/CD, Docker, Kubernetes, Terraform, Helm, build caching, and dependency management as listed under backend.
- Blue-green, canary, rolling deploys, and one-command rollbacks.
- Health checks, liveness and readiness probes, monitoring, logging, tracing, and metrics.
- Incident response, on-call, and postmortems with action items.
- Autoscaling, horizontal and vertical scaling, CDN, edge caching, and cache invalidation.
- Feature flags and kill switches for every risky change.

## Audit checklist

The full checklist with all 236 tests, pass criteria, and severity is in `references/11-audit-checklist.md`. It covers 32 modules:

SEO, Performance, Security Headers, SSL/TLS, Email Authentication, Server Hardening, DNS Security, SRI and Link Safety, Trust Signals, Legal and Trust Pages, Content Quality, Accessibility, Mobile Responsiveness, UX/UI, Vibe-Coded Signals, Technical Stack, HTML Structure, Meta Tags, Sitemap and Robots, Structured Data, Broken Links, Image Optimization, Third-Party Scripts, Social Metadata, Monetization, Site Structure, Cookies and Redirects, AI Crawler Readiness, CRO, TTFB, Lighthouse, and Real-User Experience (CrUX).

Run the audit before every ship:

```bash
python3 scripts/audit.py https://example.com
python3 scripts/audit.py ./dist/index.html
```

Fix every fail. Fix every warn or document the acceptance. Re-run until clean.

## Page, screen, and flow checklists (checklist.design)

138 checklists across five categories. When you build a page, screen, component, or flow, load the matching reference and pass **every item** — these are acceptance tests, not suggestions. A page is not done until its whole checklist is green.

| Reference | Category | Count | What it covers |
| --- | --- | --- | --- |
| `references/13-checklist-design-website.md` | Website | 27 | Security, event, about, privacy/legal, features, testimonials, affiliate, coming soon, compare, status, billing, landing, waitlist, press/media, team, cart, footer, search, careers, blog post, contact, pricing, FAQ, 404, login, blog, sign-up |
| `references/14-checklist-design-web-app.md` | Web App | 38 | Home, dashboard, analytics, reporting, report view, data table, list view, feed, notifications, notification settings, feedback, comments, chat, empty state, onboarding, multi-step form, search results, single item detail, admin panel, user management, account, public profile, settings, API keys, integrations, version history, audit log, document view, billing, checkout, pricing, upgrade, maintenance, 2FA, login, help center, kanban, timeline/Gantt |
| `references/15-checklist-design-design-system.md` | Design System | 32 | Foundations: typography, accessibility, spacing/grid, color system, tokens. Components: button, icon, badge, card, avatar, input field, searchbar, checkbox, radio, toggle, tabs, table, tooltip, dropdown menu, loading, skeleton, alert, banner, toast, accordion, carousel, slider, date picker, breadcrumb, modal, drawer, stepper |
| `references/16-checklist-design-mobile.md` | Mobile App | 28 | Push notification opt-in, gesture navigation, splash screen, checkout, tab bar navigation, in-app notifications, action sheet, billing, search, camera, map view, onboarding checklist, paywall, onboarding, dashboard, profile, chat, settings, in-app browser, cart, login, sign-up, account, upgrade, activity feed, feedback, referral, invite |
| `references/17-checklist-design-flows.md` | Flows | 13 | Adding to cart, uploading media, verifying account, canceling subscription, filtering items, saving changes, entering promo code, showing input error, resetting password, deleting account, contacting support, making a card payment, submitting a form |

Use them in the build loop: design the screen from the design-system checklist, implement it from the page/screen checklist, and make the flow checklist the acceptance path for multi-step journeys.

## Definition of done

Work is done only when all of these are true:

- Every page has a unique title, meta description, canonical, one H1, per-page og:image, and structured data.
- robots.txt, sitemap.xml, llms.txt, favicon, security.txt, and web app manifest are live and valid.
- Privacy policy, terms, contact, license, 404, and all custom error pages are live.
- Security headers pass. No CSP unsafe-inline on script-src. No exposed source maps, logs, or secrets.
- Lighthouse scores are 90+ in Performance, Accessibility, Best Practices, and SEO. Core Web Vitals are in the good band.
- No console errors. No broken links. No orphan pages. No horizontal scroll at any breakpoint.
- Every image has alt text, explicit dimensions, and a modern format. No image over 500KB.
- Every form has labels, inline errors, success confirmation, and a thank you page.
- Every email is clickable. Every phone number is clickable. Mobile menu and sticky mobile CTA work.
- No banned pattern from `references/02-anti-patterns.md` remains in the build.
- Every page, screen, component, and flow built passes its full checklist.design checklist from `references/13-checklist-design-*.md` — no item skipped or hand-waved.
- `scripts/audit.py` passes with zero fails and zero unaddressed warns.
- A page built with the `zelvior-craft` subskill passes its finish gate (`subskills/zelvior-craft/scripts/gate.mjs` ends `GATE: PASS` or `GATE: OPEN`), and every waiver is recorded with its reason.
- Deploy has health checks, monitoring, alerts, and a tested rollback.

## Subskills

- `subskills/zelvior-design/SKILL.md`: design system, patterns, and anti-patterns only.
- `subskills/zelvior-backend/SKILL.md`: backend, APIs, data, realtime, and scale.
- `subskills/zelvior-security/SKILL.md`: security headers, auth, and hardening.
- `subskills/zelvior-seo-performance/SKILL.md`: SEO, performance, and Core Web Vitals.
- `subskills/zelvior-devops/SKILL.md`: CI/CD, infra, deploys, and SRE.
- `subskills/zelvior-audit/SKILL.md`: the 236-test audit checklist and how to run it.
- `subskills/zelvior-craft/SKILL.md`: anti-slop frontend page skill. Builds client-grade landing, company, product, and game pages from a dealt system, with a real-browser checker and finish gate. Full kit (references, assets, library, scripts) lives in the same folder.
- `subskills/zelvior-lean/SKILL.md`: lean senior-dev mode — the smallest complete change that fully solves the task.
- `subskills/zelvior-lean-review/SKILL.md`: ranked quality review of a change (bugs, risk, load, tests, speed, lean).
- `subskills/zelvior-lean-audit/SKILL.md`: ranked one-shot audit of a whole repo.
- `subskills/zelvior-lean-debt/SKILL.md`: harvests `shortcut:` comments into a tracked debt ledger.
- `subskills/zelvior-lean-gain/SKILL.md`: measured-savings scoreboard (code, cost, speed).
- `subskills/zelvior-lean-help/SKILL.md`: quick reference card for lean levels, skills, and commands.
- `subskills/zelvior-ui/SKILL.md`: UI styling router — picks the right focused subskill for interface work.
- `subskills/zelvior-ui-principles/SKILL.md`: visual hierarchy, whitespace, spacing scales, layout, depth, and polish.
- `subskills/zelvior-ui-palettes/SKILL.md`: 12 ready-to-use color palettes with hex/HSL values in a 50–900 shade scale.
- `subskills/zelvior-ui-fonts/SKILL.md`: curated typeface catalog with weights, licensing, CSS snippets, and pairing tables.
- `subskills/zelvior-ui-components/SKILL.md`: reference patterns with concrete CSS values for buttons, forms, cards, modals, navs, tables, and more.
- `subskills/zelvior-ui-a11y/SKILL.md`: WCAG 2.2 Level A + AA accessibility guidelines with actionable implementation rules.
- `subskills/zelvior-discipline/SKILL.md`: behavioral coding guidelines — think before coding, simplicity first, surgical changes, goal-driven execution. Applies to every build and change.

## Assets and scripts

- `assets/robots.txt`: robots template with sitemap reference.
- `assets/llms.txt`: llms.txt template.
- `assets/security.txt`: security.txt template.
- `assets/sitemap.xml`: sitemap template.
- `assets/404.html`: custom 404 template.
- `scripts/audit.py`: local audit script implementing the highest-signal checks from all 32 modules.
- `subskills/zelvior-craft/scripts/`: the craft page-build kit — `gate.mjs` (finish gate), `start.mjs` (deal/css/brand), `moments.mjs`, `copy-lint.mjs`, `consistency.mjs`, `check.mjs`, `shoot.mjs`, `perf.mjs`, `icons.mjs`, `photos.mjs`, `effects.mjs`.
- `subskills/zelvior-craft/assets/`, `references/`, `library/`: the craft layout, motion, UI, background, effect, object, moment, scene, diagram, icon, and component kits with their reference docs and design tokens.
- `subskills/zelvior-lean*/SKILL.md`: the lean mode and its review, audit, debt, gain, and help reference skills.
- `subskills/zelvior-ui*/SKILL.md`: the UI styling router and its principles, palettes, fonts, components, and accessibility skills.

## Legacy compatibility and requirements

This skill is designed to run across a wide range of systems, from modern
machines down to older legacy hardware. What runs where:

**Always runnable (any OS):** all Markdown knowledge — the root `SKILL.md`,
every `references/` file, and every `subskills/*/SKILL.md`. These are plain
text and need nothing but a viewer. `scripts/audit.py` also runs anywhere
with Python 3.6+ (Python 3.8 is the last version that installs on Windows 7).

**Browser-free craft scripts:** `subskills/zelvior-craft/scripts/copy-lint.mjs`
and `start.mjs` run on any system with Node.js 14+. They need no browser.

**Browser-dependent craft scripts** (`gate.mjs`, `consistency.mjs`, `shoot.mjs`,
`perf.mjs`, `moments.mjs`, `effects.mjs`, `icons.mjs`, `assets/layout/check.mjs`,
`assets/backgrounds/check.mjs`) need Node.js 22+ and a browser engine. They
prefer **Obscura** (a portable single-binary headless browser, ~70 MB, CDP-compatible)
and fall back to Chrome, Edge, or Chromium. When no browser engine is present,
they do not crash: they print a MANUAL-mode message and exit with code 3, and
you follow the documented manual verification path (screenshot the built page
at 1440 / 1024 / 768 / 390 px, check the craft checklist by eye, lint the copy
with `copy-lint.mjs`, and record a `GATE: MANUAL <tool> <pass|open>` line).

**Check your environment:** run `python3 scripts/compat.py`. It probes Python,
Node.js, and the browser engine and reports FULL, PARTIAL, or MANUAL mode.

**Browser engine requirements:** the browser-dependent checks need a modern
OS — Node 22+ prebuilts require Windows 10+, macOS 13.5+, and Linux with
glibc 2.28+. Obscura additionally requires x86_64 (no 32-bit build) and, on
Linux, glibc 2.35+ (Ubuntu 22.04+). Chrome 110+ dropped Windows 7/8/8.1.
On genuinely old systems (e.g. Windows 7 32-bit, very old Linux or macOS),
the browser-dependent checks use the MANUAL path — everything else still runs.

To install Obscura, download the release archive from its repository and put
the `obscura` binary on `PATH` or set `OBSCURA_PATH`. To use Chrome/Edge/Chromium
instead, set `CHROME_PATH` to its executable.
