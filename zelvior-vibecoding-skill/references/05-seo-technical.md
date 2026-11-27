# SEO and Technical Health

Every item here is an Audityxe audit test. Pass all of them.

## On-page SEO

- Title tag: one per page, 50 to 60 characters, unique per page. Never the same title twice.
- Single title tag: exactly one. No duplicates, no missing.
- Meta description: one per page, 150 to 160 characters, unique per page.
- Canonical tag: one per page, self-referencing unless a canonical URL is intended. Single canonical only.
- H1 heading: exactly one per page. No page without an H1. No page with two H1s.
- Heading nesting: H1, then H2, then H3 in order. No skipped levels.
- Duplicate H2 headings: none. Duplicate H3 headings: none.
- Primary heading clarity: single, clear H1 that states the page purpose.
- Content depth: at least 300 words on key pages. Thin content under 80 words fails.
- Reading time: state it where helpful. Target 200 wpm estimate.
- Readability (Flesch-Kincaid): grade level under 9 for general audiences. Short sentences, plain words.
- Placeholder text: no lorem ipsum anywhere.
- Markup semantics: article and section for content, not only divs. Reasonable div ratio.
- Font family limit: maximum 2 families.
- Content sectioning: use article and section elements.

## Crawlability and indexability

- robots.txt: exists, valid, references sitemap.xml. Never blocks all crawlers.
- Crawler access: not globally blocked. AI crawlers not blocked unless intended.
- sitemap.xml: exists, valid XML, lastmod dates present, under 50,000 URLs per file.
- Freshness data: lastmod in sitemap entries.
- Cross-reference: robots.txt references the sitemap. robots and sitemap link each other.
- X-Robots-Tag header: no noindex on pages meant to be indexed.
- Robots meta: not set (defaults to indexable) unless a page must be excluded.
- Redirect chain: direct, no hops. HTTP to HTTPS upgrade in one hop.
- Internal links: every page linked from at least one other page. No orphan pages.
- Broken links: none. Check every link with a live request. No 404, 410, or 5xx.
- Unreachable links: none.
- Thin content (extended): every crawled page has at least 80 words of visible text.
- JS-rendered content risk: no client-only content that crawlers cannot see. Server-render key content.
- Pages sampled: crawl the full site in QA. Sample at least 100 pages for large sites.
- Internal links (extended): check beyond the homepage. Broken internal links fail the audit.
- Orphan pages: none in the crawled sample.
- No empty view-source. No Vite plus React browser-only SPA for public pages.

## Structured data and metadata

- Structured data: valid JSON-LD with required fields for every schema type used.
- JSON-LD present and valid. All blocks parse without error.
- Schema types: Organization and WebSite on the homepage. FAQPage on FAQ pages. Review and AggregateRating where real reviews exist.
- Required fields: every schema type has its required fields.
- Organization/WebSite schema: present, helps search engines understand the entity.
- Author/entity schema: named organization so AI systems can attribute content.
- FAQPage schema: on every page with FAQs. Highest-leverage change for AI-answer citability.
- Meta tags: title, description, language, charset, viewport, canonical, robots, generator all declared.
- Generator meta: honest framework identifier. Never fake it.
- Open Graph: og:title, og:description, og:type, og:url, og:image, og:site_name on every page.
- og:image: per-page image that loads, 1200x630. Live-check it.
- Twitter Card: summary_large_image with twitter:site and twitter:creator where applicable.
- twitter:image: explicitly set where the card needs a specific image.
- Facebook App ID: optional. Only needed for Facebook Insights.
- Social share images: per-page, load-tested, with title and description.

## HTML structure

- Doctype: <!DOCTYPE html> present.
- Landmark structure: header, nav, main, footer all present.
- Landmark regions: main landmark present. ARIA landmarks for agent navigation.
- Unique IDs: all id attributes unique.
- Deprecated tags: none.
- Language declaration: lang on html. Charset declaration present.
- HTML comment volume: reasonable. No sensitive data in comments.
- Document language: lang="en" or the correct locale declared.

## AI search and agent readiness

- AI crawler access: GPTBot, ClaudeBot, PerplexityBot, Google-Extended not blocked unless intended.
- llms.txt: present with real content describing the site.
- AI-training opt-out signal: optional. Note noai/noimageai only where intended.
- Question-phrased headings: rephrase section headings as the question they answer.
- Direct-answer opening: first heading followed by a concise self-contained paragraph.
- Agent navigation landmarks: ARIA landmarks give agents a structural map.
- Agent form-fill reliability: every input has a programmatic label.

## Legal and trust pages

- Privacy Policy: necessary for every site. Live and current.
- Terms and Conditions: recommended for every site. Live.
- Contact: necessary for every site. Live, with clickable email and phone.
- License page: mandatory. Live.
- Cookie Policy: where tracking exists. Link from the cookie banner.
- About: recommended. Builds basic trust.
- FAQ: where users ask questions. At least 5 real FAQs per key page.
- Changelog: nice-to-have. Publish real changes.
- Trust Center, DPA, Acceptable Use Policy, Subprocessors: where relevant to site type (SaaS, platforms, data processors).
- Case studies: real results with numbers, quotes, and dates. No invented metrics.
- Breadcrumbs: visible and structured-data marked up below the homepage.
- Response time promise: state a real, kept response time on contact pages.
- Maps and directions: embedded map plus directions link on location pages.
