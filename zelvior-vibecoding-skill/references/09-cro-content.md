# CRO, Content Quality, Brand, and Monetization

## CRO tests

- Call-to-action presence: clear CTA on every key page. Count them. Zero CTAs fails.
- Above-the-fold CTA: a CTA in the first screen of content, before scrolling.
- Lead-capture form: present where conversion is the goal.
- Form length: reasonable field count. 8 fields is the ceiling for a lead form.
- Direct contact links: tel and mailto links present. No tel/mailto is a warn.
- Mobile viewport: responsive viewport meta present. CTAs and forms usable on mobile.
- Trust signal: Organization schema present.
- Trust signal: reviews and ratings. Review or AggregateRating schema where real reviews exist.
- Sticky mobile CTA: primary action always reachable on mobile.
- Response time promise: state a real, kept response time on contact pages.
- Case studies: real results with numbers, quotes, and dates.
- Five FAQs: at least five real questions per key page, with FAQPage schema.
- Maps and directions: embedded map plus directions link on location pages.
- Internal links and breadcrumbs: every page linked, breadcrumbs below homepage.
- Onboarding and empty states: guide new users to value fast.

## Content quality tests

- Duplicate H2 headings: none. Duplicate H3 headings: none.
- Reading time: state it where helpful. 200 wpm estimate.
- Readability (Flesch-Kincaid): grade level under 9 for general audiences. Grade 14.8 is noticeably dense and fails.
- Content depth: at least 300 words on key pages. Under 80 words is thin content.
- Placeholder text: no lorem ipsum anywhere.
- Generic SaaS buzzwords: none. No delve, elevate, unlock, supercharge, seamless, cutting-edge, revolutionary, game-changer, leverage, empower, unleash.
- Overused em dashes: zero. 16+ em dashes is an AI tell and fails.
- No "It's not X, it's Y" copy. No checkmark bullets.

## UX and UI tests

- Above-the-fold CTA: present in the first screen.
- Primary heading clarity: single, clear H1.
- Heading nesting: levels in order.
- Markup semantics: reasonable div ratio. Article and section for content.
- Form length: reasonable field count.
- Content depth: 300+ words on key pages.
- Font family limit: maximum 2 families.
- Placeholder text: none.

## Brand and vibe-coded signals

- Purple-to-blue gradients: none. Gradient hero text: none.
- Glassmorphism or frosted glass: none.
- Emojis in production UI: none in headings or buttons.
- Pill badge above hero headline: none.
- Repeated icon rows: none.
- Scroll-triggered fade-in animation: none.
- Cursor-following glow or particles: none.
- Hover opacity fade on buttons: none.
- Grainy canvas texture overlays: none.
- Card corner radius: no 20px+ oversized radii.
- Font choice: not Inter-only. Font pairing: not Space Grotesk plus Instrument Serif.
- Overused em dashes: zero. Generic SaaS buzzwords: none.
- Pure white background: none. Purple and black: none. Neon: none. Basic pastels: none.
- Lucide icons: none. Sparkle icons: none. Radial orbs: none. Dot grids: none. Animated arrows: none.
- Three feature cards in a row: none. Three pricing tiers: none. Terminal window: none.
- No real product demos: never. Every demo is a working product surface.

## Technical stack tests

- CMS or platform: custom-built is legitimate. No traditional CMS required.
- Frontend framework: honest detection. Next.js, Astro, Remix, or custom. Never fake it.
- jQuery: not detected. Never ship jQuery for new builds.
- Analytics: present. No analytics is a warn. Privacy-respecting by default.
- CDN-hosted libraries: none or self-hosted. Audit every CDN dependency.
- Hosting provider: honest. Vercel, Netlify, Cloudflare, or self-hosted.
- Generator meta tag: honest framework identifier.

## Third-party scripts

- Total external scripts: minimize. Zero is ideal. Every script is a round trip and a risk.
- Analytics: present and privacy-respecting.
- Ad networks: only where monetization is intended.
- Tag managers: only where needed. Each tag needs a purpose.
- Chat and support widgets: only where support is offered.
- Web font services: self-host preferred. Audit every font request.
- Uncategorized third parties: none. Every third party is categorized and justified.

## Monetization

- ads.txt: present where programmatic ads run. Missing is a warn only if ads run.
- Ad networks detected: honest. Affiliate links: disclosed. Payment processors: real.
- Donation and support platforms: real. E-commerce signals: real. Pricing signals: honest.
- Never fake monetization signals. Never ship fake pricing or fake payment buttons.
