# Anti-Patterns: Banned Design and Copy

Never use these in any build. If found in existing code, remove them. This list merges the Zelvior avoid list with the Audityxe vibe-coded signals module.

## Visual bans

- Harsh gradients, purple-to-blue gradients, gradient hero text. Use flat, confident color.
- Lucide icons. Use custom or brand icons.
- Pure white background. Use a warm off-white or tinted surface.
- Rainbow coloring. One restrained palette.
- Drop shadows as decoration. Use borders and surface tints.
- Three feature cards in a row or column. Vary layout: editorial, asymmetric, or single-column with real content.
- Emojis in production UI. No emoji in headings, buttons, or body copy.
- Liquid glass or glassmorphism. No frosted glass panels.
- Terminal window mockups. Show real product UI instead.
- Soft corner radius (20px+ on cards). Small, deliberate radii with continuous corners.
- Purple and black color schemes. Choose a distinctive, ownable palette.
- Radial orbs. No decorative glowing blobs.
- Dot grids. No dotted background patterns.
- Sparkle icons. No star or sparkle decoration.
- Animated arrows. Arrows are static or absent.
- Hover animations that fade opacity on buttons. Buttons change state crisply, not by fading.
- Neon colors. No high-saturation glow palettes.
- Basic pastel colors. No washed-out generic palettes.
- Grainy canvas texture overlays. No noise textures.
- Cursor-following glow or particles. No mouse trails.
- Scroll-triggered fade-in animations. Content is visible by default.
- Pill badge above hero headline. No "New" pills floating over headlines.
- Repeated icon rows. No rows of identical icons as decoration.
- Inter-only font stack. No Space Grotesk plus Instrument Serif pairing.

## Copy bans

- Em dashes in copy. Use periods, commas, or colons. The audit flags 16+ em dashes as an AI tell. Use zero.
- "It's not X, it's Y" constructions. Say what it is directly.
- Checkmark bullets. Use real lists with real content, not checkmark decoration.
- Three pricing tiers. Price honestly: one plan, usage-based, or as many tiers as the product needs.
- Generic SaaS buzzwords: delve, elevate, unlock, supercharge, seamless, cutting-edge, revolutionary, game-changer, leverage, empower, unleash, transform your workflow, next-generation, world-class, best-in-class, state-of-the-art.
- Placeholder or lorem ipsum copy. Every word ships real.
- No real product demos. Every demo must be a working product surface, not a mockup.

## Code and SEO bans

- Empty view-source. Public pages must contain real server-rendered content.
- No 404 page. Ship a custom branded 404.
- Vite plus React browser-only SPA for public pages. Use SSR or pre-rendering.
- Same page titles. Every page has a unique title.
- No meta descriptions. Every page has one.
- No per-page og:images. Every page has a share image that loads.
- No structured data. Ship valid JSON-LD.
- Multiple H1s or no H1. Exactly one H1 per page.
- No canonical tag. Every page has one.
- No llms.txt. Ship it with real content.
- No sitemap.xml. Ship it, valid, with lastmod.
- No lang attribution. Declare lang on html.
- No favicon. Ship favicon, Apple touch icon, and manifest.
- Missing alt texts. Every content image has descriptive alt.
- Exposed source maps. Never ship .js.map files.
- Console errors. Zero in production.
- Massive JS bundles. Split, tree-shake, defer.
- No privacy policy, terms, contact, or license page. All four are mandatory.
- Exposed logs, secrets, or stack traces. Never.

## How to replace each ban

- Gradient hero text becomes solid display type with strong contrast.
- Glassmorphism becomes a solid surface with a border.
- Three feature cards become one strong feature section with real screenshots or demos.
- Checkmark bullets become a plain list with specific, verifiable claims.
- Three pricing tiers become honest pricing that matches the product.
- Terminal window becomes a real product screenshot or live demo.
- Radial orbs and dot grids become clean whitespace and typography.
- Animated arrows and hover fades become instant, crisp state changes.
- Em dashes become periods. Short sentences. Plain words.
