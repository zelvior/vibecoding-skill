# Accessibility and Mobile Responsiveness

WCAG 2.2 AA minimum. Every item is an audit test.

## Accessibility tests

- Document language: lang attribute on html. lang="en" or the correct locale.
- Form labels: every input has an associated label. All inputs labeled, no exceptions.
- Button names: every button has accessible text.
- Link names: every link has accessible text.
- Descriptive link text: no generic "click here" or "read more" links. Links describe their destination.
- Skip-to-content link: present on every page. Lets keyboard users jump past navigation.
- Image alt text: every content image has descriptive alt. Decorative images use alt="". Missing alt is a high-severity fail.
- tabindex usage: no positive tabindex values. Natural tab order only.
- aria-hidden misuse: never on root or focusable elements.
- Landmark regions: main landmark present. Header, nav, main, footer.
- iframe titles: every iframe has a title. No untitled iframes.
- Keyboard focus visibility: focus always visible. Never suppress outlines without a replacement.
- Lighthouse Accessibility score: 90+.

## Mobile tests

- Viewport meta tag: width=device-width, initial-scale=1.
- Pinch-to-zoom: never disabled. No maximum-scale=1 or user-scalable=no.
- Responsive CSS: real breakpoints at every size. Tailwind-style sm/md/lg or equivalent.
- Apple touch icon: declared.
- Theme color: declared for mobile browser chrome.
- Mobile breakpoints: 360, 390, 480, 640, 768, 1024, 1280, 1440px. Mobile-first.
- No horizontal scroll at any breakpoint. overflow-x: clip on root.
- Mobile menu: full accessible menu with focus trap and Escape support.
- Sticky mobile CTA: bottom bar, safe-area aware, never covers content.
- Hit slop: 44px minimum touch targets.
- Safe area insets: env(safe-area-inset-*) on all mobile layouts.
- All screen sizes: 320px to 2560px. Test real devices.

## Implementation rules

- Test keyboard navigation end to end. Every action reachable and operable by keyboard.
- Test with a screen reader. Headings, landmarks, labels, and alt text must make sense in order.
- Test at 200 percent zoom. No content loss, no horizontal scroll.
- Color contrast: 4.5:1 for body text, 3:1 for large text. Never rely on color alone.
- Motion: respect prefers-reduced-motion. Interruptible animations only.
- Forms: labels, inline errors, error summary with anchor links, focus to summary.
- Agent form-fill reliability: every input has a programmatic label so agents can fill by label text.
