# Contributing to Zelvior Vibecoding Mega Skill

Thanks for taking the time to contribute. This is a routing mega skill — the goal is to keep the knowledge high-signal, the triggers broad, and the checklists strict.

## Ways to contribute

- **Improve a reference guide** in `zelvior-vibecoding-skill/references/`.
- **Add or sharpen a checklist item** in the checklist.design files (`references/13`–`17`).
- **Improve a subskill** under `subskills/`.
- **Broaden a trigger** in a `SKILL.md` frontmatter `description` so it matches more ways people phrase tasks.
- **Improve the scripts** in `scripts/` (keep them stdlib-only where possible).
- **Report a gap or bug** in an existing guide or checklist.

## Guidelines

- **Keep triggers broad.** A skill should load whenever someone asks for anything even loosely like its topic. Don't assume canonical wording — cover varied verbs, casual phrasings, and registers.
- **Checklists are required tests.** Every item in a checklist is something that must pass. Don't add soft or optional items.
- **Stay on-brand.** Use the `zelvior-*` naming convention for subskills. Do not introduce upstream brand names.
- **No slop.** Follow the discipline yourself: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Match the existing style of the file you edit.
- **Keep scripts portable.** `audit.py` and `compat.py` are stdlib-only and target Python 3.6+. Browser-dependent craft scripts target Node 22+.

## Making a change

1. Fork and create a branch.
2. Make your change. If you edit any `SKILL.md` frontmatter `description`, run a quick duplicate-word sanity check on the changed lines.
3. If you change a script, verify it runs on a plain environment.
4. Open a pull request describing the change and why.

## Reporting issues

Open an issue describing what you expected, what you observed, and the task or reference involved. Including a concrete example helps a lot.

## Code of conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). Be kind, be specific, and assume good intent.
