# Final Report: Fake Company Investigation

## Executive Summary

The simulated company `NovaTrust Digital Services` presents a questionable digital footprint. The domain `novatrust-digital-example.com` has some normal technical controls, including MX, SPF, and DMARC records, but the company's public presence is thin and recent.

The request for identity documents increases the risk. Based on the simulated evidence, I would rate this case as medium risk and recommend independent validation before any engagement.

## Scope

Target company:

`NovaTrust Digital Services`

Target domain:

`novatrust-digital-example.com`

Allowed activity:

- passive DNS review
- WHOIS-style review
- public presence check
- email consistency review
- report writing

Out of scope:

- contacting the company
- submitting forms
- creating accounts
- uploading documents
- active scanning

## Technical Analysis

The domain was created recently in the simulated registration data. It resolves to a hosted website and uses generic nameservers. The site appears to be built using a simple site builder, which is not automatically suspicious, but it does not strongly support the claimed business profile.

Email configuration is mixed. MX is present, SPF is present, and DMARC is present. The DMARC policy is set to `p=none`, which means monitoring only. That is common during early deployment, but a company handling identity or payment-security topics should ideally use stronger email controls.

The biggest issue is business consistency. The company claims multiple international locations and payment security work, but simulated search and archive checks do not show older history, client references, press mentions, or strong independent validation.

## IoC and Investigation Values

| Type | Value | Notes |
| --- | --- | --- |
| Company | `NovaTrust Digital Services` | Fictional company |
| Domain | `novatrust-digital-example.com` | Fictional lab domain |
| IPv4 | `203.0.113.76` | Documentation-range IP used for simulation |
| Email | `recruiting@novatrust-digital-example.com` | Simulated sender |
| MX | `mail.novatrust-digital-example.com` | Simulated mail host |
| SPF | `v=spf1 include:mail.simple-site-example.org ~all` | SPF present |
| DMARC | `v=DMARC1; p=none` | Monitoring-only policy |

## Risk Level

Medium

## Recommendations

- Do not submit identity documents through the linked form.
- Validate the company through independent trusted sources.
- Check business registration records for claimed office locations.
- Search for employee profiles and cross-check consistency.
- Ask for a verified contact channel from a known source.
- Preserve the original message and headers if this were a real case.

## Limitations

This case is simulated. In a real investigation, I would want:

- original email headers
- the complete URL and form behavior
- company registration checks
- independent phone or address validation
- historical DNS and passive DNS data
- archived website content
- external reputation sources

This would require further validation in a real investigation.

## Personal Note

This case was useful because it was less obvious than the phishing-domain case. Some controls were present, so I had to focus more on consistency and confidence instead of treating every technical weakness as a final answer.
