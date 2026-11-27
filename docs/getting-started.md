# Getting Started

This guide walks through using the Zelvior Vibecoding Mega Skill end to end.

## 1. Check your environment

The skill runs across a wide range of systems. First, see what your machine can run:

```bash
python3 zelvior-vibecoding-skill/scripts/compat.py
```

It probes Python, Node.js, and the browser engine and reports one of three modes:

- **FULL** — the whole skill runs, including the automated browser checks.
- **PARTIAL** — the knowledge, `audit.py`, and browser-free craft scripts run; browser checks use the MANUAL path.
- **MANUAL** — the knowledge and `audit.py` run; craft browser scripts use the MANUAL path.

## 2. Read the mega skill

Start with the root skill. It is the entry point and contains the routing map:

```
zelvior-vibecoding-skill/SKILL.md
```

Read it first. It tells you which reference file or subskill to load for each kind of task. Do not load everything at once — load only what the task needs.

## 3. Pick the right reference or subskill

The routing map in `SKILL.md` ("How to use this skill") maps tasks to files:

| Task | Load |
|------|------|
| New site or redesign | `references/01`, `05`, `07`, `08`, `09` |
| Backend, API, database | `references/03`, `04` |
| Security review | `references/06` |
| DevOps, deploy | `references/10` |
| Audit / "is this done" | `references/11` + `scripts/audit.py` |
| AI search / llms.txt | `references/12` |
| A specific page or screen | the matching `references/13`–`17` checklist |
| A landing/company/product/game page | the `zelvior-craft` subskill |
| Smallest-change coding | the `zelvior-lean` subskill |
| Interface styling | the `zelvior-ui` router |
| How to approach any coding task | the `zelvior-discipline` subskill |

## 4. Run the audit

The local audit checker implements the highest-signal checks from all 32 modules. It is stdlib-only (Python 3.6+):

```bash
# Audit a live site
python3 zelvior-vibecoding-skill/scripts/audit.py https://example.com

# Audit a built file
python3 zelvior-vibecoding-skill/scripts/audit.py ./dist/index.html
```

## 5. Use the craft skill (optional)

The `zelvior-craft` subskill builds client-grade pages with a real-browser finish gate. Its scripts live in `subskills/zelvior-craft/scripts/`:

- `gate.mjs` — the finish gate (runs the browser checks, ends `GATE: PASS` or `GATE: OPEN`).
- `start.mjs` — deal/css/brand (browser-free).
- `copy-lint.mjs` — copy lint (browser-free).
- `consistency.mjs`, `shoot.mjs`, `perf.mjs`, `moments.mjs`, `effects.mjs`, `icons.mjs` — browser-dependent checks.

Browser-dependent checks prefer **Obscura** and fall back to Chrome/Edge/Chromium. If no engine is present, they print a MANUAL-mode message and exit code 3 — follow the documented manual path (screenshot at 1440/1024/768/390 px, check the checklist by eye, lint copy with `copy-lint.mjs`, record a `GATE: MANUAL <tool> <pass|open>` line).

## 6. Follow the discipline

The `zelvior-discipline` subskill applies to every build and change. Its four principles:

1. **Think Before Coding** — state assumptions, surface confusion, present tradeoffs.
2. **Simplicity First** — minimum code, nothing speculative.
3. **Surgical Changes** — touch only what's needed, match existing style.
4. **Goal-Driven Execution** — define verifiable success criteria, loop until verified.

See `subskills/zelvior-discipline/examples.md` for worked before/after examples.

## Workflow summary

1. Run `compat.py` to see what your environment supports.
2. Read `SKILL.md` for the routing map.
3. Load only the reference/subskill that matches the task.
4. Follow `zelvior-discipline` as you work.
5. Run `audit.py` to check the result.
6. If using craft, run the finish gate (`gate.mjs`) or follow the MANUAL path.
