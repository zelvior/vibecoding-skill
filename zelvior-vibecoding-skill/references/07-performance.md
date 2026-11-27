# Performance and Core Web Vitals

## Thresholds (Google good bands)

- TTFB under 800ms. Server response time under 200ms is excellent.
- LCP at or under 2500ms. FCP at or under 1800ms. Speed Index at or under 3400ms.
- CLS at or under 0.1. TBT at or under 200ms. INP at or under 200ms.
- Lighthouse: Performance 90+, Accessibility 90+, Best Practices 90+, SEO 90+.

## Audit tests

- Server response time: under 200ms excellent, under 800ms good.
- Time to First Byte: under 800ms good band.
- Server-side compression: Brotli (br) preferred, gzip fallback. Always on.
- HTML document size: under 100KB target. Over 200KB is heavy and fails.
- Render-blocking stylesheets: minimize. Inline critical CSS. Defer the rest.
- Render-blocking requests: move off the critical path. Zero on first load.
- External scripts: minimize. Every script is a round trip. Self-host or remove.
- Network dependency tree: shorten chains. Smaller resources. Defer non-critical loads.
- Lazy-loaded images: all below-fold images use loading="lazy". Hero image eager.
- Sampled image weight: no image over 500KB.
- Asset payload distribution: track scripts, styles, and images separately. Images are usually heaviest.
- Layout shift risk (embeds): reserve space for iframes and embeds. Zero CLS.
- Response compression: br enabled. Reduces bytes after first byte.
- Redirect chain: direct, no hops.
- Browser errors were logged to the console: zero console errors in production.
- Reduce unused JavaScript: remove dead code. Tree-shake. Defer until required.
- Improve image delivery: responsive sizes, srcset, CDN, preload LCP.
- Legacy JavaScript: remove polyfills and transforms for modern browsers.
- Use efficient cache lifetimes: long cache on hashed assets, short on HTML.
- Real-world Core Web Vitals: monitor CrUX field data. Lab scores do not replace field data.
- Field data availability: no CrUX data means low traffic, not a failure. Monitor until data arrives.

## Rules

- HTML under 100KB where possible. Never ship 200KB+ without justification.
- Minimize render-blocking stylesheets and scripts. Inline critical CSS. Defer the rest.
- Minimize external scripts. Self-host or remove. Audit third parties quarterly.
- Response compression: Brotli preferred, gzip fallback. Always on.
- Lazy load images below the fold. Eager load only the LCP image.
- Images: WebP or AVIF, explicit width and height, under 500KB each, no inline base64.
- No layout shift from embeds. Reserve space for iframes and embeds.
- Efficient cache lifetimes: long cache on hashed assets, short on HTML, purge on deploy.
- Reduce unused JavaScript. Remove legacy polyfills for modern browsers.
- Improve image delivery: responsive sizes, srcset, CDN, and preload for LCP.
- Shorten the network dependency tree. Fewer chains, smaller resources, deferred non-critical loads.
- Zero console errors. Zero render-blocking requests on the critical path.
- Split code into chunks. Route-level splitting. Heavy features on demand.
- Paginate large lists. Cursor pagination. Never load unbounded lists.
- Minify CSS and JS. Tree-shake dead code.
- Defer non-critical scripts. Async or defer everything off the critical path.
- No massive JS bundles. Budget under 200KB per route, ideally under 100KB.
- Cache API responses and expensive queries. CDN, edge, and application caching.
- Throughput, P99, and tail latency: track p50, p95, p99, p999. Optimize the tail.
