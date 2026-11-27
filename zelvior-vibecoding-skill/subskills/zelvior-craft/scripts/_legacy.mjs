// Shared legacy-compatibility preflight for zelvior-craft browser scripts.
//
// The browser-driven checks (visual consistency, layout, perf, screenshots,
// the finish gate) need a modern Node and a browser engine. On hosts where
// those are absent — e.g. Windows 7 32-bit, very old Linux or macOS —
// this prints a clear MANUAL-mode message and exits with code 3, so the
// caller falls back to the documented manual verification path instead of
// crashing with a raw "no Chrome found" error.
//
// requireChrome() returns the Chrome path when the host can run the browser
// checks, or exits gracefully when it cannot. It is a safe superset of every
// Chrome-detection path the individual scripts already use.
//
// launchBrowser() is the shared engine launcher: it prefers Obscura (a
// lightweight single-binary headless browser, CDP-compatible with Chrome)
// and falls back to Chrome / Edge / Chromium. Both engines expose the same
// CDP HTTP endpoints (/json/version, /json/list), so the caller's existing
// fetch → WebSocket → CDP code works unchanged regardless of engine.

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import http from 'node:http';
import https from 'node:https';
import zlib from 'node:zlib';
import { spawn, spawnSync } from 'node:child_process';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- Obscura
// A portable single-binary headless browser (Rust + V8, CDP-compatible).
// Detected from OBSCURA_PATH, common install locations, and PATH.
function obscuraCandidates() {
  const home = (os.homedir && os.homedir()) || process.env.HOME || '';
  const list = [
    process.env.OBSCURA_PATH,
    process.env.OBSCURA,
    // portable copy next to the skill or in the working directory
    path.join(path.dirname(new URL(import.meta.url).pathname), 'obscura'),
    path.join(path.dirname(new URL(import.meta.url).pathname), 'obscura.exe'),
    path.join(process.cwd(), 'obscura'),
    path.join(process.cwd(), 'obscura.exe'),
    // Scoop (Windows) / Homebrew (macOS) / common install dirs
    home ? path.join(home, 'scoop/shims/obscura.exe') : null,
    '/opt/homebrew/bin/obscura',
    '/usr/local/bin/obscura',
    '/usr/bin/obscura',
    '/opt/obscura/obscura',
  ].filter(Boolean);
  return list;
}

export function findObscura() {
  const hit = obscuraCandidates().find((p) => fs.existsSync(p));
  if (hit) return hit;
  // search PATH (which/where)
  const finder = process.platform === 'win32' ? 'where' : 'which';
  const r = spawnSync(finder, ['obscura'], { encoding: 'utf8' });
  if (r.status === 0 && r.stdout) {
    const first = r.stdout.split(/\r?\n/).map((s) => s.trim()).filter(Boolean)[0];
    if (first) return first;
  }
  return null;
}

// ---------------------------------------------------------------- Chrome
// Every Chrome / Edge / Chromium location any craft script looks for.
function chromeCandidates() {
  const home = (os.homedir && os.homedir()) || process.env.HOME || '';
  const local = process.env.LOCALAPPDATA
    ? path.join(process.env.LOCALAPPDATA, 'Google/Chrome/Application/chrome.exe')
    : null;
  return [
    process.env.CHROME_PATH,
    process.env.CHROME,
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    local,
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    home ? path.join(home, 'Applications/Google Chrome.app/Contents/MacOS/Google Chrome') : null,
    '/usr/bin/google-chrome',
    '/usr/bin/google-chrome-stable',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/snap/bin/chromium',
  ].filter(Boolean);
}

export function findChrome() {
  return chromeCandidates().find((p) => fs.existsSync(p)) || null;
}

// The preferred engine: Obscura if present, else Chrome. Returns
// { engine, path } or null when neither is available.
export function findEngine() {
  const obs = findObscura();
  if (obs) return { engine: 'obscura', path: obs };
  const chrome = findChrome();
  if (chrome) return { engine: 'chrome', path: chrome };
  return null;
}

export function nodeMajor() {
  return parseInt(String(process.versions.node).split('.')[0], 10) || 0;
}

// ---------------------------------------------------------------- ancient-Node compat
// The browser-driven checks use the global `WebSocket` (a global since Node
// 22) and `fetch` (a global since Node 18). On older Node those globals are
// absent, so the checks would crash with a raw "WebSocket is not defined"
// error. requireBrowserGlobals() turns that crash into the documented MANUAL
// fallback (exit code 3) so the skill degrades gracefully on any Node.
export function requireBrowserGlobals(tool) {
  const missing = [];
  if (typeof globalThis.WebSocket === 'undefined') missing.push('WebSocket (Node 22+)');
  if (typeof globalThis.fetch === 'undefined') missing.push('fetch (Node 18+)');
  if (missing.length) {
    return manual(tool, `Node ${process.versions.node || 'unknown'} lacks the global(s) the browser check needs: ${missing.join(', ')}.`);
  }
  return true;
}

// A minimal, dependency-free fetch for Node < 18, so the network-download
// scripts (icons, photos) still run on ancient Node. Handles http/https
// GET/HEAD, follows redirects, decompresses gzip/deflate/br, and returns a
// Response-like object with text()/json()/arrayBuffer() and headers.get().
// Also polyfills AbortController / AbortSignal.timeout when absent.
function makeSignal(controller) {
  const listeners = new Set();
  const signal = {
    aborted: controller._aborted,
    reason: undefined,
    addEventListener(type, fn) { if (type === 'abort' && !controller._aborted) listeners.add(fn); },
    removeEventListener(type, fn) { listeners.delete(fn); },
    dispatchEvent(ev) { for (const fn of listeners) fn(ev); return true; },
  };
  signal._fire = (reason) => { signal.aborted = true; signal.reason = reason; for (const fn of listeners) fn({ type: 'abort', reason }); listeners.clear(); };
  return signal;
}

function minimalFetch(input, init = {}) {
  return new Promise((resolve, reject) => {
    let url;
    try { url = new URL(typeof input === 'string' ? input : input.url); }
    catch { reject(new TypeError('invalid URL: ' + input)); return; }
    const method = (init.method || 'GET').toUpperCase();
    const headers = Object.assign({}, init.headers || {});
    const maxRedirects = 10;
    const doReq = (u, redirects) => {
      const lib = u.protocol === 'https:' ? https : http;
      const req = lib.request(u, { method, headers, redirect: 'manual' }, (res) => {
        const status = res.statusCode || 0;
        if ([301, 302, 303, 307, 308].includes(status) && res.headers.location && redirects < maxRedirects) {
          res.resume();
          let next; try { next = new URL(res.headers.location, u); } catch { reject(new TypeError('bad redirect')); return; }
          doReq(next, redirects + 1); return;
        }
        const chunks = [];
        res.on('data', (c) => chunks.push(c));
        res.on('end', () => {
          let body = Buffer.concat(chunks);
          const enc = String(res.headers['content-encoding'] || '').toLowerCase();
          try {
            if (enc === 'gzip') body = zlib.gunzipSync(body);
            else if (enc === 'deflate') body = zlib.inflateSync(body);
            else if (enc === 'br') body = zlib.brotliDecompressSync(body);
          } catch { /* leave as-is */ }
          const headersObj = {
            get(k) { const v = res.headers[String(k).toLowerCase()]; return Array.isArray(v) ? v[0] : v; },
          };
          resolve({
            ok: status >= 200 && status < 300,
            status,
            statusText: res.statusMessage || '',
            headers: headersObj,
            text: () => Promise.resolve(body.toString('utf8')),
            json: () => Promise.resolve(body.toString('utf8')).then((t) => JSON.parse(t)),
            arrayBuffer: () => Promise.resolve(body.buffer.slice(body.byteOffset, body.byteOffset + body.byteLength)),
          });
        });
      });
      const signal = init.signal;
      if (signal && typeof signal.addEventListener === 'function') {
        signal.addEventListener('abort', () => { try { req.destroy(); } catch { /* gone */ } }, { once: true });
      }
      req.on('error', reject);
      req.end();
    };
    doReq(url, 0);
  });
}

// Installs the fetch / AbortController / AbortSignal.timeout polyfills only
// where they are missing. Safe to call on any Node version.
export function installFetchCompat() {
  if (typeof globalThis.fetch !== 'function') globalThis.fetch = minimalFetch;
  if (typeof globalThis.AbortController === 'undefined') {
    globalThis.AbortController = class AbortController {
      constructor() { this._aborted = false; this.signal = makeSignal(this); }
      abort(reason) { if (this._aborted) return; this._aborted = true; this.signal._fire(reason); }
    };
  }
  if (typeof globalThis.AbortSignal === 'undefined') globalThis.AbortSignal = {};
  if (typeof globalThis.AbortSignal.timeout !== 'function') {
    globalThis.AbortSignal.timeout = (ms) => {
      const ac = new globalThis.AbortController();
      const t = setTimeout(() => ac.abort(new Error('aborted after ' + ms + 'ms')), ms);
      if (t.unref) t.unref();
      return ac.signal;
    };
  }
}

// Returns the Chrome path if the host can run the browser checks; otherwise
// prints a manual-mode message and exits with code 3. The browser checks need
// Node 14+ (ESM), the global WebSocket (Node 22+) and fetch (Node 18+), and a
// browser engine — any missing piece routes to the MANUAL fallback.
export function requireChrome(tool) {
  const major = nodeMajor();
  if (major < 14) {
    return manual(tool, `Node ${process.versions.node || 'unknown'} is too old (ESM needs Node 14+).`);
  }
  requireBrowserGlobals(tool);
  const eng = findEngine();
  if (!eng) {
    return manual(tool, 'no Obscura, Chrome, Edge or Chromium found (set OBSCURA_PATH or CHROME_PATH to its executable).');
  }
  return eng.path;
}

function manual(tool, reason) {
  console.error('');
  console.error(`[zelvior-craft] ${tool}: running in MANUAL mode — ${reason}`);
  console.error('[zelvior-craft] The automated headless-browser check cannot run on this host.');
  console.error('[zelvior-craft] Fall back to the manual verification path:');
  console.error('[zelvior-craft]   1. Open the built page in any browser and screenshot it at');
  console.error('[zelvior-craft]      1440, 1024, 768 and 390 px.');
  console.error('[zelvior-craft]   2. Check every item in the craft checklist (SKILL.md "Checklist").');
  console.error('[zelvior-craft]   3. Read the copy aloud and lint it by eye, or run copy-lint.mjs');
  console.error('[zelvior-craft]      (which needs no browser).');
  console.error('[zelvior-craft]   4. Record the result by hand as a GATE line, e.g.');
  console.error('[zelvior-craft]      "GATE: MANUAL <tool> <pass|open>".');
  console.error('[zelvior-craft] Run: python3 <skill>/scripts/compat.py for a full environment report.');
  console.error('');
  process.exit(3);
}

// ---------------------------------------------------------------- launcher
// Build the argument list for the chosen engine. Obscura takes its own
// flags (it is always headless and does its own rendering, so Chrome's
// GPU/window flags are irrelevant); Chrome keeps the existing flag set.
function engineArgs(engine, o) {
  const { profile, gpu, windowSize, allowPrivateNetwork, allowFileAccess, stealth } = o;
  if (engine === 'obscura') {
    // Obscura serve is a CDP server; --port 0 picks a free port and the
    // ready-file records it once V8 is up. --allow-private-network lets it
    // reach local dev servers (http://127.0.0.1:<port>/); --allow-file-access
    // lets it open file:// pages. --storage-dir keeps state in the profile
    // folder so cleanup removes it.
    const args = [
      'serve', '--port', '0',
      '--ready-file', path.join(profile, 'obscura-ready.json'),
      '--storage-dir', profile,
    ];
    if (allowPrivateNetwork) args.push('--allow-private-network');
    if (allowFileAccess) args.push('--allow-file-access');
    if (stealth) args.push('--stealth');
    return args;
  }
  // Chrome / Edge / Chromium
  const args = [
    '--headless=new', `--user-data-dir=${profile}`, '--remote-debugging-port=0', '--no-first-run',
    '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars', '--mute-audio',
    '--disable-background-timer-throttling', '--disable-renderer-backgrounding',
    '--disable-backgrounding-occluded-windows', '--force-color-profile=srgb',
    `--window-size=${windowSize}`, 'about:blank',
  ];
  if (gpu) args.push('--enable-gpu', '--ignore-gpu-blocklist', '--use-angle=d3d11', '--enable-unsafe-webgpu');
  else args.push('--disable-gpu', '--use-angle=swiftshader', '--enable-unsafe-swiftshader');
  return args;
}

// Launch the browser engine and wait until its CDP port is ready. Returns
// { port, pid, child, kill, cleanup, engine }. The caller keeps its own
// fetch('/json/version') → WebSocket → CDP code, which works for both
// engines because both expose the same CDP HTTP endpoints.
//
// opts: { tool, profile, gpu, windowSize, allowPrivateNetwork, allowFileAccess, stealth, timeoutMs }
export async function launchBrowser(opts = {}) {
  const {
    tool = 'browser',
    profile,
    gpu = false,
    windowSize = '1440,900',
    allowPrivateNetwork = true,
    allowFileAccess = true,
    stealth = false,
    timeoutMs = 60000,
  } = opts;

  const eng = findEngine();
  if (!eng) {
    return manual(tool, 'no Obscura, Chrome, Edge or Chromium found (set OBSCURA_PATH or CHROME_PATH to its executable).');
  }

  fs.mkdirSync(profile, { recursive: true });

  const args = engineArgs(eng.engine, { profile, gpu, windowSize, allowPrivateNetwork, allowFileAccess, stealth });
  const child = spawn(eng.path, args, { stdio: ['ignore', 'ignore', 'pipe'], windowsHide: true });
  const pid = child.pid;

  const kill = () => {
    if (child.exitCode != null) return;
    if (process.platform === 'win32') {
      try { spawnSync('taskkill', ['/PID', String(pid), '/T', '/F'], { stdio: 'ignore' }); } catch { try { child.kill(); } catch { /* gone */ } }
    } else {
      try { process.kill(pid, 'SIGKILL'); } catch { /* gone */ }
    }
  };
  const cleanup = async () => {
    kill();
    for (let i = 0; i < 40 && fs.existsSync(profile); i++) {
      try { fs.rmSync(profile, { recursive: true, force: true }); } catch { /* still open */ }
      if (!fs.existsSync(profile)) break;
      await sleep(250);
    }
  };
  process.once('exit', () => { try { kill(); } catch { /* gone */ } });

  // wait for readiness: Obscura writes a JSON ready-file; Chrome writes the
  // DevToolsActivePort file. Both land in the profile directory.
  const readyFile = path.join(profile, 'obscura-ready.json');
  const portFile = path.join(profile, 'DevToolsActivePort');
  let port = null;
  const t0 = Date.now();
  while (Date.now() - t0 < timeoutMs) {
    if (child.exitCode != null) {
      await cleanup();
      throw new Error(`${eng.engine} exited early (code ${child.exitCode}) before its CDP port was ready.`);
    }
    try {
      if (eng.engine === 'obscura' && fs.existsSync(readyFile)) {
        const rec = JSON.parse(fs.readFileSync(readyFile, 'utf8'));
        if (rec && rec.port) { port = rec.port; break; }
      } else if (fs.existsSync(portFile)) {
        port = parseInt(fs.readFileSync(portFile, 'utf8').split('\n')[0], 10) || null;
        if (port) break;
      }
    } catch { /* still being written */ }
    await sleep(100);
  }
  if (!port) {
    await cleanup();
    throw new Error(`${eng.engine} did not become ready within ${timeoutMs}ms (no CDP port).`);
  }

  return { port, pid, child, kill, cleanup, engine: eng.engine };
}
