# Changelog

All notable changes to this project are documented here. This project adheres to [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-11-27

### Changed

- **Removed brand images** — deleted the `images/` folder (logo, banner,
  architecture diagram) and stripped all image references from the README,
  docs, and CHANGELOG.
- **Zelvior Labs attribution** — the project is now explicitly presented as
  made by **Zelvior Labs** across the README, docs, and llms.txt.

### Fixed

- **Ancient-Node support** — browser-dependent craft checks no longer crash on
  Node < 22. They degrade gracefully to the documented MANUAL mode (exit code
  3) when the global `WebSocket`/`fetch` are missing. A dependency-free `fetch`
  polyfill lets the network-download scripts (icons, photos) run on Node 14+.

### Added

- **`SECURITY.md`** — GitHub-recognized security policy.
- **`.github/FUNDING.yml`** — enables the Sponsor button.
- **GitHub issue templates** — bug report and feature request.

## [1.0.0] - 2026-11-27

### Added

- **Mega skill** (`zelvior-vibecoding-skill/SKILL.md`): a description-driven routing system that loads only the knowledge relevant to a given task.
- **12 deep-dive reference guides** (`references/01`–`12`): design system, anti-patterns, backend, frontend/data, SEO, security, performance, accessibility/mobile, CRO, DevOps/SRE, audit, and AI search.
- **138 checklists** across 5 checklist.design files (`references/13`–`17`): website page types, web-app screens, design-system foundations, mobile screens, and user flows.
- **236-test audit** across 32 modules, with a local `audit.py` checker (stdlib-only, Python 3.6+).
- **21 subskills** under `subskills/`:
  - Core knowledge: `zelvior-design`, `zelvior-backend`, `zelvior-security`, `zelvior-seo-performance`, `zelvior-devops`, `zelvior-audit`.
  - `zelvior-craft`: anti-slop frontend page skill with a real-browser finish gate.
  - `zelvior-lean` + siblings: lean minimal-change coding, review, audit, debt, gain, help.
  - `zelvior-ui`: UI styling router with principles, palettes, fonts, components, a11y.
  - `zelvior-discipline`: four behavioral coding principles with worked examples.
- **`compat.py`**: environment compatibility probe reporting FULL, PARTIAL, or MANUAL mode.
- **Assets**: `robots.txt`, `llms.txt`, `security.txt`, `sitemap.xml`, `404.html`.
- **Documentation**: `docs/architecture.md`, `docs/getting-started.md`, `docs/legacy-compatibility.md`.
- **Community files**: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, this `CHANGELOG.md`.
- **Broad trigger descriptions** across all 21 `SKILL.md` frontmatter fields, tuned to match how different people phrase tasks.
- **Ancient-Node compatibility**: browser-dependent craft checks now degrade gracefully to MANUAL mode on Node < 22 (missing `WebSocket`/`fetch` globals) instead of crashing; a dependency-free `fetch` polyfill lets the network-download scripts (icons, photos) run on Node 14+.
