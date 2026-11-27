# Zelvior Vibecoding Mega Skill

**Made by Zelvior Labs.**

![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Node](https://img.shields.io/badge/Node-22%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-web%20%26%20cli-informational)
![Skills](https://img.shields.io/badge/skills-21%20subskills-9b59b6)
![Checklists](https://img.shields.io/badge/checklists-138-7c3aed)
![Audit](https://img.shields.io/badge/audit-236%20tests-e8590c)

**A senior-level mega skill for building production websites and apps that pass a strict, opinionated audit.** It merges design patterns, backend architecture, security hardening, Core Web Vitals, accessibility, CRO, AI-search readiness, a 236-test audit across 32 modules, 138 page/screen/design-system/flow checklists, an anti-slop frontend craft skill, a lean minimal-change coding mode, a UI styling knowledge set, and behavioral coding guidelines — into one description-driven routing system.

The skill works with any coding agent that reads `SKILL.md` files (Claude Skills and compatible agents). Point it at a task and it routes itself to only the knowledge it needs — never dumping everything at once.

## Why this exists

Most "vibe coding" produces slop: pretty pages that fail accessibility, slow Core Web Vitals, missing security headers, and copy that reads like a template. This skill is the antidote — a single routing system that loads the right senior-level checklist for the job and verifies the result against a strict audit.

**What you get, at a glance:**

| | |
|---|---|
| 🧭 **Routing mega skill** | One `SKILL.md` entry point; trigger-driven, loads only what's needed |
| 📚 **12 deep-dive guides** | Design, backend, frontend, SEO, security, performance, a11y, CRO, DevOps, audit, AI search |
| ✅ **138 checklists** | Every page, screen, flow, and design-system component — as required tests |
| 🔍 **236-test audit** | Local `audit.py` + a full manual checklist across 32 modules |
| 🎨 **Anti-slop craft skill** | Real-browser finish gate for client-grade landing/product/game pages |
| 🪶 **Lean coding mode** | Smallest change that fully solves the task |
| 🎯 **Behavioral discipline** | Four principles that govern how every change is made |

## Connect with Zelvior Labs

Find Zelvior Labs and support the project across the web:

| | |
|---|---|
| [![npm](https://img.shields.io/badge/npm-zelnpm-cb3837?style=for-the-badge)](https://www.npmjs.com/~zelnpm) | [![ORCID](https://img.shields.io/badge/ORCID-0009--0009--2376--367X-4c8c66?style=for-the-badge)](https://orcid.org/0009-0009-2376-367X) |
| [![YouTube](https://img.shields.io/badge/YouTube-zelviorhere-ff0000?style=for-the-badge)](https://youtube.com/@zelviorhere) | [![Linktree](https://img.shields.io/badge/Linktree-zelvior-1db954?style=for-the-badge)](https://linktr.ee/zelvior) |
| [![Discord](https://img.shields.io/badge/Discord-Zelvior-5865f2?style=for-the-badge)](https://discord.gg/UQfzQzymc) | [![Donate](https://img.shields.io/badge/Donate-Zelvior-f38029?style=for-the-badge)](https://nowpayments.io/donation/zelviorhere) |
| [![X](https://img.shields.io/badge/X-zelviorhere-000000?style=for-the-badge)](https://x.com/zelviorhere) | [![Website](https://img.shields.io/badge/Website-zelviorlabs-6366f1?style=for-the-badge)](https://zelviorlabs.vercel.app) |
| [![Blog](https://img.shields.io/badge/Blog-zelvior-ff8c00?style=for-the-badge)](https://zelvior.blogspot.com) | [![GitHub Org](https://img.shields.io/badge/GitHub%20Org-ZelviorLabs-181717?style=for-the-badge)](https://github.com/Zelvior-Labs) |
| [![GitHub](https://img.shields.io/badge/GitHub-zelvior-181717?style=for-the-badge)](https://github.com/zelvior) | |

## Table of contents

- [How it works](#how-it-works)
- [What is inside](#what-is-inside)
- [Connect with Zelvior Labs](#connect-with-zelvior-labs)
- [Quick start](#quick-start)
- [Legacy compatibility](#legacy-compatibility)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## How it works

The skill is a **description-driven routing system**. The root `SKILL.md` is the entry point; each `description` in a SKILL.md's frontmatter is the trigger that decides when a skill loads. The agent reads the routing map, matches the task against the triggers, and loads only the matching file — never everything at once.

```
User request
  │
  ▼
Root SKILL.md loads (broad trigger: any web/coding task)
  │
  ▼
Agent reads the "How to use this skill" routing map
  │
  ▼
Matches the task → loads the matching reference(s) and/or subskill(s)
  │
  ▼
Router subskills (e.g. zelvior-ui) switch one level deeper to focused subskills
```

## What is inside

### The mega skill

- `zelvior-vibecoding-skill/SKILL.md` — the root mega skill. Design must-haves and banned patterns, backend/frontend/data functionality, security, SEO, performance, accessibility, CRO, DevOps, the definition of done, and the routing map that loads the right reference or subskill for each task.

### Reference guides (`references/`)

12 deep-dive guides plus 5 checklist.design files (138 checklists total — every item is a required test, nothing is optional):

| # | File | Covers |
|---|------|--------|
| 01 | `01-design-system.md` | Design must-have patterns |
| 02 | `02-anti-patterns.md` | Copy, brand, and anti-vibe-coded checks |
| 03 | `03-backend.md` | Backend, APIs, databases, realtime, scale |
| 04 | `04-frontend-data.md` | Frontend and data work |
| 05 | `05-seo-technical.md` | SEO and technical health |
| 06 | `06-security.md` | Security review and hardening |
| 07 | `07-performance.md` | Performance and Core Web Vitals |
| 08 | `08-accessibility-mobile.md` | Accessibility and mobile |
| 09 | `09-cro-content.md` | CRO, content, and brand |
| 10 | `10-devops-sre.md` | DevOps and SRE |
| 11 | `11-audit-checklist.md` | The 236-test audit checklist across 32 modules |
| 12 | `12-ai-search-agents.md` | AI search, agents, and llms.txt |
| 13 | `13-checklist-design-website.md` | 27 website page types |
| 14 | `14-checklist-design-web-app.md` | 38 web-app screens |
| 15 | `15-checklist-design-design-system.md` | 32 design-system foundations and components |
| 16 | `16-checklist-design-mobile.md` | 28 mobile screens and patterns |
| 17 | `17-checklist-design-flows.md` | 13 user flows |

### Subskills (`subskills/`)

Standalone skills for focused work. Each has its own `SKILL.md` with a trigger `description`.

**Core knowledge subskills:**

- `zelvior-design/SKILL.md` — design system, patterns, and anti-patterns.
- `zelvior-backend/SKILL.md` — backend, APIs, data, realtime, and scale.
- `zelvior-security/SKILL.md` — security headers, auth, and hardening.
- `zelvior-seo-performance/SKILL.md` — SEO, performance, and Core Web Vitals.
- `zelvior-devops/SKILL.md` — CI/CD, infra, deploys, and SRE.
- `zelvior-audit/SKILL.md` — the 236-test audit checklist and how to run it.

**zelvior-craft — anti-slop frontend page skill:**

Builds client-grade landing, company, product, and game pages from a dealt system, with a real-browser checker and finish gate. Full kit lives in `subskills/zelvior-craft/`:

- `references/` — craft reference docs (layout, motion, UI, background, effect, object, moment, scene, diagram, icon, copy, system, gate, perf).
- `assets/` — layout, motion, UI, background, effect, object, moment, scene, diagram, icon, and component kits with starter templates (`starter.html`, `system.css`, `system.js`).
- `library/` — design tokens (`palettes.json`, `type.json`).
- `scripts/` — `gate.mjs` (finish gate), `start.mjs` (deal/css/brand), `moments.mjs`, `copy-lint.mjs`, `consistency.mjs`, `shoot.mjs`, `perf.mjs`, `icons.mjs`, `photos.mjs`, `effects.mjs`, and the shared `_legacy.mjs` launcher.

**zelvior-lean — lean senior-dev mode:**

The smallest change that fully solves the task. Siblings: `zelvior-lean-review` (ranked quality review), `zelvior-lean-audit` (ranked one-shot repo audit), `zelvior-lean-debt` (shortcut debt ledger), `zelvior-lean-gain` (measured savings), `zelvior-lean-help` (quick reference).

**zelvior-ui — UI styling router:**

Routes interface styling work to focused subskills: `zelvior-ui-principles` (hierarchy, whitespace, layout), `zelvior-ui-palettes` (12 color palettes), `zelvior-ui-fonts` (typeface catalog), `zelvior-ui-components` (component patterns), `zelvior-ui-a11y` (WCAG 2.2 A + AA).

**zelvior-discipline — behavioral coding guidelines:**

Four principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) that apply to every build and change. Includes `examples.md` with worked before/after code examples.

### Scripts (`scripts/`)

- `audit.py` — local audit script implementing the highest-signal checks from all 32 modules. Stdlib-only, Python 3.6+.
- `compat.py` — environment compatibility probe. Checks Python, Node.js, and the browser engine, and reports FULL, PARTIAL, or MANUAL mode. Stdlib-only.

### Assets (`assets/`)

Ready-to-use web templates: `robots.txt`, `llms.txt`, `security.txt`, `sitemap.xml`, and `404.html`.

### Docs (`docs/`)

- `docs/architecture.md` — the skill architecture in depth.
- `docs/getting-started.md` — how to use the skill, end to end.
- `docs/legacy-compatibility.md` — what runs on which OS, and the MANUAL fallback.

## Quick start

```bash
# Check what your environment can run
python3 zelvior-vibecoding-skill/scripts/compat.py

# Audit a live site or a built file
python3 zelvior-vibecoding-skill/scripts/audit.py https://example.com
python3 zelvior-vibecoding-skill/scripts/audit.py ./dist/index.html
```

Read `zelvior-vibecoding-skill/SKILL.md` first, then load only the reference files and subskills you need for the task. See `docs/getting-started.md` for the full workflow.

## Legacy compatibility

The skill degrades gracefully on older systems instead of failing hard:

- **Always runnable** — all Markdown knowledge and `audit.py` (Python 3.6+).
- **Browser-free craft scripts** (`copy-lint.mjs`, `start.mjs`) — run on Node 14+.
- **Network-download scripts** (`icons.mjs fetch`, `photos.mjs search/fetch`) — run on Node 14+ via a built-in, dependency-free `fetch` polyfill.
- **Browser-dependent craft checks** — run automated checks on Node 22+ with a browser engine (**Obscura** preferred, falling back to Chrome/Edge/Chromium). On older Node or without an engine, they **never crash**: they print a MANUAL-mode message and exit code 3, and you follow the documented manual verification path.

See `docs/legacy-compatibility.md` for the full breakdown and `python3 zelvior-vibecoding-skill/scripts/compat.py` for a per-machine report.

## Documentation

- [Architecture](docs/architecture.md) — how the routing system and skill structure work.
- [Getting started](docs/getting-started.md) — the end-to-end workflow.
- [Legacy compatibility](docs/legacy-compatibility.md) — OS support and the MANUAL fallback.

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). This project follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[GPL-3.0](LICENSE). See [LICENSE](LICENSE).
