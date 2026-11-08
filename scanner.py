#!/usr/bin/env python3
"""AI-Friendly Scanner v0 — is your website AI friendly?

Checks what an AI agent or crawler ACTUALLY gets from a website, not what
the site declares. Built on the research-corrected spec (RESEARCH.md):

  1. THE DOOR — fetch the homepage as the real named bots (GPTBot,
     ClaudeBot, Googlebot) and compare with what robots.txt declares.
     Declarations lie both ways: paper-only bans and silent blocks.
  2. WHAT CRAWLERS RECEIVE — the major AI crawlers do not run JavaScript.
     Everything they will ever see is in the first raw response. This
     measures how much readable content that response holds and whether
     the page looks like an empty app shell without scripts.
  3. LABELS — agents navigate by the accessibility tree: named buttons,
     named links, labelled form fields. Counts unnamed controls with
     examples, straight from the page skeleton.
  4. PLUMBING — robots.txt and sitemap reality: present, fetchable,
     how many entries.

NOT scored (research says scoring these is theatre): llms.txt presence,
JSON-LD / structured data. They are reported as information only.
There is NO 0-100 score. The verdict is plain English with counts.

Stdlib only. Usage:
    python3 scanner.py https://example.com/ [--out reports/]
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/126.0.0.0 Safari/537.36")

BOTS = {
    "GPTBot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; "
               "compatible; GPTBot/1.2; +https://openai.com/gptbot)"),
    "ClaudeBot": ("Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; "
                  "compatible; ClaudeBot/1.0; "
                  "+https://www.anthropic.com/claudebot)"),
    "Googlebot": ("Mozilla/5.0 (compatible; Googlebot/2.1; "
                  "+http://www.google.com/bot.html)"),
}

CHALLENGE_MARKERS = ("just a moment", "challenges.cloudflare.com",
                     "cf-chl", "attention required", "are you a robot",
                     "checking your browser")

MAX_READ = 2_000_000


# ---------------------------------------------------------------- fetching

class FetchResult:
    def __init__(self, url):
        self.url = url
        self.status = None
        self.final_url = url
        self.body = b""
        self.elapsed_ms = None
        self.error = None
        self.server = None

    @property
    def text(self):
        return self.body.decode("utf-8", errors="replace")

    @property
    def challenge(self):
        body = self.text[:20000].lower()
        return any(m in body for m in CHALLENGE_MARKERS)


def fetch(url, ua, timeout=20):
    """One honest fetch. Never raises; the failure IS the receipt."""
    r = FetchResult(url)
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    })
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            r.status = resp.status
            r.final_url = resp.geturl()
            r.server = resp.headers.get("Server")
            r.body = resp.read(MAX_READ)
    except urllib.error.HTTPError as e:
        r.status = e.code
        r.final_url = e.geturl() or url
        try:
            r.body = e.read(200000)
        except Exception:
            r.body = b""
    except Exception as e:  # URLError, timeout, SSL — all are findings
        r.error = f"{type(e).__name__}: {e}"
    r.elapsed_ms = round((time.time() - start) * 1000)
    return r


# ---------------------------------------------------------------- robots

def parse_robots(text):
    """Return ({agent: [(directive, path)]}, [sitemaps], {signal: value},
    directive_line_count). Comment-only files (a content-signals preamble
    with nothing filled in) yield zero directives — a real finding."""
    groups, sitemaps, signals, current = {}, [], {}, []
    rules_started, n_directives = False, 0
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "sitemap":
            sitemaps.append(value)
            n_directives += 1
        elif key == "user-agent":
            if rules_started:
                current, rules_started = [], False
            current.append(value.lower())
            groups.setdefault(value.lower(), [])
            n_directives += 1
        elif key in ("allow", "disallow") and current:
            rules_started = True
            n_directives += 1
            for agent in current:
                groups[agent].append((key, value))
        elif key == "content-signal":
            n_directives += 1
            for pair in value.split(","):
                if "=" in pair:
                    k, _, v = pair.partition("=")
                    signals[k.strip().lower()] = v.strip().lower()
    return groups, sitemaps, signals, n_directives


def robots_verdict(groups, agent, path="/"):
    """Simplified RFC 9309: group for the agent else '*'; longest matching
    rule wins; ties go to Allow. Returns 'allowed' or 'disallowed'."""
    rules = groups.get(agent.lower())
    if rules is None:
        rules = groups.get("*")
    if not rules:
        return "allowed"
    best_len, verdict = -1, "allowed"
    for directive, rule_path in rules:
        if rule_path == "":
            continue
        if path.startswith(rule_path):
            if len(rule_path) > best_len:
                best_len, verdict = len(rule_path), directive
            elif len(rule_path) == best_len and directive == "allow":
                verdict = "allow"
    return "disallowed" if verdict == "disallow" else "allowed"


# ---------------------------------------------------------------- page audit

def element_string(tag, attrs, keys):
    """Rebuild the element as a receipt, e.g.
    <input type="email" name="EMAIL" placeholder="Email">. Only the
    attributes that matter to a visitor are kept, in a fixed order."""
    parts = [tag]
    for k in keys:
        v = attrs.get(k)
        if v:
            parts.append('%s="%s"' % (k, str(v).replace('"', "'")))
    if "required" in attrs:
        parts.append("required")
    return "<" + " ".join(parts) + ">"


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts, self.in_title = [], False
        self.meta_description = None
        self.h1_texts, self._h1 = [], None
        self.links = []          # {href, text, aria}
        self.buttons = []        # {text, aria, title}
        self.fields = []         # {tag, type, id, name, placeholder, aria}
        self.forms = []          # v0.2a: {action, method, id, name, role,
                                 #  fields: [...], submits: [...]}
        self._form_stack = []    # currently open forms
        self.label_texts = {}    # label-for id -> label text (v0.2a)
        self.label_fors = set()
        self.id_texts = {}       # any element's id -> its text (for
                                 # resolving aria-labelledby, F1)
        self._id_stack = []      # open elements carrying an id
        self.images = []         # {src, alt_present, alt}
        self.jsonld = 0
        self.script_tags = 0
        self.text_words = 0
        self.noscript_words = 0
        self.app_shell_id = None
        self._stack = []         # open elements for text capture
        self._skip_depth = 0
        self._in_noscript = 0
        self._in_label = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self._id_stack.append([tag, a["id"], []])
        if tag in ("script", "style"):
            self._skip_depth += 1
            if tag == "script":
                self.script_tags += 1
                if (a.get("type") or "").lower() == "application/ld+json":
                    self.jsonld += 1
        if tag == "noscript":
            self._in_noscript += 1
        if tag == "title":
            self.in_title = True
        if tag == "meta" and (a.get("name") or "").lower() == "description":
            self.meta_description = a.get("content") or ""
        if tag == "h1":
            self._h1 = []
        if tag == "a" and "href" in a:
            rec = {"href": a.get("href") or "", "text": [],
                   "aria": a.get("aria-label") or a.get("title") or ""}
            self.links.append(rec)
            self._stack.append(("a", rec))
        if tag == "button":
            rec = {"text": [], "aria": a.get("aria-label") or "",
                   "title": a.get("title") or "",
                   "type": (a.get("type") or "").lower()}
            self.buttons.append(rec)
            self._stack.append(("button", rec))
            if self._form_stack:
                self._form_stack[-1]["submits"].append({
                    "kind": "button", "rec": rec, "type": rec["type"],
                    "element": element_string(
                        "button", a, ("type", "id", "name", "aria-label"))})
        if tag == "form":
            rec = {"action_raw": a.get("action") or "",
                   "method": (a.get("method") or "get").lower(),
                   "id": a.get("id") or "", "name": a.get("name") or "",
                   "role": (a.get("role") or "").lower(),
                   "fields": [], "submits": []}
            self.forms.append(rec)
            self._form_stack.append(rec)
        if tag == "label":
            self._in_label += 1
            if a.get("for"):
                self.label_fors.add(a["for"])
            self._stack.append(("label", {"text": [],
                                          "for": a.get("for") or ""}))
        if tag in ("input", "select", "textarea"):
            ftype = (a.get("type") or "text").lower()
            if tag == "input" and ftype in ("hidden", "submit", "button",
                                            "image"):
                # an image input IS a submit control (its alt is its
                # accessible name) — never a field needing a label (F2)
                if ftype in ("submit", "button", "image") and \
                        self._form_stack:
                    self._form_stack[-1]["submits"].append({
                        "kind": "input", "type": ftype,
                        "value": a.get("value") or "",
                        "aria": a.get("aria-label") or "",
                        "alt": a.get("alt") or "",
                        "element": element_string(
                            "input", a,
                            ("type", "name", "value", "alt",
                             "aria-label"))})
            else:
                wrapped_rec = None
                for t, rec in reversed(self._stack):
                    if t == "label":
                        wrapped_rec = rec
                        break
                field = {
                    "tag": tag, "type": ftype, "id": a.get("id") or "",
                    "name": a.get("name") or "",
                    "placeholder": a.get("placeholder") or "",
                    "aria": a.get("aria-label") or
                            a.get("aria-labelledby") or "",
                    "aria_label": a.get("aria-label") or "",
                    "aria_labelledby": a.get("aria-labelledby") or "",
                    "wrapped_in_label": self._in_label > 0,
                    "required": ("required" in a or
                                 (a.get("aria-required") or "") == "true"),
                    "autocomplete": a.get("autocomplete") or "",
                    "element": element_string(
                        tag, a, ("type", "name", "id", "placeholder",
                                 "autocomplete", "aria-label")),
                    "_wrapped_label": wrapped_rec,
                }
                self.fields.append(field)
                if self._form_stack:
                    self._form_stack[-1]["fields"].append(field)
        if tag == "img":
            alt = a.get("alt") or ""
            self.images.append({"src": (a.get("src") or "")[:80],
                                "alt_present": "alt" in a, "alt": alt})
            # an image's alt text IS the accessible name of a link or
            # button that wraps it — credit it, like a real tree does
            if alt:
                for _t, rec in self._stack:
                    rec["text"].append(alt)
        if a.get("id") in ("root", "app", "__next") and not self.app_shell_id:
            self.app_shell_id = a["id"]

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag == "noscript" and self._in_noscript > 0:
            self._in_noscript -= 1
        if tag == "title":
            self.in_title = False
        if tag == "h1" and self._h1 is not None:
            self.h1_texts.append(" ".join(self._h1).strip())
            self._h1 = None
        if tag == "label" and self._in_label > 0:
            self._in_label -= 1
        if tag == "form" and self._form_stack:
            self._form_stack.pop()
        for i in range(len(self._id_stack) - 1, -1, -1):
            if self._id_stack[i][0] == tag:
                _t, el_id, parts = self._id_stack[i]
                del self._id_stack[i]
                if el_id not in self.id_texts:
                    self.id_texts[el_id] = " ".join(parts).strip()
                break
        if tag in ("a", "button", "label"):
            for i in range(len(self._stack) - 1, -1, -1):
                if self._stack[i][0] == tag:
                    rec = self._stack[i][1]
                    del self._stack[i]
                    if tag == "label" and rec.get("for"):
                        self.label_texts[rec["for"]] = \
                            " ".join(rec["text"]).strip()
                    break

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self._h1 is not None:
            self._h1.append(data)
        if self._skip_depth == 0:
            words = len(data.split())
            self.text_words += words
            if self._in_noscript > 0:
                self.noscript_words += words
            for _tag, rec in self._stack:
                rec["text"].append(data)
            for entry in self._id_stack:
                entry[2].append(data)

    # derived measures -------------------------------------------------
    @property
    def title(self):
        return " ".join(self.title_parts).strip()

    def unnamed_links(self):
        return [l for l in self.links
                if not " ".join(l["text"]).strip() and not l["aria"]]

    def unnamed_buttons(self):
        return [b for b in self.buttons
                if not " ".join(b["text"]).strip()
                and not b["aria"] and not b["title"]]

    def unlabelled_fields(self):
        out = []
        for f in self.fields:
            labelled = (f["aria"] or f["wrapped_in_label"] or
                        (f["id"] and f["id"] in self.label_fors))
            if not labelled:
                out.append(f)
        return out

    # v0.2a: per-form records ------------------------------------------
    def _resolve_labelledby(self, refs):
        """aria-labelledby names other elements by id; the label is
        THEIR text. Returns the referenced elements' text joined, or
        "" when any reference is missing or textless — an unresolved
        reference is no name at all, and the raw IDREF is never
        itself a label (F1)."""
        parts = []
        for ref in refs.split():
            text = self.id_texts.get(ref)
            if not text:
                return ""
            parts.append(text)
        return " ".join(parts)

    def field_label(self, f):
        """(label_text_or_None, how_it_is_labelled). A placeholder is
        NOT a label: it vanishes when the visitor types and is not an
        accessible name in the tree. Readable text wins wherever it
        lives: an EMPTY label element falls through to the aria
        sources before being reported as present-but-unreadable (F3),
        and aria-labelledby is resolved to the referenced element's
        actual text, never quoted as the raw IDREF (F1)."""
        empty_kind = None
        if f["id"] and f["id"] in self.label_fors:
            text = self.label_texts.get(f["id"], "")
            if text:
                return text, "label element"
            empty_kind = "label element"
        rec = f.get("_wrapped_label")
        if rec is not None:
            text = " ".join(rec["text"]).strip()
            if text:
                return text, "wrapping label"
            if empty_kind is None:
                empty_kind = "wrapping label"
        if f.get("aria_label"):
            return f["aria_label"], "aria-label"
        if f.get("aria_labelledby"):
            text = self._resolve_labelledby(f["aria_labelledby"])
            if text:
                return text, "aria-labelledby"
            return None, "aria-labelledby-unresolved"
        if empty_kind:
            return "", empty_kind
        return None, None

    def form_records(self, page_url):
        """Finalize this page's forms into plain dicts for the report:
        field-by-field label/name/type/required/autocomplete, the
        submit control's accessible name, and a purpose INFERENCE with
        its evidence. Element strings are the skeleton receipts."""
        unlab_ids = {id(x) for x in self.unlabelled_fields()}
        out = []
        for form in self.forms:
            fields = []
            for f in form["fields"]:
                text, kind = self.field_label(f)
                fields.append({
                    "element": f["element"],
                    "label": text if text else None,
                    "label_kind": kind,
                    # an aria-labelledby whose reference is not on the
                    # page names nothing — the field is unlabelled in
                    # the receipt, whatever v0's coarser test said (F1)
                    "labelled": id(f) not in unlab_ids and
                                kind != "aria-labelledby-unresolved",
                    "name": f["name"], "type": f["type"],
                    "required": bool(f["required"]),
                    "autocomplete": f["autocomplete"] or None,
                    "placeholder": f["placeholder"] or None,
                })
            submit = None
            for cand in form["submits"]:
                is_submit = (cand["type"] in ("submit", "image")
                             if cand["kind"] == "input"
                             else cand["type"] in ("", "submit"))
                if submit is not None and not is_submit:
                    continue
                if cand["kind"] == "input":
                    # a submit input's name is its value; an image
                    # submit's name is its alt (F2)
                    nm = (cand["value"] or cand.get("alt", "")
                          or cand["aria"])
                else:
                    rec = cand["rec"]
                    nm = (" ".join(rec["text"]).strip() or rec["aria"]
                          or rec["title"])
                submit = {"name": nm or None, "element": cand["element"]}
                if is_submit:
                    break
            purpose, evidence = infer_form_purpose(form)
            out.append({
                "page": page_url,
                "action": urllib.parse.urljoin(page_url,
                                               form["action_raw"]),
                "method": form["method"],
                "purpose": purpose, "purpose_evidence": evidence,
                "fields": fields, "submit": submit,
            })
        return out

    def images_missing_alt(self):
        return [i for i in self.images if not i["alt_present"]]


# ---------------------------------------------------------------- scan

def infer_form_purpose(form):
    """What a form appears to be for, from its action, identity and
    fields. This is an INFERENCE — the report always prints the evidence
    beside it, and it is never upgraded to a fact."""
    fields = form["fields"]
    ident = " ".join([form["id"], form["name"],
                      form["action_raw"]]).lower()
    types = [f["type"] for f in fields]
    names = " ".join((f["name"] + " " + f["id"]).lower() for f in fields)
    has_email = "email" in types or "email" in names
    has_textarea = any(f["tag"] == "textarea" for f in fields)
    n_pw = types.count("password")
    if form["role"] == "search" or "search" in types:
        return ("search", "the form is marked role=search or holds a "
                "search field")
    if (any(k in ident for k in ("checkout", "payment")) or
            any(k in names for k in ("card", "cvc", "expiry", "ccnum"))):
        return ("checkout / payment", "the form's destination or fields "
                "mention checkout, payment or card details")
    if n_pw >= 2:
        return ("signup (account creation)",
                f"{n_pw} password fields — a new password is being set, "
                f"not entered")
    if n_pw == 1:
        if any(k in ident for k in ("login", "log-in", "signin",
                                    "sign-in")):
            return ("login", "one password field, and the form "
                    "identifies itself as a login")
        if any(k in ident for k in ("register", "signup", "sign-up",
                                    "join")):
            return ("signup (account creation)", "one password field, "
                    "and the form identifies itself as a signup")
        return ("login or signup", "one password field; nothing in the "
                "form's destination or identity says which")
    if "comment" in ident or "comment" in names:
        return ("comment", "the form or its fields identify as a "
                "comment form")
    if has_textarea and has_email:
        return ("contact", "a message box (textarea) plus an email "
                "field")
    if has_textarea:
        return ("contact / message", "a message box (textarea) is the "
                "main field")
    if has_email and any(k in ident for k in (
            "subscribe", "newsletter", "mailchimp", "list-manage",
            "convertkit", "kit.com", "substack", "buttondown",
            "mailerlite", "sendfox", "campaign-archive")):
        return ("newsletter signup", "an email field, and the form's "
                "destination identifies a mailing list or subscription")
    if has_email and len(fields) <= 2:
        return ("email signup (newsletter or lead capture)", "an email "
                "field and little else; the destination says no more")
    if has_email:
        return ("signup / lead capture", "an email field among other "
                "fields")
    return ("general form", "no strong signals in the destination, "
            "identity or fields")


CRAWL_CAP = 25
ASSET_EXTS = (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".css",
              ".js", ".xml", ".pdf", ".zip", ".ico", ".mp4", ".mp3",
              ".woff", ".woff2")


def _locs(xml_text):
    return [m.strip() for m in
            re.findall(r"<loc>\s*([^<]+?)\s*</loc>", xml_text)]


def collect_urls(base_url, fetcher=fetch, cap=CRAWL_CAP):
    """The pages to audit beyond the homepage: the sitemap's URLs (an
    index's children included), falling back to the homepage's own
    links when no usable sitemap exists. Same host only, fragments
    stripped, homepage first. Returns (urls, source_note, total_found)
    — total_found is the pre-cap count, so the report can say plainly
    when the cap cut the list."""
    origin = urllib.parse.urlparse(base_url)
    home = base_url if base_url.endswith("/") else base_url + "/"
    root = f"{origin.scheme}://{origin.netloc}"

    def same_host_clean(candidates):
        seen, clean = set(), []
        for u in candidates:
            p = urllib.parse.urlparse(u)
            if p.netloc != origin.netloc or \
                    p.scheme not in ("http", "https"):
                continue
            u2 = urllib.parse.urlunparse(p._replace(fragment=""))
            if u2 not in seen:
                seen.add(u2)
                clean.append(u2)
        return clean

    robots_r = fetcher(root + "/robots.txt", BROWSER_UA)
    declared = []
    if robots_r.status == 200 and robots_r.text.strip():
        _, declared, _, _ = parse_robots(robots_r.text)
    sm_url = declared[0] if declared else root + "/sitemap.xml"
    sm = fetcher(sm_url, BROWSER_UA)
    found, source = [], ""
    if sm.status == 200:
        if "<sitemapindex" in sm.text[:2000]:
            children = _locs(sm.text)[:10]
            for child in children:
                cr = fetcher(child, BROWSER_UA)
                if cr.status == 200:
                    found += _locs(cr.text)
            if found:
                source = (f"sitemap index {sm_url} "
                          f"({len(children)} child sitemaps read)")
        else:
            found = _locs(sm.text)
            if found:
                source = f"sitemap {sm_url}"
    clean = same_host_clean([home] + found)
    if len(clean) > 1:
        return clean[:cap], source or "sitemap", len(clean)
    # fallback: the homepage's own links
    base = fetcher(home, BROWSER_UA)
    audit = PageAudit()
    audit.feed(base.text)
    candidates = [urllib.parse.urljoin(home, l["href"])
                  for l in audit.links]
    candidates = [u for u in candidates
                  if not urllib.parse.urlparse(u).path.lower()
                  .endswith(ASSET_EXTS)]
    clean = same_host_clean([home] + candidates)
    return clean[:cap], "homepage links (no usable sitemap)", len(clean)


def scan_site(base_url, fetcher=fetch, cap=CRAWL_CAP):
    """v0.2a: the v0 homepage scan PLUS a crawl — every page the
    sitemap (or the homepage's links) offers, up to the cap — with a
    field-by-field audit of every form on every page."""
    r = scan(base_url, fetcher)
    urls, source, total = collect_urls(base_url, fetcher, cap)
    pages, forms = [], []
    for u in urls:
        fr = fetcher(u, BROWSER_UA)
        if fr.status != 200 or not fr.body:
            pages.append({"url": u, "status": fr.status, "forms": 0,
                          "fields": 0, "unlabelled": 0})
            continue
        a = PageAudit()
        a.feed(fr.text)
        page_forms = a.form_records(u)
        forms += page_forms
        pages.append({"url": u, "status": fr.status,
                      "forms": len(page_forms),
                      "fields": len(a.fields),
                      "unlabelled": len(a.unlabelled_fields())})
    r["crawl"] = {"source": source, "urls_found": total, "cap": cap,
                  "pages_audited": sum(1 for p in pages
                                       if p["status"] == 200)}
    r["pages"] = pages
    r["forms"] = forms
    return r


def scan(base_url, fetcher=fetch):
    origin = urllib.parse.urlparse(base_url)
    root = f"{origin.scheme}://{origin.netloc}"
    home = base_url if base_url.endswith("/") else base_url + "/"

    receipts = {"url": base_url, "scanned_from": "scanner network (one vantage point)"}
    findings = []

    # PLUMBING: robots + sitemap
    robots_r = fetcher(root + "/robots.txt", BROWSER_UA)
    groups, declared_sitemaps, signals, n_dir = {}, [], {}, 0
    robots_fetched = robots_r.status == 200
    if robots_fetched and robots_r.text.strip():
        groups, declared_sitemaps, signals, n_dir = parse_robots(robots_r.text)
    receipts["robots"] = {"status": robots_r.status,
                          "bytes": len(robots_r.body),
                          "found": robots_fetched,
                          "directives": n_dir,
                          "content_signals": signals}
    sitemap_url = declared_sitemaps[0] if declared_sitemaps else root + "/sitemap.xml"
    sm = fetcher(sitemap_url, BROWSER_UA)
    sm_entries = None
    if sm.status == 200:
        sm_entries = sm.text.count("<loc>")
    receipts["sitemap"] = {"url": sitemap_url, "status": sm.status,
                           "entries": sm_entries,
                           "kind": ("index" if "<sitemapindex" in sm.text[:2000]
                                    else "urlset" if sm.status == 200 else None)}

    # THE DOOR: browser baseline + bots
    door = {}
    base = fetcher(home, BROWSER_UA)
    door["browser"] = {"status": base.status, "bytes": len(base.body),
                       "ms": base.elapsed_ms, "error": base.error}
    for name, ua in BOTS.items():
        r = fetcher(home, ua)
        declared = (robots_verdict(groups, name) if robots_fetched
                    else "robots.txt unreachable")
        actual = ("served" if r.status == 200 else
                  f"http {r.status}" if r.status else "failed")
        entry = {"ua_status": r.status, "bytes": len(r.body),
                 "ms": r.elapsed_ms, "error": r.error,
                 "challenge": r.challenge,
                 "robots_declares": declared, "actual": actual}
        if robots_fetched:
            if declared == "disallowed" and r.status == 200:
                entry["mismatch"] = "PAPER-ONLY BAN: robots.txt says no, the site serves it anyway"
            elif declared == "allowed" and (r.status in (401, 403) or r.challenge):
                entry["mismatch"] = "SILENT BLOCK: robots.txt says welcome, the door says no"
        door[name] = entry
    receipts["door"] = door

    # CONTENT + LABELS from the browser-UA raw response (what crawlers get
    # is the same raw body — no JavaScript runs for them either way)
    audit = PageAudit()
    audit.feed(base.text)
    un_links, un_buttons = audit.unnamed_links(), audit.unnamed_buttons()
    un_fields = audit.unlabelled_fields()
    no_alt = audit.images_missing_alt()
    receipts["content"] = {
        "visible_words_raw": audit.text_words,
        "script_tags": audit.script_tags,
        "app_shell_id": audit.app_shell_id,
        "noscript_words": audit.noscript_words,
        "title": audit.title,
        "h1": audit.h1_texts,
        "meta_description": bool(audit.meta_description),
    }
    receipts["labels"] = {
        "links_total": len(audit.links), "links_unnamed": len(un_links),
        "buttons_total": len(audit.buttons),
        "buttons_unnamed": len(un_buttons),
        "fields_total": len(audit.fields),
        "fields_unlabelled": len(un_fields),
        "images_total": len(audit.images),
        "images_missing_alt": len(no_alt),
        "example_unnamed_links": [l["href"] for l in un_links[:3]],
        "example_unlabelled_fields":
            [f["name"] or f["id"] or f["type"] for f in un_fields[:3]],
    }

    # INFORMATION ONLY (not scored — see RESEARCH.md)
    llms = fetcher(root + "/llms.txt", BROWSER_UA)
    receipts["info_only"] = {
        "llms_txt": {"status": llms.status, "bytes": len(llms.body)},
        "jsonld_blocks": audit.jsonld,
    }
    receipts["fetches"] = {"homepage_bytes": len(base.body),
                           "homepage_ms": base.elapsed_ms}
    return receipts


# ---------------------------------------------------------------- verdict

def verdict_lines(r):
    """Plain-English verdict. No score. Worst true things first."""
    lines, door, c, l = [], r["door"], r["content"], r["labels"]
    silent = [b for b, e in door.items()
              if b != "browser" and "SILENT BLOCK" in e.get("mismatch", "")]
    paper = [b for b, e in door.items()
             if b != "browser" and "PAPER-ONLY BAN" in e.get("mismatch", "")]
    if silent:
        lines.append(f"AI visitors are being turned away at the door: "
                     f"{', '.join(silent)} get a block or a challenge page "
                     f"even though robots.txt says they are welcome.")
    if paper:
        lines.append(f"robots.txt says {', '.join(paper)} may not enter, "
                     f"but the site serves them anyway — the declared rule "
                     f"is not the real rule.")
    if not silent and not paper:
        ok = [b for b, e in door.items() if b != "browser"
              and e.get("ua_status") == 200]
        if len(ok) == 3:
            lines.append("The door is honest: every major AI bot that "
                         "robots.txt welcomes actually gets the page.")
    if c["visible_words_raw"] < 100:
        lines.append(f"A crawler that cannot run JavaScript receives "
                     f"almost nothing: {c['visible_words_raw']} words of "
                     f"readable text in the raw page.")
    elif c["app_shell_id"]:
        lines.append(f"The raw page is an app shell (#{c['app_shell_id']}) "
                     f"with {c['visible_words_raw']} words — content that "
                     f"appears only after JavaScript runs is invisible to "
                     f"AI crawlers.")
    bumps = []
    if l["links_unnamed"]:
        bumps.append(f"{l['links_unnamed']} of {l['links_total']} links "
                     f"have no name an agent can read")
    if l["buttons_unnamed"]:
        bumps.append(f"{l['buttons_unnamed']} of {l['buttons_total']} "
                     f"buttons are unnamed")
    if l["fields_unlabelled"]:
        bumps.append(f"{l['fields_unlabelled']} of {l['fields_total']} "
                     f"form fields have no label")
    if l["images_missing_alt"]:
        bumps.append(f"{l['images_missing_alt']} of {l['images_total']} "
                     f"images have no alt text at all")
    if bumps:
        lines.append("Navigation bumps in the page skeleton: " +
                     "; ".join(bumps) + ".")
    else:
        lines.append("The page skeleton is clean: every link, button and "
                     "form field carries a name an agent can read.")
    rob = r.get("robots", {})
    if rob.get("found") and rob.get("directives", 0) == 0:
        lines.append("robots.txt is a preamble with nothing filled in: "
                     "it states no rules and sets no AI content signals "
                     "(search / ai-input / ai-train are all unstated).")
    if r["sitemap"].get("status") != 200:
        lines.append(f"No working sitemap (fetch of "
                     f"{r['sitemap'].get('url')} returned "
                     f"{r['sitemap'].get('status')}) — crawlers get no "
                     f"map of the site.")
    if "crawl" in r:
        cr = r["crawl"]
        lines.append(f"Beyond the homepage: audited "
                     f"{cr['pages_audited']} of {cr['urls_found']} "
                     f"pages found (cap {cr['cap']}, via "
                     f"{cr['source']}).")
        forms = r.get("forms", [])
        n_fields = sum(len(f["fields"]) for f in forms)
        n_unlab = sum(1 for f in forms for fd in f["fields"]
                      if not fd["labelled"])
        if forms:
            if n_unlab:
                lines.append(f"Across the site, {len(forms)} forms "
                             f"hold {n_fields} fields; {n_unlab} "
                             f"field(s) have no label — each one is a "
                             f"place a visitor, human or agent, can "
                             f"get stuck.")
            else:
                lines.append(f"Across the site, {len(forms)} forms "
                             f"hold {n_fields} fields and every field "
                             f"carries a label.")
    return lines


def render_report(r):
    d, c, l, p, io = (r["door"], r["content"], r["labels"],
                      r["sitemap"], r["info_only"])
    out = [f"# Is it AI friendly? — {r['url']}", "",
           f"Scanned from: {r['scanned_from']}. One vantage point, "
           f"raw fetches only (no JavaScript run) — which is also what "
           f"the AI crawlers get.", "", "## Verdict", ""]
    out += [f"- {v}" for v in verdict_lines(r)]
    out += ["", "## The door — declared vs actual", "",
            "| Visitor | robots.txt says | Actually got |",
            "|---|---|---|"]
    for name, e in d.items():
        if name == "browser":
            out.append(f"| Browser (baseline) | — | "
                       f"{e['status'] or e['error']} "
                       f"({e['bytes']} bytes, {e['ms']} ms) |")
        else:
            got = e["actual"] + (" + challenge page" if e["challenge"] else "")
            row = (f"| {name} | {e['robots_declares']} | {got} |")
            if e.get("mismatch"):
                row += f"\n  **{e['mismatch']}**"
            out.append(row)
    out += ["", "## What crawlers receive (no JavaScript)", "",
            f"- Readable words in the raw page: **{c['visible_words_raw']}**",
            f"- Script tags on the page: {c['script_tags']}",
            f"- App-shell container: {c['app_shell_id'] or 'none detected'}",
            f"- Page title: {c['title'] or '(none)'}",
            f"- H1 headings: {c['h1'] or '(none)'}",
            f"- Meta description: {'yes' if c['meta_description'] else 'no'}",
            "", "## Labels an agent navigates by", "",
            f"- Links: {l['links_total']} total, "
            f"**{l['links_unnamed']} unnamed**"
            + (f" (e.g. {', '.join(l['example_unnamed_links'])})"
               if l['example_unnamed_links'] else ""),
            f"- Buttons: {l['buttons_total']} total, "
            f"**{l['buttons_unnamed']} unnamed**",
            f"- Form fields: {l['fields_total']} total, "
            f"**{l['fields_unlabelled']} with no label**"
            + (f" (e.g. {', '.join(l['example_unlabelled_fields'])})"
               if l['example_unlabelled_fields'] else ""),
            f"- Images: {l['images_total']} total, "
            f"**{l['images_missing_alt']} with no alt attribute**",
            "", "## Plumbing", "",
            f"- robots.txt: {'found' if r['robots']['found'] else 'NOT FOUND'}"
            f" (status {r['robots']['status']}, "
            f"{r['robots'].get('directives', 0)} directive lines)"
            + (f"\n- Declared AI content signals: "
               + ", ".join(f"{k}={v}" for k, v in
                           r["robots"].get("content_signals", {}).items())
               if r["robots"].get("content_signals") else ""),
            f"- Sitemap: {p['url']} — status {p['status']}, "
            f"{p['entries'] if p['entries'] is not None else '—'} entries"
            + (f", a sitemap index" if p["kind"] == "index" else ""),
            "", "## Information only — NOT scored", "",
            f"- llms.txt: status {io['llms_txt']['status']}"
            + (f", {io['llms_txt']['bytes']} bytes"
               if io['llms_txt']['status'] == 200 else "")
            + ". (Research: no major AI "
            f"system is known to read it; presence proves nothing.)",
            f"- Structured data (JSON-LD) blocks: {io['jsonld_blocks']}. "
            f"(Research: helps systems understand content; controlled "
            f"studies show it does not buy AI citations.)",
            "", "## Not checked in v0", "",
            "- A live agent task run ('find the price', 'start the "
            "signup') — the v0.2 step, and the one no incumbent does.",
            "- Rendered-vs-raw diff in a real browser (v0 measures the "
            "raw response, which is what crawlers receive).",
            "- Pages beyond the homepage; login flows; checkout.",
            ""]
    return "\n".join(out)


def render_site_report(r):
    """The v0 report (homepage sections) with the v0.2a crawl and
    form sections in place of the v0 'not checked' list."""
    text = render_report(r)
    marker = "\n## Not checked in v0"
    if marker in text:
        text = text[:text.index(marker)]
    cr, pages, forms = r["crawl"], r["pages"], r["forms"]
    out = [text.rstrip(), "", "## Site crawl (v0.2a)", "",
           f"- Source: {cr['source']}.",
           f"- URLs found: {cr['urls_found']}; pages audited: "
           f"{cr['pages_audited']} (cap {cr['cap']}"
           + (f" — the cap cut the list" if cr['urls_found'] > cr['cap']
              else "") + ").",
           "- (The sections above describe the homepage; this section "
           "and the next cover the whole crawl.)", "",
           "| Page | Forms | Fields | Unlabelled fields |",
           "|---|---|---|---|"]
    for p in pages:
        if p["status"] == 200:
            out.append(f"| {p['url']} | {p['forms']} | {p['fields']} "
                       f"| {p['unlabelled']} |")
        else:
            out.append(f"| {p['url']} | fetch status {p['status']} "
                       f"| — | — |")
    n_fields = sum(len(f["fields"]) for f in forms)
    n_unlab = sum(1 for f in forms for fd in f["fields"]
                  if not fd["labelled"])
    out += ["", "## Forms — field by field (v0.2a)", "",
            f"{len(forms)} forms, {n_fields} fields, **{n_unlab} with "
            f"no label** across the crawl. A field's label is what a "
            f"screen reader announces and what an agent navigates by; "
            f"a placeholder is not a label. Every field below is quoted "
            f"as the element actually found — the receipt, not a "
            f"summary of it."]
    for i, f in enumerate(forms, 1):
        out += ["", f"### Form {i} — appears to be: {f['purpose']}",
                "",
                f"*Purpose is an inference* — from: "
                f"{f['purpose_evidence']}.",
                f"- Page: {f['page']}",
                f"- Sends to: {f['action']} (method {f['method']})", "",
                "| Field (element as found) | Label | Name | Type | "
                "Required | Autocomplete |",
                "|---|---|---|---|---|---|"]
        for fd in f["fields"]:
            if not fd["labelled"]:
                label = "**ABSENT**"
                if fd["label_kind"] == "aria-labelledby-unresolved":
                    label += (" (aria-labelledby names an element "
                              "that is not on this page — the field "
                              "has no readable label)")
            elif fd["label"]:
                label = fd["label"]
            else:
                label = "(label element present, no readable text)"
            if fd["placeholder"] and not fd["labelled"]:
                label += f" (placeholder only: \"{fd['placeholder']}\")"
            out.append(f"| `{fd['element']}` | {label} | "
                       f"{fd['name'] or '—'} | {fd['type']} | "
                       f"{'yes' if fd['required'] else 'no'} | "
                       f"{fd['autocomplete'] or 'absent'} |")
        if f["submit"] is None:
            out.append("\nSubmit control: **none found in the "
                       "skeleton** — a visitor has no visible way to "
                       "send this form.")
        elif f["submit"]["name"]:
            out.append(f"\nSubmit control: \"{f['submit']['name']}\" — "
                       f"`{f['submit']['element']}`")
        else:
            out.append(f"\nSubmit control: **no accessible name** — "
                       f"`{f['submit']['element']}`")
    out += ["", "## Not checked in v0.2a", "",
            "- A live agent task run (the Inspector, v0.2b) — protocol "
            "specced at goals/ai-friendly-website-scanner/files/"
            "inspector-run-protocol-2026-11-04.md; it runs through a "
            "browser seat, not this code.",
            "- Rendered-vs-raw diff in a real browser (v0.2a measures "
            "the raw response, which is what crawlers receive).",
            "- Anything past a submit click; login flows.",
            ""]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default=None,
                    help="directory for the markdown + JSON reports")
    ap.add_argument("--deep", action="store_true",
                    help="v0.2a: crawl the site (sitemap, else homepage "
                         "links) and audit every form field by field")
    ap.add_argument("--cap", type=int, default=CRAWL_CAP,
                    help="max pages to audit in --deep mode "
                         f"(default {CRAWL_CAP})")
    args = ap.parse_args(argv)
    if args.deep:
        r = scan_site(args.url, cap=args.cap)
        report = render_site_report(r)
    else:
        r = scan(args.url)
        report = render_report(r)
    if args.out:
        import os
        os.makedirs(args.out, exist_ok=True)
        parsed = urllib.parse.urlparse(args.url)
        host = parsed.netloc.replace(".", "-")
        slug = parsed.path.strip("/").replace("/", "-")[:60]
        name = host + ("--" + slug if slug else "")
        if args.deep:
            name += "--deep"
        with open(os.path.join(args.out, name + ".md"), "w") as f:
            f.write(report)
        with open(os.path.join(args.out, name + "-receipts.json"), "w") as f:
            json.dump(r, f, indent=2)
    # print AFTER writing (F4): a closed or truncated stdout pipe must
    # never be able to take the --out report files down with it
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
