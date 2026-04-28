# Investigation Notes

Target:

`secure-login-alert-example.com`

Date of simulated investigation:

`2026-04-20`

## Step 1: Domain Naming Review

The domain uses words that are common in phishing lures:

- secure
- login
- alert

This does not prove anything by itself. Some real services use similar words. Still, the combination is generic and seems designed to create urgency.

## Step 2: WHOIS-Style Check

Command:

```bash
whois secure-login-alert-example.com
```

Simulated output:

```text
Domain Name: SECURE-LOGIN-ALERT-EXAMPLE.COM
Registrar: Example Registrar LLC
Creation Date: 2026-04-18T09:14:22Z
Updated Date: 2026-04-18T09:16:10Z
Registry Expiry Date: 2027-04-18T09:14:22Z
Name Server: NS1.TEMP-HOSTING-EXAMPLE.NET
Name Server: NS2.TEMP-HOSTING-EXAMPLE.NET
Registrant Organization: Redacted for Privacy
Registrant Country: PA
```

What I checked:

- creation date
- registrar
- nameservers
- privacy use

Reasoning:

The domain appears recently created in this simulated data. A recent creation date is a common risk factor for phishing domains, especially when combined with security-themed naming. Privacy protection is normal and not suspicious alone.

## Step 3: A Record Lookup

Command:

```bash
dig secure-login-alert-example.com A
```

Simulated output:

```text
secure-login-alert-example.com. 300 IN A 198.51.100.42
```

What I checked:

I wanted to see whether the domain resolves and whether the TTL looks temporary.

Reasoning:

The domain resolves to a documentation-range IP in this lab. The low TTL would make infrastructure changes easier. Low TTLs are not malicious by themselves, but they are common in disposable setups.

## Step 4: Nameserver Lookup

Command:

```bash
nslookup -type=ns secure-login-alert-example.com
```

Simulated output:

```text
secure-login-alert-example.com nameserver = ns1.temp-hosting-example.net
secure-login-alert-example.com nameserver = ns2.temp-hosting-example.net
```

What I checked:

I checked whether the nameservers looked like a stable company setup or temporary hosting.

Reasoning:

The simulated nameservers suggest generic temporary hosting. This is not conclusive because many small sites use inexpensive hosting, but it does not help establish trust.

## Step 5: MX Record Lookup

Command:

```bash
host -t MX secure-login-alert-example.com
```

Simulated output:

```text
secure-login-alert-example.com mail is handled by 10 mail.secure-login-alert-example.com.
```

What I checked:

I wanted to know whether the domain could receive mail.

Reasoning:

The domain has an MX record pointing to itself. That may be fine, but for a supposed security notification domain, I would expect clearer mail provider configuration or a recognizable sending platform.

## Step 6: TXT, SPF, and DMARC

Command:

```bash
dig secure-login-alert-example.com TXT
```

Simulated output:

```text
secure-login-alert-example.com. 300 IN TXT "verification=74219"
```

Command:

```bash
dig _dmarc.secure-login-alert-example.com TXT
```

Simulated output:

```text
;; status: NXDOMAIN
```

What I checked:

- SPF record in TXT
- DMARC policy
- signs of email authentication

Reasoning:

No SPF record was visible in the simulated TXT response, and the DMARC record was missing. This could allow spoofing or weak mail handling. This indicator alone is not conclusive because some small or unused domains have poor email configuration.

## Step 7: HTTP Header Check

Command:

```bash
curl -I http://secure-login-alert-example.com
```

Simulated output:

```text
HTTP/1.1 302 Found
Server: nginx
Location: https://secure-login-alert-example.com/login/verify
Cache-Control: no-store
Content-Type: text/html
```

What I checked:

I checked whether the domain redirected to a login-looking path.

Reasoning:

The redirect path `/login/verify` matches the phishing hypothesis, but in a real case I would avoid loading the full page unless I had a controlled environment.

## Step 8: TLS Certificate Review

Command:

```bash
openssl s_client -connect secure-login-alert-example.com:443 -servername secure-login-alert-example.com
```

Simulated output:

```text
subject=CN=secure-login-alert-example.com
issuer=C=US, O=Example Automated CA, CN=Example TLS R3
notBefore=Apr 18 10:00:00 2026 GMT
notAfter=Jul 17 10:00:00 2026 GMT
Verify return code: 0 (ok)
```

What I checked:

- certificate common name
- issuer
- certificate age
- whether TLS was valid

Reasoning:

A valid TLS certificate does not mean the site is safe. It only means the certificate is valid for that domain. The certificate date being close to the domain creation date supports the idea that the site was recently set up.

## Step 9: Indicator Correlation

The stronger part of the case is not one single indicator. It is the combination:

- security-themed domain name
- recent registration in simulated WHOIS data
- low TTL
- missing SPF and DMARC
- redirect to login verification path
- new TLS certificate

My confidence would be medium to high in a lab report, but in a real case I would still want user email headers, message content, and any related URLs before making a final call.
