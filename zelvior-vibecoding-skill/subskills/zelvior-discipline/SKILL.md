---
name: zelvior-discipline
description: >
  Behavioral guidelines to reduce common LLM coding mistakes. Use for essentially
  any coding or engineering task — writing, fixing, editing, refactoring,
  reviewing, debugging, reworking, or even thinking about code — to avoid
  overcomplication, keep changes surgical, surface assumptions instead of
  guessing, and define verifiable success criteria before looping. Applies to
  every build and every change, no matter how the user words it (e.g. "write
  this", "fix the bug", "refactor X", "review my code", "review this", "clean
  up this", "how should I approach this", "how do I do this", "keep it
  simple", "don't overcomplicate", "make sure it actually works", "is this
  right", "can you help me with this code").
---

# Zelvior Discipline

Behavioral guidelines that reduce the most common mistakes made when writing
code. Four principles, each addressing a known failure mode.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial
tasks (simple typo fixes, obvious one-liners), use judgment — not every
change needs the full rigor. The goal is reducing costly mistakes on
non-trivial work, not slowing down simple tasks.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes,
simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it
work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer
rewrites due to overcomplication, and clarifying questions come before
implementation rather than after mistakes.
