---
name: zelvior-design
description: Zelvior design system subskill. Use for absolutely any request that involves, touches, or concerns UI, UX, visual design, look-and-feel, styling, components, motion, animation, or brand — no matter the wording or register. Matches whether the user wants to design, style, format, lay out, structure, arrange, organize, plan, sketch, mock up, polish, refine, overhaul, revamp, improve, or fix up a UI, screen, or interface; set up, build, create, or define a design system; build, make, design, or review components; add motion, animation, or transitions; or define, set up, pick, or choose brand visuals, colors, identity, or look — or says I need a design system, help me design the UI, how should I style this, can you lay out the screen, make it look good, make it look better, design the components, how should I structure the UI, what should the look be, and anything even loosely like it. Covers must-have patterns and banned anti-patterns. Part of zelvior-vibecoding-skill.
---

# Zelvior Design Subskill

Build distinctive, restrained, production-grade UI. Read `../../references/01-design-system.md` and `../../references/02-anti-patterns.md` for full detail.

## Page, screen, and flow checklists

138 checklist.design checklists cover every page type, app screen, design-system component, and user flow. Read the matching file and pass every item before calling a screen done:

- `../../references/13-checklist-design-website.md` — 27 website page types
- `../../references/14-checklist-design-web-app.md` — 38 web app screens
- `../../references/15-checklist-design-design-system.md` — 32 foundations and components
- `../../references/16-checklist-design-mobile.md` — 28 mobile screens and patterns
- `../../references/17-checklist-design-flows.md` — 13 user flows

## Must-have patterns

Skeleton loaders, optimistic updates, command menu, shortcut hints, undo toasts, stale-while-revalidate, pre-rendering, BlurHash placeholders, view transitions, swipe-to-dismiss sheets, interruptable animations, predictive back, hit slop (44px), safe area insets, one-time code autofill, tabular numbers, balanced headlines, continuous corners, indempotency keys, Amazon safe triangle, no horizontal scroll, clickable emails and phones, mobile menu, clear error and success messages, custom 404 and error pages, custom thank you pages, mobile breakpoints, sticky mobile CTA, loading states, form error states, cookie banner.

## Banned patterns

Harsh gradients, Lucide icons, pure white background, rainbow coloring, decorative drop shadows, three feature cards in a row, emojis, liquid glass, glassmorphism, terminal window, "It's not X, it's Y" copy, checkmark bullets, three pricing tiers, fake demos, soft oversized radius, purple and black, radial orbs, dot grids, sparkle icons, animated arrows, hover opacity fades, neon colors, basic pastels, em dashes, purple-to-blue gradients, gradient hero text, pill badge above hero, repeated icon rows, scroll fade-ins, cursor glow, grainy textures, Inter-only fonts, Space Grotesk plus Instrument Serif, generic SaaS buzzwords.

## Rules

- Maximum 2 font families. Warm off-white surface, never pure white.
- Real product demos only. Every CTA and form works.
- Test at 320, 360, 390, 768, 1024, 1440, 2560px. No horizontal scroll.
- Respect prefers-reduced-motion. Animations interruptible and reversible.
