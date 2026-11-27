# Architecture

The Zelvior Vibecoding Mega Skill — made by **Zelvior Labs** — is a **description-driven routing system** built on SKILL.md files. There is no hidden mechanism — the agent reads each file's `description` (the trigger) plus the routing maps written in the root `SKILL.md` and router subskills, then loads only the file(s) that match the current task.

## Three layers

### 1. The `description` field is the trigger

Every SKILL.md starts with YAML frontmatter. The `description` is the routing key the agent matches against the user's request:

```yaml
---
name: zelvior-craft
description: >-
  Zelvior Craft 2.5.1, the anti-slop frontend skill. Builds professional
  company websites... Use this for absolutely any request that involves
  ... a real, polished, made-for-the-client web page or site — no matter
  the wording, register, or phrasing.
---
```

The trigger language is deliberately broad: it covers many verbs, request framings ("I need", "can you", "help me", "how do I"), colloquial phrasings, and question forms, so it matches regardless of how the user words a request. Each subskill has its own trigger scope.

### 2. The root SKILL.md is the entry point and routing map

The mega-skill's frontmatter description is broad, so it loads first for any web/coding task. Its body contains a **"How to use this skill"** section that is an explicit routing map:

```
- New site or redesign: read references/01, 05, 07, 08, 09
- Backend/API work: read references/03, 04
- Build a landing page...: use the zelvior-craft subskill
- Smallest-change coding task: use the zelvior-lean subskill
- Interface styling: use the zelvior-ui router
- How to approach any coding task: use the zelvior-discipline subskill
```

A key rule near the top:

> Read this file first. Then load only the reference files you need for the task. Do not load everything at once.

The agent reads the routing map, matches the task against the descriptions, and loads only the matching file(s).

### 3. Router subskills switch one level deeper

Some subskills are themselves routers that switch to even more focused subskills. `zelvior-ui` is the clearest example — it contains a routing table:

| Task | Subskill to load |
|------|------------------|
| Spacing, layout, hierarchy | `zelvior-ui-principles/SKILL.md` |
| Picking colors | `zelvior-ui-palettes/SKILL.md` |
| Choosing fonts | `zelvior-ui-fonts/SKILL.md` |
| Building a component | `zelvior-ui-components/SKILL.md` |
| Accessibility/WCAG | `zelvior-ui-a11y/SKILL.md` |

For "build an accessible card with good colors and spacing", the agent loads the `zelvior-ui` router, reads the table, and loads all three matching subskills, then reconciles their rules (a11y and contrast win over aesthetics).

## The full flow

```
User: "build a landing page for a coffee shop"
  │
  ▼
Root SKILL.md loads (broad trigger: any web/coding task)
  │
  ▼
Agent reads "How to use this skill" routing map
  │
  ▼
Matches: "build a landing page" → zelvior-craft subskill
  │
  ▼
Agent loads zelvior-craft/SKILL.md (reads its description, confirms it fits)
  │
  ▼
Inside craft, if styling questions arise → zelvior-ui router → zelvior-ui-palettes etc.
```

## Directory layout

```
zelvior-vibecoding-skill/
├── SKILL.md                  # root mega skill + routing map
├── references/               # 12 deep-dive guides + 5 checklist.design files
│   ├── 01-design-system.md
│   ├── ...
│   └── 17-checklist-design-flows.md
├── scripts/
│   ├── audit.py              # local audit checker (Python 3.6+, stdlib)
│   └── compat.py             # environment compatibility probe
├── assets/                   # robots.txt, llms.txt, security.txt, sitemap.xml, 404.html
└── subskills/
    ├── zelvior-design/       # design system, patterns, anti-patterns
    ├── zelvior-backend/      # backend, APIs, data, realtime, scale
    ├── zelvior-security/     # security headers, auth, hardening
    ├── zelvior-seo-performance/
    ├── zelvior-devops/
    ├── zelvior-audit/
    ├── zelvior-craft/        # anti-slop frontend skill (full kit)
    │   ├── SKILL.md
    │   ├── references/       # craft reference docs
    │   ├── assets/           # layout, motion, UI, background, effect kits
    │   ├── library/          # palettes.json, type.json
    │   └── scripts/          # gate, start, moments, consistency, shoot, perf...
    ├── zelvior-lean/         # lean senior-dev mode
    ├── zelvior-lean-review/
    ├── zelvior-lean-audit/
    ├── zelvior-lean-debt/
    ├── zelvior-lean-gain/
    ├── zelvior-lean-help/
    ├── zelvior-ui/           # UI styling router
    ├── zelvior-ui-principles/
    ├── zelvior-ui-palettes/
    ├── zelvior-ui-fonts/
    ├── zelvior-ui-components/
    ├── zelvior-ui-a11y/
    └── zelvior-discipline/   # behavioral coding guidelines
```

## Design principles

1. **Load on demand.** Only the matching file is loaded — never everything at once. This keeps context focused and the skill fast.
2. **Broad triggers, narrow content.** The `description` is deliberately wide to catch varied phrasing; the loaded content is focused and deep.
3. **Routers compose.** A router subskill can fan out to multiple focused subskills and reconcile their rules.
4. **Graceful degradation.** Browser-dependent craft scripts fall back to a documented MANUAL path when no browser engine is available, instead of crashing.
