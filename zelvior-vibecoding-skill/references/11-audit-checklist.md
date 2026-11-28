# Audit Checklist: All 236 Tests Across 32 Modules

Extracted from the Audityxe audit of zelviorlabs.vercel.app (2026-11-27). Overall 8.5/10. 198 pass, 29 warn, 3 fail, 6 unverified. Every test below must pass before ship. Fix every fail, fix every warn or document acceptance, re-run until clean.

Severity guide: critical > high > medium > low. Warn counts at half the weight of an equivalent fail. A single high-severity finding escalates its module to critical. Critical and warning modules are score-capped.

## 1. SEO (10 tests)

- [ ] Title tag: one title, 50 to 60 characters, unique per page.
- [ ] Single title tag: exactly one title element.
- [ ] Meta description: one per page, 150 to 160 characters, unique per page.
- [ ] Canonical tag: present on every page.
- [ ] Single canonical tag: at most one canonical per page.
- [ ] H1 heading: exactly one H1 per page.
- [ ] robots.txt: found and valid.
- [ ] sitemap.xml: found and valid.
- [ ] Structured data: JSON-LD present.
- [ ] robots to sitemap link: robots.txt references the sitemap.

## 2. Performance (10 tests)

- [ ] Server response time: under 800ms good, under 200ms excellent.
- [ ] HTML document size: under 100KB target. Over 200KB fails.
- [ ] Render-blocking stylesheets: minimized. Inline critical CSS.
- [ ] External scripts: minimized. Every script is a round trip.
- [ ] Lazy-loaded images: all below-fold images use loading="lazy".
- [ ] Redirect chain: direct, no hops.
- [ ] Response compression: Brotli (br) preferred, gzip fallback.
- [ ] Sampled image weight: no image over 500KB.
- [ ] Asset payload distribution: scripts, styles, and images tracked separately.
- [ ] Layout shift risk (embeds): reserve space for iframes and embeds. Zero CLS.

## 3. Security Headers (25 tests)

- [ ] HTTPS: site served over HTTPS.
- [ ] Redirect downgrade: no HTTPS to HTTP downgrade.
- [ ] Strict-Transport-Security: present, max-age at least 31536000, includeSubDomains, preload.
- [ ] HSTS preload-list eligibility: meets hstspreload.org requirements.
- [ ] HSTS includeSubDomains: set.
- [ ] Content-Security-Policy script-src: present WITHOUT unsafe-inline. High severity fail if weakened.
- [ ] Content-Security-Policy style-src: present WITHOUT unsafe-inline.
- [ ] CSP object-src: 'none'.
- [ ] CSP base-uri: restricted.
- [ ] CSP frame-ancestors: set.
- [ ] X-Frame-Options: present.
- [ ] X-Content-Type-Options: nosniff.
- [ ] Referrer-Policy: privacy-conscious value.
- [ ] Permissions-Policy: present.
- [ ] Cross-Origin-Opener-Policy: present.
- [ ] Cross-Origin-Embedder-Policy: present. Missing is a medium warn.
- [ ] Cross-Origin-Resource-Policy: present.
- [ ] CORS configuration: no wildcard Access-Control-Allow-Origin.
- [ ] Server header exposure: platform not revealed.
- [ ] X-Powered-By: not exposed.
- [ ] Cache-Control on sensitive path: no public caching on sensitive paths.
- [ ] Cookie security: Secure, HttpOnly, SameSite on every cookie.
- [ ] Cookie classification: every cookie classified. No unneeded cookies.
- [ ] Mixed content: no HTTP resources on HTTPS pages.
- [ ] Form action security: no form submits over plain HTTP.

## 4. SSL / TLS Certificate (6 tests)

- [ ] Certificate expiration: valid and monitored. Alert at 30 days.
- [ ] Certificate issuer: trusted CA.
- [ ] Hostname / SAN match: certificate covers the hostname.
- [ ] TLS protocol version: TLS 1.2 minimum, TLS 1.3 preferred.
- [ ] Cipher suite: strong modern ciphers only.
- [ ] Key strength: at least 2048 bits.

## 5. Email Authentication (3 tests)

- [ ] SPF record: present where email is sent.
- [ ] DMARC policy: present and enforced where email is sent.
- [ ] DKIM: present where email is sent. Check common and custom selectors.

## 6. Server Hardening (3 tests)

- [ ] Dangerous HTTP methods: TRACE, CONNECT, and unsafe methods disabled.
- [ ] Exposed configuration files: .env, .git, backups blocked.
- [ ] Directory listing: disabled everywhere.

## 7. DNS Security (6 tests)

- [ ] CAA record: restricts certificate issuance.
- [ ] DNSSEC: enabled where supported.
- [ ] Dangling CNAME / subdomain takeover: no dangling records.
- [ ] Nameserver records: at least two nameservers.
- [ ] SOA record: present.
- [ ] MX records: correct where email is received.

## 8. Subresource Integrity and Link Safety (4 tests)

- [ ] Script SRI: integrity hashes on cross-origin scripts.
- [ ] Stylesheet SRI: integrity hashes on cross-origin stylesheets.
- [ ] Source map exposure: no public .js.map files.
- [ ] target="_blank" safety: every target="_blank" link includes rel="noopener".

## 9. Trust Signals (4 tests)

- [ ] Vulnerability disclosure (security.txt): present with valid contact and expiry.
- [ ] Favicon: resolves correctly.
- [ ] Web app manifest: linked and resolves correctly.
- [ ] Safari pinned-tab icon: optional mask-icon. Unverified if missing.

## 10. Legal and Trust Pages (11 tests)

- [ ] [Necessary] Privacy Policy: live.
- [ ] [Recommended] Terms and Conditions: live.
- [ ] [Skippable] Cookie Policy: live where tracking exists.
- [ ] [Recommended] About: live.
- [ ] [Skippable] FAQ: live where users ask questions.
- [ ] [Skippable] Trust Center: live for SaaS and platforms.
- [ ] [Skippable] Data Processing Agreement (DPA): live for data processors.
- [ ] [Skippable] Acceptable Use Policy: live for platforms with accounts or UGC.
- [ ] [Skippable] Third-Party Services / Subprocessors: live for SaaS.
- [ ] [Skippable] Changelog: live. Publish real changes.
- [ ] [Necessary] Contact: live, with clickable email and phone.

## 11. Content Quality and Readability (4 tests)

- [ ] Duplicate H2 headings: none.
- [ ] Duplicate H3 headings: none.
- [ ] Reading time: stated where helpful.
- [ ] Readability (Flesch-Kincaid): grade level under 9 for general audiences.

## 12. Accessibility (12 tests)

- [ ] Document language: lang declared.
- [ ] Form labels: every input labeled.
- [ ] Button names: every button has accessible text.
- [ ] Link names: every link has accessible text.
- [ ] Descriptive link text: no generic "click here" links.
- [ ] Skip-to-content link: present.
- [ ] Image alt text: every content image has descriptive alt. High severity fail if missing.
- [ ] tabindex usage: no positive tabindex values.
- [ ] aria-hidden misuse: not on root or focusable elements.
- [ ] Landmark regions: main landmark present.
- [ ] iframe titles: every iframe titled.
- [ ] Keyboard focus visibility: focus always visible.

## 13. Mobile Responsiveness (5 tests)

- [ ] Viewport meta tag: width=device-width, initial-scale=1.
- [ ] Pinch-to-zoom: not disabled.
- [ ] Responsive CSS: real breakpoints at every size.
- [ ] Apple touch icon: declared.
- [ ] Theme color: declared.

## 14. UX / UI (8 tests)

- [ ] Above-the-fold CTA: present in the first screen.
- [ ] Primary heading clarity: single, clear H1.
- [ ] Heading nesting: levels in order.
- [ ] Markup semantics: reasonable div ratio. Article and section for content.
- [ ] Form length: reasonable field count.
- [ ] Content depth: 300+ words on key pages.
- [ ] Font family limit: maximum 2 families.
- [ ] Placeholder text: none.

## 15. AI-Generated / Vibe-Coded Pattern Detection (15 tests)

- [ ] Purple-to-blue gradients: none.
- [ ] Gradient hero text: none.
- [ ] Glassmorphism / frosted glass: none.
- [ ] Emojis in production UI: none in headings or buttons.
- [ ] Pill badge above hero headline: none.
- [ ] Repeated icon rows: none.
- [ ] Scroll-triggered fade-in animation: none.
- [ ] Cursor-following glow / particles: none.
- [ ] Hover opacity fade on buttons: none.
- [ ] Grainy canvas texture overlays: none.
- [ ] Card corner radius: no 20px+ oversized radii.
- [ ] Font choice: not Inter-only.
- [ ] Font pairing: not Space Grotesk plus Instrument Serif.
- [ ] Overused em dashes: zero. 16+ fails.
- [ ] Generic SaaS buzzwords: none.

## 16. Technical Stack (7 tests)

- [ ] CMS / platform: honest. Custom-built is legitimate.
- [ ] Frontend framework: honest detection.
- [ ] jQuery: not detected.
- [ ] Analytics: present. Missing is a low warn.
- [ ] CDN-hosted libraries: none or self-hosted.
- [ ] Hosting provider: honest.
- [ ] Generator meta tag: honest framework identifier.

## 17. HTML Structure (8 tests)

- [ ] Doctype: present.
- [ ] Landmark structure: header, nav, main, footer present.
- [ ] Content sectioning: article and section, not only divs.
- [ ] Unique IDs: all id attributes unique.
- [ ] Deprecated tags: none.
- [ ] Language declaration: present.
- [ ] Charset declaration: present.
- [ ] HTML comment volume: reasonable. No sensitive data.

## 18. Meta Tags (8 tests)

- [ ] Title: present and unique.
- [ ] Description: present and unique.
- [ ] Language: declared.
- [ ] Charset: declared.
- [ ] Viewport: declared.
- [ ] Canonical: declared.
- [ ] Robots meta: not set (indexable) unless exclusion is intended.
- [ ] Generator: honest framework identifier.

## 19. Sitemap and Robots.txt (5 tests)

- [ ] robots.txt exists: live GET returns 200.
- [ ] Crawler access: not globally blocked.
- [ ] sitemap.xml exists: valid XML.
- [ ] Freshness data: lastmod present.
- [ ] Cross-reference: robots.txt references the sitemap.

## 20. Structured Data (5 tests)

- [ ] JSON-LD present: at least one block.
- [ ] Valid JSON: all blocks parse without error.
- [ ] Schema types found: Organization, WebSite, FAQPage, Review where relevant.
- [ ] Required fields: every schema type has required fields.
- [ ] Organization/WebSite schema: present.

## 21. Broken Links (3 tests)

- [ ] Links found: sample at least 10 links.
- [ ] Broken (404/410/5xx): none.
- [ ] Unreachable links: none.

## 22. Image Optimization (6 tests)

- [ ] Images found: count all images.
- [ ] Explicit dimensions: every image has width and height.
- [ ] Modern formats: WebP or AVIF. No legacy JPG/PNG/GIF only.
- [ ] Lazy loading: below-fold images use loading="lazy".
- [ ] Inline base64 images: none.
- [ ] Live weight sample: no image over 500KB.

## 23. Third-Party Scripts (7 tests)

- [ ] Total external scripts: minimized. Zero is ideal.
- [ ] Analytics: present and privacy-respecting.
- [ ] Ad networks: only where monetization is intended.
- [ ] Tag managers: only where needed.
- [ ] Chat/support widgets: only where support is offered.
- [ ] Web font services: self-host preferred.
- [ ] Uncategorized third parties: none.

## 24. Social Metadata (8 tests)

- [ ] Open Graph completeness: og:title, og:description, og:type, og:url present.
- [ ] og:site_name: present.
- [ ] Twitter Card type: summary_large_image.
- [ ] twitter:site: present where applicable.
- [ ] twitter:creator: present where applicable.
- [ ] Facebook App ID: optional. Only for Facebook Insights.
- [ ] twitter:image: explicitly set where needed.
- [ ] og:image: per-page image that loads. Live-check it.

## 25. Basic Monetization Setup (7 tests)

- [ ] ads.txt: present where programmatic ads run.
- [ ] Ad networks detected: honest.
- [ ] Affiliate links: disclosed.
- [ ] Payment processors: real.
- [ ] Donation/support platforms: real.
- [ ] E-commerce signals: real.
- [ ] Pricing signals: honest.

## 26. Site Structure, Multi-Page Crawl (5 tests)

- [ ] Pages sampled: crawl at least 100 pages for large sites.
- [ ] Internal links (extended): no broken internal links beyond the homepage. High severity fail.
- [ ] Orphan pages: none.
- [ ] Thin content (extended): every page has at least 80 words.
- [ ] JS-rendered content risk: no client-only content crawlers cannot see.

## 27. Cookies and Redirects (3 tests)

- [ ] Cookie flags: Secure, HttpOnly, SameSite on every cookie.
- [ ] Redirect hops: URL resolves directly with no redirects.
- [ ] HTTP to HTTPS upgrade: resolves to an https URL.

## 28. AI Search and Agent Optimization (10 tests)

- [ ] AI crawler access: GPTBot, ClaudeBot, PerplexityBot, Google-Extended not blocked.
- [ ] llms.txt: present with real content.
- [ ] X-Robots-Tag header: no noindex on indexable pages.
- [ ] AI-training opt-out signal: optional. Note noai/noimageai only where intended.
- [ ] FAQPage schema: present on FAQ pages.
- [ ] Author/entity schema: Organization structured data present.
- [ ] Question-phrased headings: sections phrased as questions they answer.
- [ ] Direct-answer opening: first heading followed by a concise self-contained paragraph.
- [ ] Agent navigation landmarks: ARIA landmarks present.
- [ ] Agent form-fill reliability: every input has a programmatic label.

## 29. Conversion Rate Optimization (8 tests)

- [ ] Call-to-action presence: clear CTA on every key page.
- [ ] Above-the-fold CTA: present before scrolling.
- [ ] Lead-capture form: present where conversion is the goal.
- [ ] Form length: reasonable field count.
- [ ] Direct contact links: tel and mailto present.
- [ ] Mobile viewport: responsive viewport meta present.
- [ ] Trust signal: Organization schema present.
- [ ] Trust signal: reviews/ratings. Review or AggregateRating schema where real.

## 30. TTFB (2 tests)

- [ ] Time to First Byte: under 800ms good band.
- [ ] Server-side compression: br enabled.

## 31. Lighthouse Audit (17 tests)

- [ ] Performance score: 90+ (good band).
- [ ] Accessibility score: 90+ (good band).
- [ ] Best Practices score: 90+ (good band).
- [ ] SEO score: 90+ (good band).
- [ ] LCP: at or under 2500ms.
- [ ] CLS: at or under 0.1.
- [ ] TBT: at or under 200ms.
- [ ] FCP: at or under 1800ms.
- [ ] Speed Index: at or under 3400ms.
- [ ] Real-world Core Web Vitals: monitor CrUX field data.
- [ ] Render-blocking requests: zero on the critical path.
- [ ] Network dependency tree: shortened chains, smaller resources, deferred non-critical loads.
- [ ] Browser errors were logged to the console: zero console errors.
- [ ] Reduce unused JavaScript: dead code removed, tree-shaken, deferred.
- [ ] Improve image delivery: responsive sizes, srcset, CDN, preload LCP.
- [ ] Legacy JavaScript: polyfills removed for modern browsers.
- [ ] Use efficient cache lifetimes: long cache on hashed assets, short on HTML.

## 32. Real-User Experience, CrUX (1 test)

- [ ] Field data availability: monitor CrUX. No data means low traffic, not a failure. Lab scores are the best signal until field data arrives.

## Fixes from the audit

- Image alt text (high severity): 7 of 7 images missing alt. Fix: add descriptive alt to every content image. Use alt="" only for purely decorative images.

```diff
<img src="/example.png"
-  alt=""
+  alt="Describe what this image actually shows"
/>
```

## Top Lighthouse issues to fix first

1. Render-blocking requests: move off the critical path.
2. Network dependency tree: shorten chains, shrink resources, defer non-critical loads.
3. Browser errors in console: fix every error.
4. Reduce unused JavaScript: remove dead code, defer until required.
5. Improve image delivery: responsive sizes, CDN, preload LCP.
6. Legacy JavaScript: remove polyfills for modern browsers.
7. Use efficient cache lifetimes: long cache on hashed assets.

## Scoring notes

- Overall is the unweighted average of 6 category scores: Messaging and Copy Clarity, UI/UX and Visual Hierarchy, CRO, Technical and Metadata Health, Brand Distinctiveness, Security and Performance.
- Every fail or warn subtracts a fraction of its module score based on severity. Warn counts at half the weight of an equivalent fail.
- Module status (good, warning, critical) is set from severity alone. A single high-severity finding escalates a module to critical.
- Hard ceilings apply for failures that make the rest of a checklist moot: no HTTPS, robots.txt blocking every crawler, no responsive viewport, HTTPS to HTTP downgrade, zero CTAs.
