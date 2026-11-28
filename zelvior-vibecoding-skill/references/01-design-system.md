# Design System: Must-Have Patterns

Detailed implementation notes for every design must-have in the mega skill. Build the system first, then the screens.

## Foundations

- Color: one restrained palette. No purple and black. No neon. No basic pastels. No rainbow. No pure white background. Use a warm off-white or tinted surface with strong contrast. Text contrast at least 4.5:1 for body, 3:1 for large text.
- Type: maximum 2 font families. Never Inter-only. Never Space Grotesk plus Instrument Serif. Pair a distinctive display face with a readable text face. Balanced headlines with text-wrap: balance.
- Spacing: 4px base scale. Generous whitespace. No cramped layouts.
- Radius: continuous corners (squircle) where supported. Never soft oversized radius (20px+ on cards). Small, deliberate radii only.
- Motion: fast, interruptible, reversible. 150 to 300ms for micro-interactions. Respect prefers-reduced-motion. Never scroll-triggered fade-in as the primary reveal. Never cursor-following glow or particles.
- Icons: custom or brand icons. Never Lucide. Never sparkle icons. Never repeated icon rows as decoration.
- Shadows: no decorative drop shadows. Use borders, surface tints, and spacing for depth. A single functional shadow for overlays only, if needed.

## Pattern details

### Skeleton loaders

- Match the skeleton to the final layout: same dimensions, same blocks.
- Show skeletons for any load over 300ms. Swap to content without layout shift.
- Never use a lone spinner for content areas. Never show a blank screen.
- Skeleton count matches expected item count. Animate with a subtle shimmer, disabled under reduced motion.

### Optimistic updates

- Apply the change locally first. Send the request in background.
- On failure, roll back and show an undo toast with the error in plain language.
- On success, reconcile silently. Never flash the UI.
- Use for likes, toggles, quantity changes, and list reordering.

### Command menu

- Cmd/Ctrl+K opens a palette. Fuzzy search over actions, pages, and records.
- Full keyboard navigation: arrows, Enter, Escape. Show shortcut hints inside the menu.
- Recent actions first. Empty query shows suggested actions, never a blank menu.

### Shortcut hints

- Render shortcuts with kbd styling next to the action they trigger.
- Discoverable: a shortcuts help dialog (?) lists every shortcut.
- Never assign a shortcut that conflicts with browser or OS defaults.

### Undo toasts

- Every destructive or mutating action offers undo for at least 5 seconds.
- Toast states what happened and offers Undo as the primary action.
- Undo restores the exact prior state. Redo is a bonus, not a requirement.

### Stale-while-revalidate

- Serve cached data instantly. Revalidate in background. Update silently.
- Show a subtle "Updated" indicator or timestamp. Never a full-page reload.
- Set per-resource stale times. Money, auth, and permissions data never serve stale.

### Pre-rendering

- Pre-render all marketing and static pages at build time.
- Use ISR for content that changes on a schedule. Revalidate on demand for edits.
- Never ship a client-only shell for public pages. Crawlers must see real content in HTML.

### BlurHash placeholders

- Every image has a BlurHash or dominant-color placeholder.
- Reserve space with explicit width and height or aspect-ratio. Zero layout shift.
- Fade the real image in over the placeholder. Never pop it in.

### View transitions

- Use the View Transitions API for page changes and major state changes.
- Fall back to instant swaps where unsupported. Never block navigation on animation.
- Keep transitions under 300ms. Interruptible at any point.

### Swipe-to-dismiss sheets

- Bottom sheets, toasts, and cards dismiss with swipe on touch devices.
- Provide a visible close button and Escape key support. Focus returns to the trigger.
- Snap points for partial and full sheet states. Never trap the user.

### Interruptable animations

- Every animation can be interrupted and reversed mid-flight.
- Use spring or ease-out curves that feel responsive, not theatrical.
- Under prefers-reduced-motion, replace motion with instant state changes.

### Predictive back

- Support Android predictive back. Back gestures preview the previous screen.
- Never break system back behavior. Never trap history.
- Web: ensure browser back restores scroll and state correctly.

### Hit slop

- Touch targets at least 44px by 44px.
- Expand hit area beyond the visual icon with padding or pseudo-elements.
- Adjacent targets never overlap. Test with one thumb.

### Safe area insets

- Use env(safe-area-inset-top/right/bottom/left) on all mobile layouts.
- Sticky bars, sheets, and CTAs pad for the home indicator and notch.
- Test on notched and non-notched devices.

### One-time code autofill

- OTP inputs: autocomplete="one-time-code", inputmode="numeric", pattern="[0-9]*".
- Split into per-digit fields with auto-advance and paste support.
- Support SMS autofill on iOS and Android. Provide resend with a countdown.

### Tabular numbers

- font-variant-numeric: tabular-nums on prices, metrics, tables, timers, and counters.
- Digits never jitter when values change.

### Balanced headlines

- text-wrap: balance on all headings.
- Never leave a single orphan word on the last line.
- Test headlines at the narrowest breakpoint.

### Continuous corners

- Use border-radius with continuous curves (corner-shape: squircle) where supported.
- Fall back to standard radius gracefully. Keep radii small and deliberate.

### Indempotency keys

- Every mutating API call accepts an Idempotency-Key header.
- Same key plus same payload returns the stored response. Same key plus different payload returns 422.
- Store keys with responses for at least 24 hours. See backend reference.

### Amazon safe triangle

- Hover menus stay open while the cursor travels from trigger to menu.
- Implement with a padded bridge or a triangle hit area between trigger and menu.
- Never close the menu on diagonal cursor movement. Add a close delay of 150 to 300ms.

### No horizontal scroll

- Test at 320, 360, 390, 768, 1024, 1440, and 2560px.
- Fix overflow with minmax(), wrapping, and overflow-x: clip on the root element.
- Long tables scroll inside their container, never the page. Code blocks scroll internally.

### Clickable emails and phone numbers

- Every email is an a href="mailto:" link. Every phone number is an a href="tel:" link.
- Include the full number in the tel href with country code. Never render contact details as plain text.

### Mobile menu

- Full accessible menu: focus trap, Escape to close, focus returns to trigger.
- Visible current page state. Large touch targets. No content hidden behind the menu.

### Error and success messages

- Errors: what happened, why, and what to do next. Plain language. No codes, no stack traces.
- Success: what changed and what happens next. Confirm the outcome, not just "Done".
- Form errors: inline per field, plus a summary with anchor links. Focus moves to the summary.

### Custom pages

- Custom 404: branded, with search, key links, and a homepage path. Returns HTTP 404.
- Custom error pages: 400, 401, 403, 404, 429, 500, 503. Each branded, helpful, correct status code.
- Custom thank you pages: summary of what was submitted or purchased, next steps, and a path back.

### Mobile breakpoints and sticky CTA

- Mobile-first. Breakpoint scale: 360, 390, 480, 640, 768, 1024, 1280, 1440px.
- Sticky mobile CTA: bottom bar with the primary action. Respects safe areas. Never covers content. Dismissible where appropriate.

### Loading and form error states

- Every async surface has a loading state. Every form has inline errors, a summary, and recovery paths.
- Never freeze the UI. Never lose user input on error. Preserve drafts.

### Cookie banner

- Accept, reject, and customize. No non-essential tracking before consent.
- Store the choice in a first-party cookie or local storage. Respect it on every visit.
- Re-prompt only when the policy changes. Link to the cookie policy page.
