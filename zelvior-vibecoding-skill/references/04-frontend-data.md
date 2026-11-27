# Frontend and Data: Rendering, State, and UX States

## Rendering strategy

- Pre-render marketing and static pages at build time. ISR for scheduled content.
- SSR for personalized or crawlable dynamic pages. Never ship a client-only shell for public pages.
- Client rendering only for app surfaces behind auth. Even there, server-render the shell.
- No Vite plus React browser-only SPA for public pages. Crawlers must see real content in HTML.
- No empty view-source. Server HTML contains real content, not a JS shell.

## Performance patterns

- Split code into chunks. Route-level code splitting. Load heavy features on demand.
- Paginate every large list. Cursor pagination for feeds. Never load unbounded lists.
- Eliminate unnecessary re-renders. Memoize components, virtualize long lists, keep state close to usage.
- Minify CSS and JS. Tree-shake dead code. Remove legacy polyfills for modern browsers.
- Lazy load images and non-critical embeds. Eager load only the LCP image.
- Defer non-critical scripts. Async or defer everything off the critical path.
- No massive JS bundles. Budget: under 200KB JS per route, ideally under 100KB.
- No console errors in production. Fix every error before ship.

## State and data

- Server is source of truth. Local storage for drafts and preferences only.
- Stale-while-revalidate for reads. Optimistic updates for reversible writes. Undo toasts for destructive writes.
- Network states: offline, slow, and error states with retry. Never a dead screen.
- Data persistence: handle conflicts with versioning. Preserve drafts across errors and reloads.
- Crash reporting: capture and report client crashes with breadcrumbs. No PII in reports.

## UX states (every surface, every time)

- Loading: skeleton matching layout. Never blank, never a lone spinner for content.
- Empty: explain what is missing and how to add it. Guide the user to the next action.
- Error: what happened, why, and what to do next. Retry where possible. Preserve input.
- Success: what changed and what happens next. Confirm the outcome.
- Form errors: inline per field, summary with anchor links, focus to summary, aria-describedby.
- Onboarding: progressive, skippable, completable in under 2 minutes.
- User flows: map every flow end to end. No dead ends. Every step has back, cancel, and error paths.

## Responsive and mobile

- All screen sizes: 320px to 2560px. Test real devices, not just devtools.
- Mobile breakpoints: 360, 390, 480, 640, 768, 1024, 1280, 1440px. Mobile-first.
- No horizontal scroll at any breakpoint. overflow-x: clip on root. Tables scroll internally.
- Mobile menu: full accessible menu with focus trap and Escape support.
- Sticky mobile CTA: bottom bar, safe-area aware, never covers content.
- Hit slop: 44px minimum touch targets. Safe area insets on all mobile layouts.
- Swipe-to-dismiss sheets and toasts. Predictive back on Android. View transitions for page changes.
- One-time code autofill: autocomplete="one-time-code", inputmode="numeric", per-digit fields with paste support.
- Tabular numbers for prices, metrics, and tables. Balanced headlines with text-wrap: balance.

## Forms

- Every input has a programmatic label. Every button has an accessible name.
- Reasonable field count. 8 fields is the ceiling for a lead form.
- Inline errors, error summary, success confirmation, and a thank you page.
- Clickable emails (mailto) and phone numbers (tel) everywhere they appear.
- Cookie banner: accept, reject, customize. No non-essential tracking before consent.
