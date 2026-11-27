---
name: zelvior-lean-help
description: >
  Quick reference for zelvior-lean levels, skills and commands. One-shot display.
  Use for /zelvior-lean-help, "zelvior-lean help", "how do I use zelvior-lean".
---

# Zelvior-Lean Help

Display this reference card when invoked. One-shot, do NOT change mode,
write flag files, or persist anything.

## Levels

| Level | Trigger | What change |
|-------|---------|-------------|
| **Lite** | `/zelvior-lean lite` | Build what was asked, name the smaller option in one line. |
| **Full** | `/zelvior-lean` | The smallest complete change, a check where the logic needs one, and a reply that names what was skipped and any risk. Default. |
| **Ultra** | `/zelvior-lean ultra` | Also questions the request and pushes back before building. |

Level sticks until changed or session end.

## Skills

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **zelvior-lean** | `/zelvior-lean` | Lazy mode itself: least new code, clear replies that name skipped work and risks. |
| **zelvior-lean-review** | `/zelvior-lean-review` | Quality review of a diff: bugs, security, load, missing tests, speed, what to cut. Each finding says what goes wrong and how to fix it. |
| **zelvior-lean-audit** | `/zelvior-lean-audit` | The same quality review for the whole repo, ranked. |
| **zelvior-lean-debt** | `/zelvior-lean-debt` | Harvest `shortcut:` comments into a tracked ledger. |
| **zelvior-lean-gain** | `/zelvior-lean-gain` | Measured-impact scoreboard: less code, less cost, more speed. |
| **zelvior-lean-help** | `/zelvior-lean-help` | This card. |

In Codex CLI and the IDE extension, invoke skills with `$zelvior-lean:zelvior-lean`,
`$zelvior-lean:zelvior-lean-review`, or `$zelvior-lean:zelvior-lean-help`. Claude Code and OpenCode use the
slash-command forms above (OpenCode ships all six as slash commands).

## Deactivate

Say "stop zelvior-lean" or "normal mode". Resume anytime with `/zelvior-lean`.
`/zelvior-lean off` also works.

## Band (Claude Code)

`/zelvior-lean band` hides the band above the prompt, the same command brings it back.
`/zelvior-lean band on` and `/zelvior-lean band off` set it directly. The level stays.
`/zelvior-lean band import` adds your past Claude Code sessions (cost, agent time, tokens) to the board.

## Configure Default Mode

Default mode = `full`, auto-active every session. Change it:

**Environment variable** (highest priority):
```bash
export ZELVIOR_LEAN_DEFAULT_MODE=ultra
```

**Config file** (`~/.config/zelvior-lean/config.json`, Windows: `%APPDATA%\zelvior-lean\config.json`):
```json
{ "defaultMode": "lite" }
```

Set `"off"` to disable auto-activation on session start, activate manually
with `/zelvior-lean` when wanted.

Resolution: env var > config file > `full`.

## Update

Enable auto-update once: open `/plugin`, go to Marketplaces, pick zelvior-lean, Enable auto-update. Claude Code then pulls new versions at startup (run `/reload-plugins` when it prompts). Manual refresh: `/plugin marketplace update zelvior-lean` then `/reload-plugins`.

If `/plugin` is not recognized, your Claude Code is out of date. Update it (`npm install -g @anthropic-ai/claude-code@latest`, or `brew upgrade claude-code`) and restart. Other hosts use their own update flow.

## More

This reference card ships inside zelvior-vibecoding-skill. Load the
`zelvior-lean` skill for the mode itself and its siblings for review, audit,
debt, and gain.
