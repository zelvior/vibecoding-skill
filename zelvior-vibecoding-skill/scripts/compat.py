#!/usr/bin/env python3
"""Zelvior skill compatibility checker.

Answers one question: what can this skill actually run on THIS machine?

It probes the runtime this skill depends on — Python, Node.js, and a
browser engine (Obscura, or Chrome/Edge/Chromium as a fallback) — and
reports, per component, whether it is available and which mode you are in.
It is stdlib-only and runs on the same old systems the skill targets
(Python 3.6+, including Python 3.8 on Windows 7). No packages, no network.

Usage:
  python3 compat.py

Exit code: 0 if the full skill can run, 3 if only the manual path is
available, 1 if Python itself is too old to run this checker.
"""

import os
import shutil
import subprocess
import sys

# Chrome / Edge / Chromium locations probed on every platform.
CHROME_PATHS = [
    # env overrides
    os.environ.get("CHROME_PATH", ""),
    os.environ.get("CHROME", ""),
    # Windows
    os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe"),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    # Linux
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
]

# Obscura: a portable single-binary headless browser (CDP-compatible).
# Checked before Chrome because the craft launcher prefers it.
OBSCURA_PATHS = [
    os.environ.get("OBSCURA_PATH", ""),
    os.environ.get("OBSCURA", ""),
    "/opt/homebrew/bin/obscura",
    "/usr/local/bin/obscura",
    "/usr/bin/obscura",
    "/opt/obscura/obscura",
]


def py_major():
    return int(sys.version_info[0]), int(sys.version_info[1])


def run(cmd):
    """Run a command, return (ok, stdout_text). Never raises."""
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
        return p.returncode == 0, (p.stdout or "").strip()
    except (OSError, ValueError):
        return False, ""


def node_major():
    """Return (found, major) for the node on PATH, or (False, None)."""
    exe = shutil.which("node") or shutil.which("nodejs")
    if not exe:
        return False, None
    ok, out = run([exe, "--version"])
    if not ok or not out:
        return False, None
    # "v22.22.3" -> 22 (take the major before the first dot)
    first = out.split()[0].lstrip("v")
    major_str = first.split(".")[0]
    return True, (int(major_str) if major_str.isdigit() else None)


def obscura_path():
    """Return the first Obscura binary that exists, or None."""
    for p in OBSCURA_PATHS:
        if p and os.path.isfile(p):
            return p
    exe = shutil.which("obscura")
    if exe:
        return exe
    return None


def chrome_path():
    """Return the first Chrome/Edge/Chromium that exists, or None."""
    for p in CHROME_PATHS:
        if p and os.path.isfile(p):
            return p
    # fall back to a PATH lookup
    for name in ("google-chrome", "google-chrome-stable", "chromium",
                 "chromium-browser", "chrome", "msedge"):
        exe = shutil.which(name)
        if exe:
            return exe
    return None


def ok(label, detail):
    print("  [ OK ] {:26} {}".format(label, detail))


def warn(label, detail):
    print("  [WARN] {:26} {}".format(label, detail))


def bad(label, detail):
    print("  [FAIL] {:26} {}".format(label, detail))


def main():
    major, minor = py_major()
    print("Zelvior skill — environment compatibility")
    print("=" * 60)

    if major < 3 or (major == 3 and minor < 6):
        bad("Python", "{}.{} — need 3.6+ to run this checker".format(major, minor))
        print("\nThis checker itself needs Python 3.6+. The skill's knowledge")
        print("(all Markdown) still reads on any system; only the Python tools")
        print("need a newer Python.")
        return 1
    ok("Python", "{}.{} (checker + audit.py need 3.6+)".format(major, minor))

    # --- Node ---
    n_found, n_major = node_major()
    if not n_found:
        bad("Node.js", "not installed")
    elif n_major is not None and n_major >= 22:
        ok("Node.js", "v{} (full browser checks)".format(n_major))
    elif n_major is not None and n_major >= 14:
        warn("Node.js", "v{} (browser-free scripts run; browser checks need 22+)".format(n_major))
    else:
        bad("Node.js", "v{} too old (ESM needs 14+)".format(n_major))

    # --- Browser engine (Obscura preferred, Chrome fallback) ---
    obscura = obscura_path()
    chrome = chrome_path()
    if obscura:
        ok("Browser", "Obscura ({})".format(obscura))
    elif chrome:
        ok("Browser", chrome)
    else:
        bad("Browser", "no Obscura, Chrome/Edge/Chromium found (set OBSCURA_PATH or CHROME_PATH)")

    # --- Mode ---
    print("-" * 60)
    node_ok = n_found and n_major is not None and n_major >= 22
    browser_ok = obscura is not None or chrome is not None
    if node_ok and browser_ok:
        mode = "FULL"
        print("Mode: FULL — the whole skill runs, including the automated")
        print("      browser checks (craft gate, consistency, layout, perf).")
        exit_code = 0
    elif n_found and n_major is not None and n_major >= 14:
        mode = "PARTIAL"
        print("Mode: PARTIAL — the skill's knowledge, audit.py, and the")
        print("      browser-free craft scripts (copy-lint, start, deal) run.")
        print("      The browser checks fall back to the documented MANUAL path.")
        exit_code = 3
    else:
        mode = "MANUAL"
        print("Mode: MANUAL — the skill's knowledge and audit.py run; the")
        print("      craft browser scripts cannot run here. Use the documented")
        print("      manual verification path (screenshot + checklist by eye).")
        exit_code = 3

    print("-" * 60)
    print("What runs on this machine:")
    print("  * All Markdown knowledge (SKILL.md, references, all subskills): YES")
    print("  * scripts/audit.py (Python 3.6+, stdlib only):                  YES")
    if n_found and n_major is not None and n_major >= 14:
        print("  * Craft browser-free scripts (copy-lint, start, deal):        YES")
    else:
        print("  * Craft browser-free scripts (copy-lint, start, deal):        no Node")
    if node_ok and browser_ok:
        print("  * Craft browser checks (gate, consistency, layout, perf):     YES")
    else:
        print("  * Craft browser checks (gate, consistency, layout, perf):     manual")
    print("\nBrowser checks are the only part that needs a modern OS: Node 22+")
    print("and a browser engine need Windows 10+, macOS 13.5+ (for current")
    print("Node prebuilts), and a recent Linux (glibc 2.28+). Obscura is a")
    print("portable single-binary engine (preferred by the craft launcher);")
    print("Chrome/Edge/Chromium is the fallback. On older systems the skill")
    print("still works via the MANUAL path described in the craft SKILL.md.")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
