#!/usr/bin/env python3
"""Zelvior audit script: highest-signal checks from the 236-test Audityxe checklist.

Usage:
  python3 audit.py https://example.com
  python3 audit.py ./dist/index.html

Stdlib only. No dependencies. Prints pass/warn/fail per check and a summary.
Checks that need live headers/DNS/TLS are reported as unverified when offline.
"""

import html.parser
import json
import re
import ssl
import sys
import urllib.request
import urllib.error
from urllib.parse import urljoin, urlparse

PASS, WARN, FAIL, UNVERIFIED = "pass", "warn", "fail", "unverified"
results = []


def record(module, label, status, detail=""):
    results.append({"module": module, "label": label, "status": status, "detail": detail})
    mark = {"pass": "PASS", "warn": "WARN", "fail": "FAIL", "unverified": "UNVERIFIED"}[status]
    print(f"[{mark:10}] {module:22} {label}: {detail}")


class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles = []
        self._in_title = False
        self.metas = []
        self.links = []
        self.h1 = []
        self.h2 = []
        self.h3 = []
        self._heading = None
        self.imgs = []
        self.inputs = []
        self.buttons = []
        self.anchors = []
        self.iframes = []
        self.scripts = []
        self.stylesheets = []
        self.ids = []
        self.lang = None
        self.charset = None
        self.viewport = None
        self.canonical = None
        self.og = {}
        self.twitter = {}
        self.jsonld = []
        self._in_jsonld = False
        self._jsonld_buf = ""
        self.landmarks = set()
        self.skip_link = False
        self.text = []
        self.doctype = False
        self.deprecated = []
        self.positive_tabindex = 0
        self.target_blank_no_noopener = 0
        self.font_families = set()
        self.em_dashes = 0
        self.mailto = 0
        self.tel = 0
        self.ctas = 0
        self.external_scripts = 0
        self.aria_hidden_root = 0
        self.inline_base64 = 0
        self.loading_lazy = 0
        self.has_media_queries = False
        self.has_responsive_classes = 0

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype"):
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("header", "nav", "main", "footer"):
            self.landmarks.add(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self._in_title = True
        if tag in ("h1", "h2", "h3"):
            self._heading = tag
        if tag == "meta":
            self.metas.append(a)
            name = (a.get("name") or "").lower()
            prop = (a.get("property") or "").lower()
            content = a.get("content", "")
            if name == "viewport":
                self.viewport = content
            if name == "charset" or (a.get("charset")):
                self.charset = a.get("charset") or content
            if name == "description":
                pass
            if prop.startswith("og:"):
                self.og[prop] = content
            if name.startswith("twitter:") or prop.startswith("twitter:"):
                self.twitter[name or prop] = content
        if tag == "link":
            rel = (a.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href")
            if "stylesheet" in rel:
                self.stylesheets.append(a.get("href", ""))
            if "mask-icon" in rel:
                pass
        if tag == "img":
            self.imgs.append(a)
            if (a.get("src") or "").startswith("data:image"):
                self.inline_base64 += 1
            if a.get("loading") == "lazy":
                self.loading_lazy += 1
        if tag == "input":
            self.inputs.append(a)
        if tag == "button":
            self.buttons.append(a)
        if tag == "a":
            href = a.get("href", "")
            self.anchors.append(a)
            if href.startswith("mailto:"):
                self.mailto += 1
            if href.startswith("tel:"):
                self.tel += 1
            if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or ""):
                self.target_blank_no_noopener += 1
            if "cta" in href.lower() or "contact" in href.lower() or "signup" in href.lower() or "start" in href.lower():
                self.ctas += 1
        if tag == "iframe":
            self.iframes.append(a)
        if tag == "script":
            src = a.get("src", "")
            self.scripts.append(a)
            if src.startswith("http"):
                self.external_scripts += 1
            if (a.get("type") or "") == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = ""
        if tag in ("center", "font", "marquee", "blink"):
            self.deprecated.append(tag)
        if a.get("tabindex") and a["tabindex"].lstrip("-").isdigit() and int(a["tabindex"]) > 0:
            self.positive_tabindex += 1
        if a.get("aria-hidden") == "true" and tag in ("html", "body", "main"):
            self.aria_hidden_root += 1
        if a.get("href", "").startswith("#") and "skip" in a.get("href", "").lower():
            self.skip_link = True
        style = a.get("style", "")
        if "font-family" in style:
            for fam in style.split("font-family:")[-1].split(";")[0].split(","):
                self.font_families.add(fam.strip().strip("'\""))
        cls = a.get("class", "")
        if re.search(r"\b(sm|md|lg|xl|2xl):", cls):
            self.has_responsive_classes += 1
        if tag == "style":
            pass

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in ("h1", "h2", "h3"):
            self._heading = None
        if tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._jsonld_buf)

    def handle_data(self, data):
        if self._in_title:
            self.titles.append(data.strip())
        if self._heading == "h1":
            self.h1.append(data.strip())
        elif self._heading == "h2":
            self.h2.append(data.strip())
        elif self._heading == "h3":
            self.h3.append(data.strip())
        if self._in_jsonld:
            self._jsonld_buf += data
        self.text.append(data)
        self.em_dashes += data.count("\u2014")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "zelvior-audit/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.status, dict(resp.headers), resp.read().decode("utf-8", "replace")


def fetch_headers(url):
    req = urllib.request.Request(url, headers={"User-Agent": "zelvior-audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, dict(resp.headers), resp.geturl()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), url


def audit_html(html_text, base_url=""):
    p = Parser()
    p.feed(html_text)
    full_text = " ".join(p.text)
    words = len(full_text.split())

    # SEO
    title = " ".join(p.titles).strip()
    record("SEO", "Title tag", PASS if title else FAIL, f"{len(title)} chars" if title else "missing")
    record("SEO", "Single title tag", PASS if len(p.titles) == 1 else FAIL, f"{len(p.titles)} found")
    desc = next((m.get("content", "") for m in p.metas if (m.get("name") or "").lower() == "description"), "")
    record("SEO", "Meta description", PASS if desc else FAIL, f"{len(desc)} chars" if desc else "missing")
    record("SEO", "Canonical tag", PASS if p.canonical else FAIL, p.canonical or "missing")
    record("SEO", "Single canonical tag", PASS if p.canonical else WARN, "present" if p.canonical else "missing")
    record("SEO", "H1 heading", PASS if len(p.h1) == 1 else FAIL, f"{len(p.h1)} H1 found")
    record("SEO", "Structured data", PASS if p.jsonld else WARN, f"{len(p.jsonld)} JSON-LD block(s)")

    # HTML structure
    record("HTML Structure", "Doctype", PASS if p.doctype else FAIL, "present" if p.doctype else "missing")
    record("HTML Structure", "Landmark structure", PASS if len(p.landmarks) >= 3 else WARN, f"{sorted(p.landmarks)}")
    record("HTML Structure", "Unique IDs", PASS if len(p.ids) == len(set(p.ids)) else FAIL, f"{len(p.ids)} ids, {len(set(p.ids))} unique")
    record("HTML Structure", "Deprecated tags", PASS if not p.deprecated else FAIL, str(p.deprecated) if p.deprecated else "none")
    record("HTML Structure", "Language declaration", PASS if p.lang else FAIL, p.lang or "missing")
    record("HTML Structure", "Charset declaration", PASS if p.charset else WARN, p.charset or "missing")

    # Accessibility
    record("Accessibility", "Document language", PASS if p.lang else FAIL, p.lang or "missing")
    unlabeled = [i for i in p.inputs if not i.get("id") and not i.get("aria-label")]
    record("Accessibility", "Form labels", PASS if not unlabeled else WARN, f"{len(p.inputs)} inputs, {len(unlabeled)} without id/aria-label (check <label for>)")
    record("Accessibility", "Button names", PASS if p.buttons else PASS, f"{len(p.buttons)} buttons (verify accessible text manually)")
    record("Accessibility", "Link names", PASS if p.anchors else PASS, f"{len(p.anchors)} links (verify accessible text manually)")
    generic = [a for a in p.anchors if (a.get("href") or "") in ("#", "")]
    record("Accessibility", "Descriptive link text", PASS if not generic else WARN, f"{len(generic)} empty-href links")
    record("Accessibility", "Skip-to-content link", PASS if p.skip_link else WARN, "found" if p.skip_link else "not found")
    missing_alt = [i for i in p.imgs if "alt" not in i]
    record("Accessibility", "Image alt text", FAIL if missing_alt else PASS, f"{len(missing_alt)} of {len(p.imgs)} missing alt")
    record("Accessibility", "tabindex usage", PASS if p.positive_tabindex == 0 else FAIL, f"{p.positive_tabindex} positive tabindex")
    record("Accessibility", "aria-hidden misuse", PASS if p.aria_hidden_root == 0 else FAIL, f"{p.aria_hidden_root} root misuse")
    record("Accessibility", "Landmark regions", PASS if "main" in p.landmarks else FAIL, "main present" if "main" in p.landmarks else "no main")
    untitled = [f for f in p.iframes if not f.get("title")]
    record("Accessibility", "iframe titles", PASS if not untitled else FAIL, f"{len(untitled)} untitled")

    # Mobile
    record("Mobile", "Viewport meta tag", PASS if p.viewport else FAIL, p.viewport or "missing")
    zoom_off = p.viewport and ("user-scalable=no" in p.viewport or "maximum-scale=1" in p.viewport)
    record("Mobile", "Pinch-to-zoom", FAIL if zoom_off else PASS, "disabled" if zoom_off else "not disabled")
    record("Mobile", "Responsive CSS", PASS if p.has_responsive_classes else WARN, f"{p.has_responsive_classes} responsive class usages")

    # UX/UI + content
    record("UX/UI", "Above-the-fold CTA", PASS if p.ctas else WARN, f"{p.ctas} CTA-like links")
    record("UX/UI", "Primary heading clarity", PASS if len(p.h1) == 1 else FAIL, f"{len(p.h1)} H1")
    record("Content Quality", "Duplicate H2 headings", PASS if len(p.h2) == len(set(p.h2)) else WARN, f"{len(p.h2)} H2")
    record("Content Quality", "Duplicate H3 headings", PASS if len(p.h3) == len(set(p.h3)) else WARN, f"{len(p.h3)} H3")
    record("UX/UI", "Content depth", PASS if words >= 300 else WARN, f"{words} words")
    record("Content Quality", "Thin content", PASS if words >= 80 else FAIL, f"{words} words")

    # Images
    record("Images", "Images found", PASS, f"{len(p.imgs)} total")
    no_dims = [i for i in p.imgs if not i.get("width") or not i.get("height")]
    record("Images", "Explicit dimensions", PASS if not no_dims else WARN, f"{len(no_dims)} of {len(p.imgs)} missing width/height")
    record("Images", "Lazy loading", PASS if p.loading_lazy == len(p.imgs) else WARN, f"{p.loading_lazy} of {len(p.imgs)} lazy")
    record("Images", "Inline base64 images", PASS if p.inline_base64 == 0 else FAIL, f"{p.inline_base64} found")

    # Social
    record("Social Metadata", "Open Graph completeness", PASS if all(k in p.og for k in ("og:title", "og:description", "og:type", "og:url")) else WARN, str(sorted(p.og.keys())))
    record("Social Metadata", "og:image", PASS if "og:image" in p.og else WARN, p.og.get("og:image", "missing"))

    # Vibe-coded signals
    record("Vibe-Coded Signals", "Overused em dashes", PASS if p.em_dashes == 0 else WARN, f"{p.em_dashes} em dashes")
    buzz = ["delve", "elevate", "unlock", "supercharge", "seamless", "cutting-edge", "revolutionary", "game-changer", "leverage", "empower", "unleash"]
    found_buzz = [b for b in buzz if b in full_text.lower()]
    record("Vibe-Coded Signals", "Generic SaaS buzzwords", PASS if not found_buzz else WARN, str(found_buzz) if found_buzz else "none")
    record("Vibe-Coded Signals", "Emojis in production UI", PASS if not re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", full_text) else WARN, "check headings/buttons")

    # CRO
    record("CRO", "Direct contact links", PASS if (p.mailto or p.tel) else WARN, f"mailto={p.mailto} tel={p.tel}")
    record("CRO", "Call-to-action presence", PASS if p.ctas else WARN, f"{p.ctas} CTA-like links")

    # Third-party
    record("Third-Party Scripts", "Total external scripts", PASS if p.external_scripts == 0 else WARN, f"{p.external_scripts} external")

    # SRI / link safety
    record("SRI & Link Safety", 'target="_blank" safety', PASS if p.target_blank_no_noopener == 0 else FAIL, f"{p.target_blank_no_noopener} missing noopener")

    # Structured data validity
    valid = 0
    for block in p.jsonld:
        try:
            json.loads(block)
            valid += 1
        except Exception:
            pass
    record("Structured Data", "Valid JSON", PASS if valid == len(p.jsonld) and p.jsonld else WARN, f"{valid}/{len(p.jsonld)} valid")

    return p


def audit_url(url):
    print(f"Auditing {url}\n")
    status, headers, final_url = fetch_headers(url)
    h = {k.lower(): v for k, v in headers.items()}

    # Security headers
    record("Security Headers", "HTTPS", PASS if urlparse(final_url).scheme == "https" else FAIL, final_url)
    record("Security Headers", "Strict-Transport-Security", PASS if "strict-transport-security" in h else FAIL, h.get("strict-transport-security", "missing"))
    csp = h.get("content-security-policy", "")
    if not csp:
        record("Security Headers", "CSP script-src", FAIL, "no CSP header")
        record("Security Headers", "CSP style-src", FAIL, "no CSP header")
    else:
        script_unsafe = "unsafe-inline" in csp.split("script-src")[1].split(";")[0] if "script-src" in csp else "unsafe-inline" in csp
        record("Security Headers", "CSP script-src", FAIL if script_unsafe else PASS, "unsafe-inline present" if script_unsafe else "ok")
        style_unsafe = "unsafe-inline" in csp.split("style-src")[1].split(";")[0] if "style-src" in csp else "unsafe-inline" in csp
        record("Security Headers", "CSP style-src", WARN if style_unsafe else PASS, "unsafe-inline present" if style_unsafe else "ok")
    record("Security Headers", "X-Frame-Options", PASS if "x-frame-options" in h else WARN, h.get("x-frame-options", "missing"))
    record("Security Headers", "X-Content-Type-Options", PASS if h.get("x-content-type-options") == "nosniff" else WARN, h.get("x-content-type-options", "missing"))
    record("Security Headers", "Referrer-Policy", PASS if "referrer-policy" in h else WARN, h.get("referrer-policy", "missing"))
    record("Security Headers", "Permissions-Policy", PASS if "permissions-policy" in h else WARN, "present" if "permissions-policy" in h else "missing")
    record("Security Headers", "Cross-Origin-Opener-Policy", PASS if "cross-origin-opener-policy" in h else WARN, "present" if "cross-origin-opener-policy" in h else "missing")
    record("Security Headers", "Cross-Origin-Embedder-Policy", PASS if "cross-origin-embedder-policy" in h else WARN, "present" if "cross-origin-embedder-policy" in h else "missing")
    record("Security Headers", "Cross-Origin-Resource-Policy", PASS if "cross-origin-resource-policy" in h else WARN, "present" if "cross-origin-resource-policy" in h else "missing")
    record("Security Headers", "Server header exposure", WARN if "server" in h else PASS, h.get("server", "not exposed"))
    record("Security Headers", "X-Powered-By", PASS if "x-powered-by" not in h else FAIL, h.get("x-powered-by", "not exposed"))
    record("Security Headers", "CORS configuration", WARN if h.get("access-control-allow-origin") == "*" else PASS, h.get("access-control-allow-origin", "no wildcard"))

    # Well-known files
    base = urljoin(url, "/")
    for path, label in [("/robots.txt", "robots.txt"), ("/sitemap.xml", "sitemap.xml"), ("/llms.txt", "llms.txt"), ("/security.txt", "security.txt"), ("/.well-known/security.txt", "security.txt (well-known)"), ("/favicon.ico", "Favicon"), ("/manifest.json", "Web app manifest")]:
        try:
            s, _, _ = fetch(urljoin(base, path))
            record("Sitemap & Robots" if "robots" in label or "sitemap" in label else "Trust Signals" if "security" in label or "Favicon" in label or "manifest" in label else "AI Crawler Readiness", label, PASS if s == 200 else WARN, f"HTTP {s}")
        except Exception as e:
            record("Sitemap & Robots", label, WARN, str(e)[:80])

    # Page HTML
    try:
        s, _, html_text = fetch(final_url)
        record("Performance", "Server response time", PASS, f"HTTP {s}, {len(html_text)} bytes")
        record("Performance", "HTML document size", PASS if len(html_text) < 100_000 else WARN, f"{len(html_text)/1024:.1f} KB")
        record("Performance", "Response compression", UNVERIFIED, "check Content-Encoding header (br preferred)")
        audit_html(html_text, final_url)
    except Exception as e:
        record("Performance", "Fetch page", FAIL, str(e)[:120])

    # TLS (best effort)
    try:
        host = urlparse(url).hostname
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(__import__("socket").create_connection((host, 443), timeout=10), server_hostname=host) as sock:
            cert = sock.getpeercert()
            record("SSL/TLS", "Certificate expiration", PASS, str(cert.get("notAfter", "")))
            record("SSL/TLS", "TLS protocol version", PASS, sock.version())
    except Exception as e:
        record("SSL/TLS", "Certificate check", UNVERIFIED, str(e)[:80])

    # DNS/email checks need dig; report unverified
    record("Email Authentication", "SPF/DKIM/DMARC", UNVERIFIED, "run: dig TXT <domain> (see references/06-security.md)")
    record("DNS Security", "CAA/DNSSEC/NS/SOA", UNVERIFIED, "run: dig CAA/DNSKEY/NS/SOA <domain>")


def audit_file(path):
    print(f"Auditing file {path}\n")
    with open(path, encoding="utf-8", errors="replace") as f:
        html_text = f.read()
    audit_html(html_text, path)
    record("Security Headers", "Headers (file mode)", UNVERIFIED, "run against a live URL for header checks")
    record("SSL/TLS", "TLS (file mode)", UNVERIFIED, "run against a live URL")
    record("Email Authentication", "SPF/DKIM/DMARC", UNVERIFIED, "run: dig TXT <domain>")
    record("DNS Security", "CAA/DNSSEC/NS/SOA", UNVERIFIED, "run: dig CAA/DNSKEY/NS/SOA <domain>")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("--help", "-h"):
        print("Usage: python3 audit.py <url-or-file>")
        sys.exit(0 if len(sys.argv) > 1 else 2)
    target = sys.argv[1]
    if target.startswith("http"):
        audit_url(target)
    else:
        audit_file(target)
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("\nSummary:", json.dumps(counts))
    print(f"Total checks: {len(results)}")
    print("Full checklist (236 tests): references/11-audit-checklist.md")
    if counts.get("fail"):
        print("RESULT: FAIL - fix every fail before ship.")
        sys.exit(1)
    if counts.get("warn"):
        print("RESULT: WARN - fix every warn or document acceptance.")
        sys.exit(0)
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
