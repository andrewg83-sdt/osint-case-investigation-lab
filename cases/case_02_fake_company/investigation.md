# Investigation Notes

Target:

`novatrust-digital-example.com`

Company:

`NovaTrust Digital Services`

Date of simulated investigation:

`2026-04-21`

## Step 1: Company Name Review

The company name sounds plausible but generic. `Trust`, `Digital`, and `Services` are common business words and can be used by real companies or fake entities.

This is only a starting observation. I would not treat the name alone as suspicious.

## Step 2: Domain Registration Review

Command:

```bash
whois novatrust-digital-example.com
```

Simulated output:

```text
Domain Name: NOVATRUST-DIGITAL-EXAMPLE.COM
Registrar: Example Registrar LLC
Creation Date: 2026-03-29T15:42:08Z
Updated Date: 2026-04-02T08:12:55Z
Registry Expiry Date: 2027-03-29T15:42:08Z
Name Server: NS1.SIMPLE-SITE-EXAMPLE.ORG
Name Server: NS2.SIMPLE-SITE-EXAMPLE.ORG
Registrant Organization: Redacted for Privacy
Registrant Country: IS
```

Reasoning:

The simulated domain is less than a month old. That does not prove fraud, but it conflicts with the claim of an established company with international clients.

## Step 3: A and NS Records

Command:

```bash
dig novatrust-digital-example.com A
```

Simulated output:

```text
novatrust-digital-example.com. 600 IN A 203.0.113.76
```

Command:

```bash
host -t NS novatrust-digital-example.com
```

Simulated output:

```text
novatrust-digital-example.com name server ns1.simple-site-example.org.
novatrust-digital-example.com name server ns2.simple-site-example.org.
```

Reasoning:

The domain resolves and appears hosted through a simple website provider. That can be normal for a small company, but it does not strongly support the claimed maturity of the business.

## Step 4: MX Record Check

Command:

```bash
dig novatrust-digital-example.com MX
```

Simulated output:

```text
novatrust-digital-example.com. 600 IN MX 10 mail.novatrust-digital-example.com.
```

Reasoning:

The domain has an MX record. That means it is configured to receive mail, at least in the simulation.

## Step 5: SPF and DMARC Checks

Command:

```bash
dig novatrust-digital-example.com TXT
```

Simulated output:

```text
novatrust-digital-example.com. 600 IN TXT "v=spf1 include:mail.simple-site-example.org ~all"
```

Command:

```bash
dig _dmarc.novatrust-digital-example.com TXT
```

Simulated output:

```text
_dmarc.novatrust-digital-example.com. 600 IN TXT "v=DMARC1; p=none; rua=mailto:dmarc@novatrust-digital-example.com"
```

Reasoning:

SPF exists, which is a positive sign. DMARC also exists, but the policy is `p=none`, so it monitors rather than enforces. This is common during setup. It is not a fraud indicator by itself.

## Step 6: HTTP Header Check

Command:

```bash
curl -I https://novatrust-digital-example.com
```

Simulated output:

```text
HTTP/2 200
server: simple-site
content-type: text/html; charset=utf-8
last-modified: Tue, 02 Apr 2026 08:44:11 GMT
x-powered-by: SiteBuilder Basic
```

Reasoning:

The site appears to use a basic site builder. That is not suspicious on its own, but it feels inconsistent with a company claiming to provide payment security consulting at an international level.

## Step 7: Digital Presence Check

Simulated public search results:

```text
Result 1: novatrust-digital-example.com - NovaTrust Digital Services
Result 2: NovaTrust Digital Services profile - business-directory-example.net
Result 3: No independent news, client references, or older archived pages found
```

Simulated archive check:

```text
No snapshots before April 2026.
```

Reasoning:

The company has a thin public footprint. The only visible results are the website and a low-detail directory listing. For a business claiming international clients, I would expect more independent references.

This would require further validation in a real investigation.

## Step 8: Email Consistency Analysis

Observed sender in simulated report:

`recruiting@novatrust-digital-example.com`

Claimed signature:

```text
NovaTrust Digital Services
Payments Risk and Identity Verification Team
London | Dublin | Singapore
```

Reasoning:

The email domain matches the website domain, which is better than using a free mailbox. Still, the claimed office locations are not supported by the simulated public footprint. I would want to validate business registration, employee profiles, and independent references before trusting the request.

## Step 9: Correlation

The strongest concerns are:

- very recent domain
- thin digital footprint
- generic business language
- sensitive onboarding request
- claimed international presence without supporting evidence
- basic website infrastructure

Some positive or neutral points:

- domain has MX
- SPF exists
- DMARC exists, although not enforced
- HTTPS is available

My view: suspicious enough to avoid sharing documents until the company identity is independently verified.
