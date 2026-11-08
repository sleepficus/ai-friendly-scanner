# Build Report — Scanner Revival (v0 re-verification + v0.2a + v0.2b spec)

**Date:** 2026-11-04 · **Builder:** Muse (subagent lane) · **Status:**
built, tested, self-reviewed — **NOT certified** (Law 2: a fresh audit
lane certifies; this report does not).

Deliverable hashes (full SHA-256):
- `scanner.py` — `0f4c490ce6ff75bc95e8598951d13901d4735540ddc39063b618124a5a586a8b`
- `test_scanner.py` — `68984dd38ca0a7a9c61e90d26591319241c3bdfa0695164255357906f1770bcf`

---

## Step 1 — v0 re-verification (before any new code)

**Test suite, exact result:** `Ran 11 tests in 0.004s — OK`. The v0
suite passes untouched, as shipped 2026-10-23.

**Fresh scans** (dated, Oct 23 reports not overwritten):
`reports/2026-11-04/www-misfitcircuit-com.md` and
`reports/2026-11-04/watercolormisfit-com.md`, each with its receipts
JSON. The tool ran clean on both of today's sites — **no errors, no
fixes needed, nothing refactored.**

*Note on evidence:* the scan run's captured stdout was internally
inconsistent with the report files it wrote (it showed older-looking
numbers). The Markdown reports and their receipts JSONs agree with each
other exactly, and an independent curl check confirmed them (MC
sitemap → 200; MC homepage ≈17 KB, matching the file's 17,314 bytes;
WCM robots = the standard WP file). All figures below are from the
files — the receipts of record.

### misfitcircuit.com — both Oct 23 findings are FIXED

| Check | Oct 23 | Nov 4 | |
|---|---|---|---|
| robots.txt | 200, **0 directive lines** (24-line preamble, nothing filled in) | 200, **3 directive lines** | FIXED |
| Sitemap | **404** — no working sitemap | **200, 36 entries** | FIXED |
| Door | honest, all bots served | honest, all bots served | stands |
| Skeleton | clean (81 links, 0 unnamed) | clean (42 links, 0 unnamed) | stands |
| Raw words | 2,134 | 979 | page rebuilt |
| llms.txt | 404 | 200, 1,032 bytes | changed (info-only, never scored) |

The site itself was rebuilt since Oct 23 (new title/H1, roughly half
the raw words and links) — the rebuild closed both plumbing findings
the v0 scan reported.

### watercolormisfit.com — Oct 23 findings STAND, nearly to the digit

| Check | Oct 23 | Nov 4 |
|---|---|---|
| Raw words | 323 | 323 |
| Links | 33 total, **3 unnamed** (same three post-card URLs as examples) | 33 total, **3 unnamed** |
| Buttons / fields | 3 buttons, 0 unnamed · 1 field, 0 unlabelled | same |
| robots.txt | 200, 5 directive lines | same |
| Sitemap | wp-sitemap.xml index, 200, 5 entries | same |
| Door | honest | honest |
| llms.txt | 404 | 404 (info-only) |

## Step 2 — v0.2a built: the form + flow deepening

`python3 scanner.py <url> --deep [--cap 25]` — v0's homepage scan plus:

- **Site crawl** (`collect_urls`): sitemap URLs first (index children
  read, up to 10), homepage links as fallback when no usable sitemap;
  same host only, fragments stripped, homepage first, cap 25 default.
  The report prints found-vs-audited counts and says when the cap cut
  the list.
- **Per-form audit** (`PageAudit.form_records` + `infer_form_purpose`):
  every form on every crawled page gets a field-by-field table — the
  element as found (the skeleton receipt), label or **ABSENT** (a
  placeholder is never a label), name, type, required, autocomplete —
  plus the submit control's accessible name, and the form's apparent
  purpose printed as an *inference* with its evidence string. Label
  resolution matches v0's labelled/unlabelled determination exactly
  (same `unlabelled_fields` logic decides), so v0.2a counts can never
  disagree with v0 counts.
- Doctrine kept: no 0–100 score, plain English with counts,
  declared-vs-actual, llms.txt/JSON-LD info-only. v0's default
  (non-`--deep`) behavior and report are unchanged.

**Tests: 19/19 pass** (`Ran 19 tests — OK`): the 11 v0 tests plus 8
new — form records found; unlabelled field caught with its element
receipt; labelled fields pass by `for`, by wrapping label, with
autocomplete captured; submit names from both `<input type=submit>`
and `<button>`; purpose inference carries evidence, never bare; crawl
cap respected (31 found → 25 returned, total reported pre-cap);
homepage-link fallback (external + asset links excluded); cross-page
form aggregation in a full fake-site `scan_site` (3 forms, exactly 1
unlabelled field, report shows "inference" and "ABSENT").

**Live deep runs** (in `reports/2026-11-04/`, `--deep` files):
- *misfitcircuit.com* — 36 URLs found via sitemap, 25 audited (cap
  stated). 1 form: the /php-check/ version form — field labelled
  "Your PHP version", submit "Check it". Clean.
- *watercolormisfit.com* — 217 URLs found via the sitemap index (5
  child sitemaps read), 25 audited (cap stated). 25 forms / 25 fields
  / **0 unlabelled**: every audited page carries the same site-search
  form (field labelled "Search articles", submit named by
  aria-label "Search").

**Stated limits (printed in the reports):** crawl order is sitemap
order, so the cap takes the first 25 — on WCM that is 25 posts, and
any signup/contact form beyond the cap, or injected by JavaScript
after load (e.g. an embed), is not in the raw skeleton and is not
audited; that is the same blindness the crawlers have, said out loud.
Fields outside a `<form>` are counted per page but only form-grouped
fields get the field-by-field table (misfitcircuit /apartment/ shows
3 such fields).

## Step 3 — v0.2b specced, NOT built

The live Inspector run protocol is written to
`~/workspace/goals/ai-friendly-website-scanner/files/inspector-run-protocol-2026-11-04.md`:
task selection (buy → newsletter signup → contact → book, by the site's
own evidence), the hard boundary (**attempt without submitting
anything**; the run ends at the pre-submit point), drive-as-the-visitor
rules (perceive via the tree, navigate by the page's own controls,
20-step / 10-minute cap), the three-part stall record — (a) intent,
(b) perception quoted, (c) the skeleton element responsible — guesses
labelled GUESS, no-score verdict headlines, and the full report
template. The spec states execution runs through **Tally's browser
route**, never a code lane, and is never simulated from static fetches.

## Self-review (builder's, not certification)

- v0's 11 tests pass unmodified; the v0 code paths (`scan`,
  `render_report`, default CLI) are behavior-identical — v0.2a is
  additive (`--deep` gate) apart from `PageAudit` now also recording
  form structure while parsing (its v0 outputs verified unchanged by
  the suite and by the fresh-scan comparison above).
- Every number in this report traces to a test run, a report file, or
  a receipts JSON named above. The one anomaly found (captured stdout
  vs. written files) is reported in Step 1 rather than smoothed over;
  the files were independently confirmed.
- Known soft spot: purpose inference is heuristic by design — it is
  labelled inference everywhere it appears, with its evidence printed.

---

## FIX-LOG — audit findings F1–F4 (fix lane, 2026-11-04)

The independent audit (AUDIT-REPORT.md) returned **CERTIFY-WITH-
FINDINGS**: F1–F3 minor correctness defects in the v0.2a form audit,
F4 info. All four are fixed here. Tests: **23/23 pass** — the 19
pre-existing tests unmodified and passing, plus 4 new regression
tests (`FormAuditFixTests`) built from the auditor's own probes.

Deliverable hashes after the fixes (full SHA-256):
- `scanner.py` — `2995f926c961768ad0c98612d68f09f4a4f9e33ba8bd57b00975897bf4d1a648`
- `test_scanner.py` — `158cebfa8bb9d647586572bdd8aff9c6d10e13bd292431054202a962de965e7c`

- **F1 — aria-labelledby resolved, never quoted raw.** The parser now
  keeps an id→text pass (`id_texts`, captured for every element
  carrying an id, descendants' text included — textContent
  semantics), and `field_label()` resolves the IDREF(s) to the
  referenced elements' actual text under kind "aria-labelledby"
  (the auditor's probe now prints "Your postcode", not "lbl9"). A
  reference that is missing or textless yields kind
  "aria-labelledby-unresolved": the form record marks the field
  unlabelled and the report prints **ABSENT** with the note
  "(aria-labelledby names an element that is not on this page — the
  field has no readable label)". The raw IDREF never appears as a
  label anywhere.
- **F2 — `<input type="image">` is a submit, not a field.** The
  parser's input split now routes image inputs to the form's submit
  candidates (name = its `alt`, falling back to `value` then
  `aria-label`), and submit selection treats type=image as a real
  submit. The auditor's probe shape now yields one text field and
  submit "Pay now" (alt), instead of a phantom unlabelled `image`
  field and submit "none found".
- **F3 — an empty label element no longer shadows aria.** Label
  resolution now prefers actual readable text: a `<label for>` (or
  wrapping label) with no text falls through to aria-label and then
  resolved aria-labelledby; only when no source yields text does the
  report declare "(label element present, no readable text)" — the
  probe case (empty label-for + aria-label "Real name") now prints
  "Real name". Non-empty label-element text keeps its v0 precedence,
  so every previously covered case resolves exactly as before.
- **F4 — files written before printing.** `main()` now writes the
  `--out` Markdown + receipts JSON first and prints the report
  afterward, so a closed or truncated stdout pipe can no longer take
  the report files down with it. (Trivial, safe reorder — the two
  operations are independent.)

**Self-review of the diff:** changes are confined to `PageAudit`
(id-text capture; the input submit/field split; two additive field
keys `aria_label`/`aria_labelledby` — the conflated `aria` key and
`unlabelled_fields()` are untouched, so v0's counts logic is
unchanged), `field_label()`, `form_records()` submit selection, the
ABSENT-note rendering, and `main()`'s write/print order. Field
element receipts keep their exact attribute set. Verified beyond the
suite: the auditor's F1 and F2 probe shapes reproduce fixed by hand,
and the v0 SAMPLE page yields its original counts (2 links / 1
unnamed / 1 unlabelled / 3 fields). Known residual approximation,
accepted: id-text capture closes an element on the first matching
end tag, so pathological same-tag nesting around a labelledby
target could truncate its text — referenced elements in practice
are simple spans/headings, and a truncated resolution degrades to
the honest ABSENT-with-note, never to a wrong label. **Not
certified** — these fixes await the fresh audit lane's re-check
(Law 2), same as the build did.
