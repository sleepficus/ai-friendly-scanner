# Audit Report — Scanner Revival (v0 re-verification + v0.2a + v0.2b spec)

**Date:** 2026-11-04 · **Auditor:** Muse, fresh lane (did not build
this) · **Audited against:** BUILD-REPORT.md (builder's claims, not
taken on word) · **Method:** all tests and scans run in a scratch copy
(`/tmp/scanner-audit/`); the original tree was only read. Live claims
verified against the sites directly with curl.

## Verdict: CERTIFY-WITH-FINDINGS

Every headline claim in the build report was independently reproduced.
Three minor correctness defects were found in edge cases of the new
form audit (F1–F3), plus one info-level observation (F4). None of them
contradicts a builder claim; all three affect the accuracy of the
field-by-field receipts in cases the builder's tests do not cover.

---

## Verification log

### File identity — PASS
Full SHA-256 of the tree matches the build report exactly:
- `scanner.py` — `0f4c490ce6ff75bc95e8598951d13901d4735540ddc39063b618124a5a586a8b`
- `test_scanner.py` — `68984dd38ca0a7a9c61e90d26591319241c3bdfa0695164255357906f1770bcf`

### Test suite — PASS (19/19, counts and content)
`Ran 19 tests — OK` in the scratch copy. Inventory confirms the split:
11 v0 tests (RobotsTests ×5, AuditTests ×5, ScanTests ×1) + 8 new
(FormAuditTests ×5, CrawlTests ×2, ScanSiteTests ×1). All 8 new tests
were read, not just counted — each asserts what its name claims:
placeholder-only field caught with its element receipt; `for`-label,
wrapping label, and autocomplete capture; submit names from both
`<input type=submit>` and `<button>`; purpose always paired with
non-empty evidence; crawl cap (31 found → 25 returned, pre-cap total
reported); homepage-link fallback excluding external and asset links;
cross-page aggregation (3 forms, exactly 1 unlabelled, rendered report
contains "inference" and "ABSENT").

### v0 re-verification — PASS
Auditor's own homepage scans reproduce the builder's dated
2026-11-04 receipts exactly for misfitcircuit.com, and for
watercolormisfit.com on every field except the llms.txt byte count
(26,500 vs 26,496 — the byte size of the site's own 404 page body,
an info-only field whose status, 404, agrees; immaterial).

Live claims confirmed with curl, independent of the scanner:
- MC robots.txt is exactly `User-agent: * / Allow: / / Sitemap: …` =
  **3 directive lines** by the tool's counting (was 0 on 2026-10-23). ✓
- MC sitemap.xml: **HTTP 200, exactly 36 `<loc>` entries** (was 404). ✓
- MC homepage scan: 979 raw words, 42 links / 0 unnamed, llms.txt
  200 / 1,032 bytes — all as claimed. ✓
- WCM: 323 raw words, 33 links / 3 unnamed, robots 5 directive lines,
  sitemap index 200 with exactly 5 child sitemaps (curl-confirmed) —
  materially unchanged from Oct 23, as claimed. ✓

That WCM — a site that did not change — reproduces its Oct 23 numbers
to the digit through the current code is also the evidence that v0's
default (non-`--deep`) behavior survived the v0.2a changes intact.

### v0.2a live deep runs — PASS
Auditor's own `--deep` runs match the builder's receipts:
- MC: crawl {36 found, cap 25, 25 audited} and the forms array are
  **identical** — 1 form (/php-check/), field labelled "Your PHP
  version", submit "Check it", purpose printed as inference. ✓
- WCM: crawl {index, 5 children read, 217 found, 25 audited}, the
  audited page list and form page list are **identical** to the
  builder's — 25 forms / 25 fields / **0 unlabelled**; the site-search
  field is labelled "Search articles", submit named by aria-label
  "Search". ✓

### Adversarial probes (auditor's own fixtures) — 4 PASS, 3 findings
- **Placeholder as only "label" → ABSENT.** PASS: labelled=False,
  label=None; the placeholder is reported as placeholder only.
- **aria-label submit vs unnamed submit.** PASS: aria-label submit
  named ("Join the list"); a bare `<input type=submit>` and an empty
  `<button type=submit>` both report name=None with the element as
  receipt (rendered as "no accessible name").
- **Autocomplete present/absent.** PASS: captured ("email") when
  present, None → rendered "absent" when not.
- **Sitemap over cap.** PASS: a 41-URL fake sitemap at cap 25 renders
  "URLs found: 41; pages audited: 25 (cap 25 — the cap cut the list)"
  in both the crawl section and the verdict line. Found-vs-audited is
  printed honestly.
- **Submit selection.** PASS: a `type=button` control before a real
  submit is correctly skipped.

### v0.2b spec — PASS against doctrine
`inspector-run-protocol-2026-11-04.md` is labeled SPEC ONLY / not
built / not run in its own header. No score anywhere (§4 headlines are
plain English with counts; §6: "No scoring"). Guesses are labelled
GUESS and "never upgraded to clean passes" (§3). The submission
boundary is unambiguous: attempt **without submitting anything**, the
run ends at the last step before the submit/commit action, and if the
first step *is* a submission that is recorded as the stall (§1, §6).
Execution route (Tally's browser route, never simulated from static
fetches) is stated in the header and §6.

---

## Findings

**F1 — Minor. aria-labelledby labels are misquoted in the receipt.**
A field labelled only via `aria-labelledby` is counted labelled
(consistent with v0), but `field_label()` returns the raw IDREF
string as the label *text* — the report prints e.g. `lbl9` in the
Label column, under kind "aria-label" — never resolving the
referenced element's actual text ("Your postcode"). The labelled
counts are right; the quoted label is wrong. Probe: field with
`aria-labelledby="lbl9"` → reported label text `'lbl9'`. Fix
direction: resolve IDREFs against element text (the parser would
need an id→text pass), or print "aria-labelledby (unresolved ref)".

**F2 — Minor. `<input type="image">` is misclassified as an
unlabelled field, and the form's submit vanishes.** The parser's
submit/field split excludes only hidden/submit/button input types,
so an image submit becomes a "field" of type `image`, counts as
unlabelled (inflating the headline unlabelled count by one), and the
form record reports submit=None — rendered as "none found in the
skeleton — a visitor has no visible way to send this form," which is
false: the image control *is* the submit, and its `alt` is its name.
Legacy pattern, but the failure lands on the tool's headline finding
species. Probe: form with an image submit → fields
`[('text', True), ('image', False)]`, submit None. Fix direction:
treat `type=image` as a submit candidate whose name is its alt.

**F3 — Minor. An empty `<label for>` shadows a working aria-label.**
`field_label()` checks label-for first and returns its (empty) text;
a field with `<label for="z"></label>` plus `aria-label="Real name"`
renders as "(label element present, no readable text)" although an
accessible name exists — in the real accessible-name computation
aria-label takes precedence over the associated label. The field is
counted labelled (correct), but the report understates its naming.
Fix direction: prefer a non-empty aria-label over an empty label
text, or report both.

**F4 — Info. `main()` prints the full report to stdout before
writing `--out` files.** If stdout is a closed/truncated pipe, the
print raises and the report files are never written (the auditor hit
this once with a `| head` pipe; re-run without the pipe wrote both
files correctly). Not a correctness defect in any artifact; noted
because the build report's Step 1 describes a stdout-vs-files
anomaly of its own — in every auditor run where the pipe stayed
open, stdout, Markdown reports, and receipts JSONs agreed exactly.

---

## Bottom line

The revival is what the build report says it is: v0 verified
untouched and still accurate, v0.2a's crawl and field-by-field form
audit reproduce live to the digit on both of Stephen's sites, the
no-score / guesses-labelled / placeholder-is-not-a-label doctrine
holds under adversarial probing, and the v0.2b spec keeps the
attempt-without-submitting boundary clean. F1–F3 are worth fixing
before the form audit's receipts are quoted publicly — they are
receipt-accuracy defects in edge cases, not claim defects.

**CERTIFY-WITH-FINDINGS.**

---

## Addendum — fixes re-check (fresh lane, 2026-11-04)

**Verdict: CERTIFY-FIXES.** The F1–F3 fixes in the FIX-LOG
(BUILD-REPORT.md) are verified; F4's reorder is covered by the
suite and the code path it touches (see item 1 note). This was a
fixes re-check only — no wholesale re-audit of v0.2a.

1. **Suite: 23/23 OK**, run in a scratch copy
   (`/tmp/scanner-recheck/`); the original tree was only read, plus
   this append. The 4 new `FormAuditFixTests` were read, not just
   counted — each asserts its finding's fixed behavior with exact
   values: F1-resolved (label == "Your postcode", kind
   "aria-labelledby"), F1-missing (labelled False, label None, kind
   "aria-labelledby-unresolved"), F2 (exactly 1 field, submit name
   from the image input's alt), F3 (label == "Real name", kind
   "aria-label").
2. **Original audit probes re-run independently** (re-checker's own
   probe script, 21/21 checks, at both the form-record level and
   the rendered-report level):
   - F1: the Label column prints "Your postcode"; the raw IDREF
     never appears as a label. A missing reference renders
     "**ABSENT** (aria-labelledby names an element that is not on
     this page — the field has no readable label)" and the missing
     id never appears as a label.
   - F2: the probe used the audit's shape with `alt="Pay now"` —
     fields are exactly `[text]`, no phantom image field, submit
     name "Pay now"; the rendered report makes no "no visible way
     to send" claim and headlines 1 field / 0 unlabelled.
   - F3: empty `<label for>` + `aria-label="Real name"` prints
     "Real name" at both levels.
3. **No regressions:** the v0 SAMPLE page still yields 2 links /
   1 unnamed / 1 unlabelled / 3 fields. A fresh homepage-mode scan
   of watercolormisfit.com yields 323 words / 33 links / 3 unnamed,
   with the receipts' content block identical to the builder's
   dated `reports/2026-11-04/` receipt.
4. **File identity:** full SHA-256 of the current tree matches the
   FIX-LOG exactly — `scanner.py`
   `2995f926c961768ad0c98612d68f09f4a4f9e33ba8bd57b00975897bf4d1a648`,
   `test_scanner.py`
   `158cebfa8bb9d647586572bdd8aff9c6d10e13bd292431054202a962de965e7c`
   (verified on the original tree and on the scratch copies).

F1–F3 are closed. The form audit's receipts may now be quoted
publicly on the strength of both audit passes.
