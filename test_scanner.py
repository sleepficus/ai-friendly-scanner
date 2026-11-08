import unittest

import scanner


class RobotsTests(unittest.TestCase):
    def test_specific_group_beats_star(self):
        groups, _, _, _ = scanner.parse_robots(
            "User-agent: *\nDisallow: /\n\n"
            "User-agent: GPTBot\nDisallow:\n")
        self.assertEqual(scanner.robots_verdict(groups, "GPTBot"), "allowed")
        self.assertEqual(scanner.robots_verdict(groups, "ClaudeBot"),
                         "disallowed")

    def test_longest_rule_wins(self):
        groups, _, _, _ = scanner.parse_robots(
            "User-agent: *\nDisallow: /admin\nAllow: /admin/public\n")
        self.assertEqual(scanner.robots_verdict(groups, "X", "/admin/panel"),
                         "disallowed")
        self.assertEqual(scanner.robots_verdict(groups, "X", "/admin/public/x"),
                         "allowed")

    def test_sitemaps_collected(self):
        _, maps, _, _ = scanner.parse_robots("Sitemap: https://e.com/s.xml\n")
        self.assertEqual(maps, ["https://e.com/s.xml"])

    def test_comment_only_preamble_has_no_directives(self):
        # the misfitcircuit.com shape: a content-signals preamble, all
        # comments, nothing filled in
        groups, maps, signals, n = scanner.parse_robots(
            "# content signals explained here\n# search: yes means...\n")
        self.assertEqual(n, 0)
        self.assertEqual(signals, {})
        self.assertEqual(scanner.robots_verdict(groups, "GPTBot"), "allowed")

    def test_content_signals_parsed(self):
        _, _, signals, n = scanner.parse_robots(
            "User-agent: *\nContent-Signal: search=yes, ai-train=no\n")
        self.assertEqual(signals, {"search": "yes", "ai-train": "no"})
        self.assertGreaterEqual(n, 2)


SAMPLE = """<html><head><title>T</title>
<meta name="description" content="d">
<script type="application/ld+json">{}</script></head>
<body><h1>Hello</h1>
<a href="/x"></a><a href="/y">Named</a>
<button></button><button aria-label="Go"></button>
<form><input type="text" name="email" placeholder="Email">
<label for="n">Name</label><input id="n" type="text">
<label>Wrapped <input type="text" name="w"></label></form>
<img src="a.png"><img src="b.png" alt=""><img src="c.png" alt="Cat">
<div id="root"></div>
<script>var x = "not words";</script>
</body></html>"""


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.a = scanner.PageAudit()
        self.a.feed(SAMPLE)

    def test_unnamed(self):
        self.assertEqual(len(self.a.unnamed_links()), 1)
        self.assertEqual(len(self.a.unnamed_buttons()), 1)

    def test_fields(self):
        un = self.a.unlabelled_fields()
        self.assertEqual(len(un), 1)          # only the placeholder-only one
        self.assertEqual(un[0]["name"], "email")

    def test_images(self):
        self.assertEqual(len(self.a.images_missing_alt()), 1)  # alt="" is present

    def test_basics(self):
        self.assertEqual(self.a.title, "T")
        self.assertEqual(self.a.h1_texts, ["Hello"])
        self.assertEqual(self.a.jsonld, 1)
        self.assertEqual(self.a.app_shell_id, "root")
        self.assertGreater(self.a.text_words, 0)

    def test_img_alt_names_wrapping_link(self):
        a = scanner.PageAudit()
        a.feed('<a href="/home"><img src="logo.png" alt="Home"></a>'
               '<a href="/x"><img src="i.png" alt=""></a>')
        un = a.unnamed_links()
        self.assertEqual(len(un), 1)
        self.assertEqual(un[0]["href"], "/x")


class FakeResp:
    def __init__(self, status, body):
        self.status, self._b = status, body
        self.headers, self._u = {}, "https://e.com/"
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False
    def geturl(self):
        return self._u
    def read(self, n=-1):
        return self._b


class ScanTests(unittest.TestCase):
    def fake_fetch(self, url, ua):
        r = scanner.FetchResult(url)
        if url.endswith("/robots.txt"):
            r.status, r.body = 200, b"User-agent: GPTBot\nDisallow: /\n"
        elif url.endswith("/sitemap.xml"):
            r.status, r.body = 200, b"<urlset><loc>a</loc><loc>b</loc></urlset>"
        elif url.endswith("/llms.txt"):
            r.status = 404
        else:
            r.status, r.body = 200, SAMPLE.encode()
            if ua == scanner.BOTS["ClaudeBot"]:
                r.status = 403
        return r

    def test_paper_only_and_silent_block(self):
        r = scanner.scan("https://e.com/", fetcher=self.fake_fetch)
        self.assertIn("PAPER-ONLY BAN", r["door"]["GPTBot"].get("mismatch", ""))
        self.assertIn("SILENT BLOCK", r["door"]["ClaudeBot"].get("mismatch", ""))
        self.assertEqual(r["sitemap"]["entries"], 2)
        text = " ".join(scanner.verdict_lines(r))
        self.assertIn("turned away at the door", text)
        self.assertIn("not the real rule", text)


FORM_PAGE = """<html><head><title>Site</title></head><body>
<form action="https://lists.example.com/subscribe" method="post" id="mc">
<input type="email" name="EMAIL" placeholder="Email address" required>
<input type="submit" value="Subscribe">
</form>
<form action="/contact" method="post">
<label for="sender">Your email</label>
<input id="sender" type="email" name="sender" autocomplete="email">
<label for="msg">Your message</label>
<textarea id="msg" name="message"></textarea>
<label>Your name <input type="text" name="fullname" autocomplete="name"></label>
<button type="submit">Send message</button>
</form>
</body></html>"""


class FormAuditTests(unittest.TestCase):
    def setUp(self):
        self.a = scanner.PageAudit()
        self.a.feed(FORM_PAGE)
        self.records = self.a.form_records("https://e.com/")

    def test_forms_found(self):
        self.assertEqual(len(self.records), 2)

    def test_unlabelled_field_caught_with_receipt(self):
        f = self.records[0]["fields"][0]
        self.assertFalse(f["labelled"])
        self.assertIsNone(f["label"])
        self.assertEqual(f["name"], "EMAIL")
        self.assertTrue(f["required"])
        self.assertIn('name="EMAIL"', f["element"])  # skeleton receipt

    def test_labelled_fields_pass(self):
        fields = self.records[1]["fields"]
        self.assertTrue(all(fd["labelled"] for fd in fields))
        self.assertEqual(fields[0]["label"], "Your email")
        self.assertEqual(fields[0]["autocomplete"], "email")
        self.assertEqual(fields[2]["label"], "Your name")  # wrapping label

    def test_submit_names(self):
        self.assertEqual(self.records[0]["submit"]["name"], "Subscribe")
        self.assertEqual(self.records[1]["submit"]["name"], "Send message")

    def test_purpose_is_inference_with_evidence(self):
        self.assertEqual(self.records[0]["purpose"], "newsletter signup")
        self.assertEqual(self.records[1]["purpose"], "contact")
        for rec in self.records:
            self.assertTrue(rec["purpose_evidence"])  # never bare


def fake_site_fetch(pages, sitemap_body=None, robots_body=None):
    """pages: {url: html}. sitemap_body None -> 404 sitemap."""
    def fake_fetch(url, ua):
        r = scanner.FetchResult(url)
        if url.endswith("/robots.txt"):
            r.status = 200
            r.body = (robots_body if robots_body is not None
                      else "User-agent: *\n").encode()
        elif url.endswith("/sitemap.xml"):
            if sitemap_body is None:
                r.status = 404
            else:
                r.status, r.body = 200, sitemap_body.encode()
        elif url.endswith("/llms.txt"):
            r.status = 404
        elif url in pages:
            r.status, r.body = 200, pages[url].encode()
        else:
            r.status = 404
        return r
    return fake_fetch


class CrawlTests(unittest.TestCase):
    def test_cap_respected(self):
        locs = "".join(f"<loc>https://e.com/p{i}</loc>"
                       for i in range(30))
        pages = {"https://e.com/": "<html><body>home</body></html>"}
        fetch = fake_site_fetch(
            pages, sitemap_body=f"<urlset>{locs}</urlset>")
        urls, source, total = scanner.collect_urls(
            "https://e.com/", fetcher=fetch, cap=25)
        self.assertEqual(len(urls), 25)          # cap holds
        self.assertEqual(total, 31)              # homepage + 30, pre-cap
        self.assertIn("sitemap", source)

    def test_homepage_link_fallback(self):
        home = ('<html><body><a href="/a">A</a><a href="/b">B</a>'
                '<a href="https://other.com/x">X</a>'
                '<a href="/img.png">img</a></body></html>')
        fetch = fake_site_fetch({"https://e.com/": home},
                                sitemap_body=None)
        urls, source, total = scanner.collect_urls(
            "https://e.com/", fetcher=fetch)
        self.assertEqual(urls, ["https://e.com/", "https://e.com/a",
                                "https://e.com/b"])
        self.assertIn("homepage links", source)


class ScanSiteTests(unittest.TestCase):
    def test_forms_aggregated_across_pages(self):
        page2 = ('<html><body><form role="search" action="/s">'
                 '<input type="search" name="q" aria-label="Search">'
                 '<button type="submit">Go</button></form>'
                 '</body></html>')
        sitemap = ('<urlset><loc>https://e.com/</loc>'
                   '<loc>https://e.com/p2</loc></urlset>')
        fetch = fake_site_fetch(
            {"https://e.com/": FORM_PAGE, "https://e.com/p2": page2},
            sitemap_body=sitemap)
        r = scanner.scan_site("https://e.com/", fetcher=fetch)
        self.assertEqual(r["crawl"]["pages_audited"], 2)
        self.assertEqual(len(r["forms"]), 3)
        unlab = sum(1 for f in r["forms"] for fd in f["fields"]
                    if not fd["labelled"])
        self.assertEqual(unlab, 1)               # only the EMAIL field
        purposes = [f["purpose"] for f in r["forms"]]
        self.assertIn("search", purposes)
        text = scanner.render_site_report(r)
        self.assertIn("inference", text)         # purpose labelled
        self.assertIn("ABSENT", text)            # unlabelled shown


class FormAuditFixTests(unittest.TestCase):
    """Regression tests for the independent audit's findings F1–F3
    (AUDIT-REPORT.md, 2026-11-04). The auditor's probe cases are the
    spec for each fix."""

    def test_f1_labelledby_resolves_to_referenced_text(self):
        a = scanner.PageAudit()
        a.feed('<span id="lbl9">Your postcode</span>'
               '<form action="/x" method="post">'
               '<input type="text" name="pc" aria-labelledby="lbl9">'
               '<input type="submit" value="Go"></form>')
        fd = a.form_records("https://e.com/")[0]["fields"][0]
        self.assertTrue(fd["labelled"])
        self.assertEqual(fd["label"], "Your postcode")  # never "lbl9"
        self.assertEqual(fd["label_kind"], "aria-labelledby")

    def test_f1_labelledby_missing_reference_is_absent(self):
        a = scanner.PageAudit()
        a.feed('<form action="/x" method="post">'
               '<input type="text" name="pc" aria-labelledby="ghost">'
               '<input type="submit" value="Go"></form>')
        fd = a.form_records("https://e.com/")[0]["fields"][0]
        self.assertFalse(fd["labelled"])
        self.assertIsNone(fd["label"])                   # never "ghost"
        self.assertEqual(fd["label_kind"],
                         "aria-labelledby-unresolved")

    def test_f2_image_input_is_the_submit(self):
        a = scanner.PageAudit()
        a.feed('<form action="/x" method="post">'
               '<label for="q">Query</label>'
               '<input id="q" type="text" name="q">'
               '<input type="image" src="go.png" alt="Search now">'
               '</form>')
        rec = a.form_records("https://e.com/")[0]
        self.assertEqual(len(rec["fields"]), 1)  # image is not a field
        self.assertEqual(rec["fields"][0]["type"], "text")
        self.assertIsNotNone(rec["submit"])      # ... it is the submit
        self.assertEqual(rec["submit"]["name"], "Search now")  # its alt

    def test_f3_empty_label_for_falls_through_to_aria_label(self):
        a = scanner.PageAudit()
        a.feed('<form action="/x" method="post">'
               '<label for="z"></label>'
               '<input id="z" type="text" name="z" '
               'aria-label="Real name">'
               '<input type="submit" value="Go"></form>')
        fd = a.form_records("https://e.com/")[0]["fields"][0]
        self.assertTrue(fd["labelled"])
        self.assertEqual(fd["label"], "Real name")
        self.assertEqual(fd["label_kind"], "aria-label")


if __name__ == "__main__":
    unittest.main()
