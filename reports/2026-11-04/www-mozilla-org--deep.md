# Is it AI friendly? — https://www.mozilla.org/

Scanned from: scanner network (one vantage point). One vantage point, raw fetches only (no JavaScript run) — which is also what the AI crawlers get.

## Verdict

- The door is honest: every major AI bot that robots.txt welcomes actually gets the page.
- The page skeleton is clean: every link, button and form field carries a name an agent can read.
- No working sitemap (fetch of https://www.mozilla.org/sitemap.xml returned 404) — crawlers get no map of the site.
- Beyond the homepage: audited 25 of 98 pages found (cap 25, via homepage links (no usable sitemap)).
- Across the site, 43 forms hold 113 fields and every field carries a label.

## The door — declared vs actual

| Visitor | robots.txt says | Actually got |
|---|---|---|
| Browser (baseline) | — | 200 (47808 bytes, 374 ms) |
| GPTBot | allowed | served |
| ClaudeBot | allowed | served |
| Googlebot | allowed | served |

## What crawlers receive (no JavaScript)

- Readable words in the raw page: **314**
- Script tags on the page: 8
- App-shell container: none detected
- Page title: Internet for people, not profit — Mozilla Global
- H1 headings: ['Choose your language or locale to browse Mozilla.org']
- Meta description: yes

## Labels an agent navigates by

- Links: 135 total, **0 unnamed**
- Buttons: 5 total, **0 unnamed**
- Form fields: 0 total, **0 with no label**
- Images: 11 total, **0 with no alt attribute**

## Plumbing

- robots.txt: found (status 200, 3 directive lines)
- Sitemap: https://www.mozilla.org/sitemap.xml — status 404, — entries

## Information only — NOT scored

- llms.txt: status 404. (Research: no major AI system is known to read it; presence proves nothing.)
- Structured data (JSON-LD) blocks: 0. (Research: helps systems understand content; controlled studies show it does not buy AI citations.)

## Site crawl (v0.2a)

- Source: homepage links (no usable sitemap).
- URLs found: 98; pages audited: 25 (cap 25 — the cap cut the list).
- (The sections above describe the homepage; this section and the next cover the whole crawl.)

| Page | Forms | Fields | Unlabelled fields |
|---|---|---|---|
| https://www.mozilla.org/ | 0 | 0 | 0 |
| https://www.mozilla.org/en-US/privacy/websites/cookie-settings/ | 2 | 5 | 0 |
| https://www.mozilla.org/en-US/ | 2 | 6 | 0 |
| https://www.mozilla.org/en-US/products/ | 2 | 2 | 0 |
| https://www.mozilla.org/en-US/products/vpn/ | 1 | 1 | 0 |
| https://www.mozilla.org/en-US/products/monitor/ | 1 | 1 | 0 |
| https://www.mozilla.org/en-US/about/ | 1 | 1 | 0 |
| https://www.mozilla.org/en-US/about/manifesto/ | 1 | 1 | 0 |
| https://www.mozilla.org/en-US/contribute/ | 2 | 5 | 0 |
| https://www.mozilla.org/en-US/advertising/ | 1 | 1 | 0 |
| https://www.mozilla.org/ach/ | 2 | 6 | 0 |
| https://www.mozilla.org/ar/ | 2 | 6 | 0 |
| https://www.mozilla.org/ast/ | 2 | 6 | 0 |
| https://www.mozilla.org/be/ | 2 | 6 | 0 |
| https://www.mozilla.org/bg/ | 2 | 6 | 0 |
| https://www.mozilla.org/br/ | 2 | 6 | 0 |
| https://www.mozilla.org/bs/ | 2 | 6 | 0 |
| https://www.mozilla.org/ca/ | 2 | 6 | 0 |
| https://www.mozilla.org/cak/ | 2 | 6 | 0 |
| https://www.mozilla.org/cs/ | 2 | 6 | 0 |
| https://www.mozilla.org/cy/ | 2 | 6 | 0 |
| https://www.mozilla.org/da/ | 2 | 6 | 0 |
| https://www.mozilla.org/de/ | 2 | 6 | 0 |
| https://www.mozilla.org/dsb/ | 2 | 6 | 0 |
| https://www.mozilla.org/el/ | 2 | 6 | 0 |

## Forms — field by field (v0.2a)

43 forms, 113 fields, **0 with no label** across the crawl. A field's label is what a screen reader announces and what an agent navigates by; a placeholder is not a label. Every field below is quoted as the element actually found — the receipt, not a summary of it.

### Form 1 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/privacy/websites/cookie-settings/
- Sends to: https://www.mozilla.org/en-US/privacy/websites/cookie-settings/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="radio" name="cookie-radio-preference" id="cookie-radio-preference-yes">` | I Agree | cookie-radio-preference | radio | no | absent |
| `<input type="radio" name="cookie-radio-preference" id="cookie-radio-preference-no">` | I Do Not Agree | cookie-radio-preference | radio | no | absent |
| `<input type="radio" name="cookie-radio-analytics" id="cookie-radio-analytics-yes">` | I Agree | cookie-radio-analytics | radio | no | absent |
| `<input type="radio" name="cookie-radio-analytics" id="cookie-radio-analytics-no">` | I Do Not Agree | cookie-radio-analytics | radio | no | absent |

Submit control: "Save Changes" — `<button type="submit">`

### Form 2 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/privacy/websites/cookie-settings/
- Sends to: https://www.mozilla.org/en-US/privacy/websites/cookie-settings/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 3 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/en-US/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Select country or region: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Select language: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | I’m okay with Mozilla handling my info as explained in  this Privacy Notice | privacy | checkbox | yes | absent |

Submit control: "Sign Up Now
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 4 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/
- Sends to: https://www.mozilla.org/en-US/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 5 — appears to be: email signup (newsletter or lead capture)

*Purpose is an inference* — from: an email field and little else; the destination says no more.
- Page: https://www.mozilla.org/en-US/products/
- Sends to: https://accounts.firefox.com/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="email" name="email" id="fxa-email-field" placeholder="user@example.com" autocomplete="email" required>` | Email address | email | email | yes | email |

Submit control: "Continue" — `<button type="submit" id="fxa-email-form-submit">`

### Form 6 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/products/
- Sends to: https://www.mozilla.org/en-US/products/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 7 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/products/vpn/
- Sends to: https://www.mozilla.org/en-US/products/vpn/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 8 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/products/monitor/
- Sends to: https://www.mozilla.org/en-US/products/monitor/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 9 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/about/
- Sends to: https://www.mozilla.org/en-US/about/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 10 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/about/manifesto/
- Sends to: https://www.mozilla.org/en-US/about/manifesto/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 11 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/en-US/contribute/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | about-mozilla | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Select country or region: | country | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | I’m okay with Mozilla handling my info as explained in  this Privacy Notice | privacy | checkbox | yes | absent |

Submit control: "Sign Up Now
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 12 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/contribute/
- Sends to: https://www.mozilla.org/en-US/contribute/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 13 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/en-US/advertising/
- Sends to: https://www.mozilla.org/en-US/advertising/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 14 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/ach/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Select country or region: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Select language: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | I’m okay with Mozilla handling my info as explained in  this Privacy Notice | privacy | checkbox | yes | absent |

Submit control: "Sign Up Now
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 15 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/ach/
- Sends to: https://www.mozilla.org/ach/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 16 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/ar/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | عنوان البريد الإلكتروني: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | حدد البلد أو المنطقة: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | اختر لغة: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | ليس لديَّ مشكلة في معالجة شركة Mozilla لمعلوماتي كما هو موضح في  إشعار الخصوصية هذا | privacy | checkbox | yes | absent |

Submit control: "سجّل الآن
          
           
           
             جاري الإرسال" — `<button type="submit" id="newsletter-submit">`

### Form 17 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/ar/
- Sends to: https://www.mozilla.org/ar/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | اللغة | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 18 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/ast/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Firefox | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="correu-de-to@exemplu.com" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Select country or region: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Llingües disponibles: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | I’m okay with Mozilla handling my info as explained in  this Privacy Notice | privacy | checkbox | yes | absent |

Submit control: "Rexistrase agora
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 19 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/ast/
- Sends to: https://www.mozilla.org/ast/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Llingua | lang | text | no | absent |

Submit control: "Dir" — `<button type="submit">`

### Form 20 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/be/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Firefox | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Ваш электронны адрас: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Выберыце краіну або рэгіён: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Абраць мову: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Я згодны з тым, як Mozilla звяртаецца з маімі дадзенымі згодна з  гэтым паведамленнем аб прыватнасцi | privacy | checkbox | yes | absent |

Submit control: "Зарэгістравацца зараз
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 21 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/be/
- Sends to: https://www.mozilla.org/be/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Мова | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 22 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/bg/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Firefox | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Адрес на електронна поща: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Изберете държава: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Изберете език: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Съгласен съм Mozilla да разполага с данните ми, както е обяснено в  тази Политика за личните данни | privacy | checkbox | yes | absent |

Submit control: "Абониране
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 23 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/bg/
- Sends to: https://www.mozilla.org/bg/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Език | lang | text | no | absent |

Submit control: "Напред" — `<button type="submit">`

### Form 24 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/br/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Select country or region: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Select language: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | I’m okay with Mozilla handling my info as explained in  this Privacy Notice | privacy | checkbox | yes | absent |

Submit control: "Sign Up Now
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 25 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/br/
- Sends to: https://www.mozilla.org/br/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Language | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 26 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/bs/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="ime@example.com" required>` | Vaša email adresa: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Odaberite državu ili regiju: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Izaberite jezik: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Slažem se da se Mozilla koristi mojim informacijama kao što je objašnjeno u  ovoj obavjesti o privatnosti | privacy | checkbox | yes | absent |

Submit control: "Registrujte se sada
          
           
           
             Šaljem" — `<button type="submit" id="newsletter-submit">`

### Form 27 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/bs/
- Sends to: https://www.mozilla.org/bs/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Jezik | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 28 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/ca/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Firefox | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="ADREÇA ELECTRÒNICA" required>` | Your email address: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Seleccioneu l'estat: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Llengües disponibles: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Accepto que Mozilla gestioni la meva informació en els termes descrits en l' avís de privadesa | privacy | checkbox | yes | absent |

Submit control: "Subscriviu-vos-hi ara
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 29 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/ca/
- Sends to: https://www.mozilla.org/ca/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Llengua | lang | text | no | absent |

Submit control: "Vés-hi" — `<button type="submit">`

### Form 30 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/cak/
- Sends to: https://basket.mozilla.org/news/subscribe/ (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Firefox | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Rochochib'al ataqoya'l: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Ticha' Amaq' o k'ojlib'äl: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Wachel taq ch'ab'äl: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Ütz rub'anon chi nuwäch rusamajixik ri wetamab'al pa Mozilla achi'el niq'alajisäx pa  re ichinan runa'oj | privacy | checkbox | yes | absent |

Submit control: "Tatz'ib'aj awi' wakami
          
           
           
             Sending" — `<button type="submit" id="newsletter-submit">`

### Form 31 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/cak/
- Sends to: https://www.mozilla.org/cak/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Ch'ab'äl | lang | text | no | absent |

Submit control: "Jo'" — `<button type="submit">`

### Form 32 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/cs/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="vase-adresa@example.com" required>` | Vaše e-mailová adresa: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Vyberte zemi nebo oblast: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Vyberte jazyk: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Souhlasím s tím, aby Mozilla zpracovávala mé informace tak, jak je popsáno v  zásadách ochrany osobních údajů | privacy | checkbox | yes | absent |

Submit control: "Přihlásit se
          
           
           
             Odesílá se" — `<button type="submit" id="newsletter-submit">`

### Form 33 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/cs/
- Sends to: https://www.mozilla.org/cs/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Jazyk | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 34 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/cy/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="eichenw@example.com" required>` | Eich cyfeiriad e-bost: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Dewiswch wlad neu ardal: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Dewiswch Iaith: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Rwy'n fodlon i Mozilla drin fy manylion fel mae'n cael ei esbonio yn y  Datganiad Preifatrwydd hwn | privacy | checkbox | yes | absent |

Submit control: "Cofrestrwch nawr
          
           
           
             Anfon" — `<button type="submit" id="newsletter-submit">`

### Form 35 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/cy/
- Sends to: https://www.mozilla.org/cy/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Iaith | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 36 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/da/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="navn@eksempel.dk" required>` | Din mailadresse: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Vælg land eller region: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Vælg sprog: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Det er helt fint, at Mozilla håndterer mine oplysninger som beskrevet i  denne privatlivserklæring | privacy | checkbox | yes | absent |

Submit control: "Tilmeld mig
          
           
           
             Sender" — `<button type="submit" id="newsletter-submit">`

### Form 37 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/da/
- Sends to: https://www.mozilla.org/da/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Sprog | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 38 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/de/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="deinname@example.com" required>` | Deine E-Mail-Adresse: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Land oder Region auswählen: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Sprache wählen: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Ich bin einverstanden, dass Mozilla meine Daten wie in  diesem Datenschutzhinweis  angegeben verwendet | privacy | checkbox | yes | absent |

Submit control: "Jetzt abonnieren
          
           
           
             Sendevorgang" — `<button type="submit" id="newsletter-submit">`

### Form 39 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/de/
- Sends to: https://www.mozilla.org/de/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Sprache | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 40 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/dsb/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="wasome@example.com" required>` | Waša e-mailowa adresa: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Kraj abo region wubraś: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Rěc wubraś: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Som z tym wobjadny, kak Mozilla wobchada pó  toś tych pšawidłach priwatnosći  z mójimi informacijami | privacy | checkbox | yes | absent |

Submit control: "Registrěrujśo se něnto
          
           
           
             Słanje" — `<button type="submit" id="newsletter-submit">`

### Form 41 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/dsb/
- Sends to: https://www.mozilla.org/dsb/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Rěc | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

### Form 42 — appears to be: newsletter signup

*Purpose is an inference* — from: an email field, and the form's destination identifies a mailing list or subscription.
- Page: https://www.mozilla.org/el/
- Sends to: https://abdri3ttkb.execute-api.us-east-2.amazonaws.com/api/newsletter/mozillaorg (method post)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<input type="checkbox" name="newsletters" id="id_newsletters_0">` | Mozilla Foundation | newsletters | checkbox | no | absent |
| `<input type="email" name="email" id="id_email" placeholder="yourname@example.com" required>` | Η διεύθυνση email σας: | email | email | yes | absent |
| `<select name="country" id="id_country" required>` | Επιλέξτε χώρα ή περιοχή: | country | text | yes | absent |
| `<select name="lang" id="id_lang" required>` | Επιλογή γλώσσας: | lang | text | yes | absent |
| `<input type="checkbox" name="privacy" id="privacy" required>` | Δέχομαι την επεξεργασία των πληροφοριών μου από τη Mozilla, όπως εξηγεί η  Δήλωση απορρήτου . | privacy | checkbox | yes | absent |

Submit control: "Εγγραφή τώρα
          
           
           
             Αποστολή" — `<button type="submit" id="newsletter-submit">`

### Form 43 — appears to be: general form

*Purpose is an inference* — from: no strong signals in the destination, identity or fields.
- Page: https://www.mozilla.org/el/
- Sends to: https://www.mozilla.org/el/ (method get)

| Field (element as found) | Label | Name | Type | Required | Autocomplete |
|---|---|---|---|---|---|
| `<select name="lang" id="page-language-select">` | Γλώσσα | lang | text | no | absent |

Submit control: **none found in the skeleton** — a visitor has no visible way to send this form.

## Not checked in v0.2a

- A live agent task run (the Inspector, v0.2b) — protocol specced at goals/ai-friendly-website-scanner/files/inspector-run-protocol-2026-11-04.md; it runs through a browser seat, not this code.
- Rendered-vs-raw diff in a real browser (v0.2a measures the raw response, which is what crawlers receive).
- Anything past a submit click; login flows.
