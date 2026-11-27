# Legacy Compatibility

The skill is designed to run across a wide range of systems, from modern machines down to older legacy hardware. It degrades gracefully instead of failing hard.

## What runs where

| Part | Windows 7 32-bit / very old Linux / macOS | Modern systems |
|------|------------------------------------------|----------------|
| All Markdown knowledge (SKILL.md, references, subskills) | ✅ runs | ✅ runs |
| `scripts/audit.py` (Python 3.6+, stdlib-only) | ✅ runs (Python ≤3.8 on Win7) | ✅ runs |
| Browser-free craft scripts (`copy-lint.mjs`, `start.mjs`) | ✅ runs (Node 14+) | ✅ runs |
| Browser-dependent craft checks | ⚠️ **MANUAL path** | ✅ runs (Obscura or Chrome) |

## The only hard requirement

The **browser-dependent craft checks** (`gate.mjs`, `consistency.mjs`, `shoot.mjs`, `perf.mjs`, `moments.mjs shot`, `effects.mjs shot|perf`, `icons.mjs measure`, `assets/layout/check.mjs`, `assets/backgrounds/check.mjs`) need Node 22+ and a browser engine. They prefer **Obscura** and fall back to Chrome/Edge/Chromium.

This is a hard OS limitation, not a skill limitation:

- **Node 22+ prebuilts** require Windows 10+, macOS 13.5+, and Linux with glibc 2.28+.
- **Obscura** requires x86_64 (no 32-bit build) and, on Linux, glibc 2.35+ (Ubuntu 22.04+).
- **Chrome 110+** dropped Windows 7/8/8.1.

So on genuinely old systems (Windows 7 32-bit, very old Linux or macOS), no browser engine runs — and the browser-dependent checks use the MANUAL path. Everything else still runs.

## The MANUAL fallback

When no browser engine is present, the browser-dependent scripts do **not** crash. They print a MANUAL-mode message and exit with code 3. Follow the documented manual verification path:

1. Open the built page in any browser and screenshot it at **1440, 1024, 768, and 390 px**.
2. Check every item in the craft checklist (the craft `SKILL.md` "Checklist") by eye.
3. Read the copy aloud and lint it by eye, or run `copy-lint.mjs` (which needs no browser).
4. Record the result by hand as a GATE line: `GATE: MANUAL <tool> <pass|open>`.

## Check your environment

```bash
python3 zelvior-vibecoding-skill/scripts/compat.py
```

The compatibility probe checks Python, Node.js, and the browser engine (Obscura first, then Chrome/Edge/Chromium) and reports FULL, PARTIAL, or MANUAL mode. It is stdlib-only and runs on the same old systems the skill targets (Python 3.6+, including Python 3.8 on Windows 7).

## Installing a browser engine

**Obscura** (preferred by the craft launcher — a portable single-binary headless browser, ~70 MB, CDP-compatible):

- Download the release archive from its repository and put the `obscura` binary on `PATH`, or set `OBSCURA_PATH` to its executable.

**Chrome / Edge / Chromium** (fallback):

- Set `CHROME_PATH` to the browser executable, or leave it to be detected from the usual install locations.

## Browser-free craft scripts

These need no browser and run on Node 14+, so they work on older systems that still have a usable Node:

- `copy-lint.mjs` — copy lint.
- `start.mjs` — deal / css / brand.
- Browser-free subcommands of `effects.mjs` (`list`, `index`, `pick`, `gallery`, `publish`, `serve`), `moments.mjs` (`check`, `list`), and `icons.mjs` (`fetch`, `scan`).

## Summary

The skill is fully usable on ancient legacy devices. The automated headless-browser verification is the only part that needs a modern OS — and even that has a documented, reliable MANUAL fallback. Run `compat.py` on any machine to see exactly which mode it is in.
