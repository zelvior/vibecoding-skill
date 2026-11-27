---
name: zelvior-seo-performance
description: Zelvior SEO and performance subskill. Use for absolutely any request that involves, touches, or concerns SEO, ranking, rank, search, search results, Core Web Vitals, performance, speed, load, loading, Lighthouse, image, images, or metadata — no matter the wording or register. Matches whether the user wants to improve, optimize, speed up, speed, accelerate, tune, fix, get better, boost, raise, increase, clean up, or enhance SEO, ranking, rank, search results, visibility, traffic, visits, performance, speed, load time, load speed, Core Web Vitals, Lighthouse scores, images, or metadata — or says make it rank, improve my SEO, boost my SEO, speed up the site, make it faster, make the site faster, speed up the page, get more traffic, get more visits, better search results, better ranking, optimize performance, improve performance, how do I improve ranking, how do I rank higher, and anything even loosely like it. Part of zelvior-vibecoding-skill.
---

# Zelvior SEO and Performance Subskill

Ship crawlable, fast, shareable pages. Read `../../references/05-seo-technical.md` and `../../references/07-performance.md` for full detail.

## SEO must-have

Unique title and meta description per page, one canonical, exactly one H1, nested headings, no duplicate H2/H3, robots.txt, sitemap.xml with lastmod, valid JSON-LD (Organization, WebSite, FAQPage, Review), no broken links, no orphan pages, no thin content, no client-only content, llms.txt, AI crawlers allowed, Open Graph and Twitter Card per page with loading og:image, honest meta tags, valid HTML with landmarks and unique IDs, legal pages live (privacy, terms, contact, license).

## Performance must-have

TTFB under 800ms, LCP under 2500ms, CLS under 0.1, INP under 200ms, TBT under 200ms, Lighthouse 90+ in all four categories. HTML under 100KB, Brotli compression, minimal render-blocking resources, minimal external scripts, lazy-loaded images, WebP/AVIF under 500KB with explicit dimensions, no inline base64, efficient cache lifetimes, no console errors, no unused JS, no legacy polyfills, shortened dependency tree.

## Rules

- Never the same title or description twice. Never a page without an H1.
- Never ship without robots, sitemap, llms.txt, favicon, and structured data.
- Never ship console errors, massive bundles, or unoptimized images.
