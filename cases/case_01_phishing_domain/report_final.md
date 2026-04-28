# Final Report: Phishing Domain Investigation

## Executive Summary

The simulated domain `secure-login-alert-example.com` presents several characteristics commonly associated with phishing infrastructure. The domain name is security-themed, the simulated registration is very recent, mail authentication appears weak, and the HTTP redirect points to a login verification path.

Based on the available simulated evidence, I would rate this domain as high risk for phishing activity.

## Scope

Target:

`secure-login-alert-example.com`

Allowed activity:

- passive DNS checks
- WHOIS-style review
- HTTP header review
- TLS certificate review
- documentation of findings

Out of scope:

- vulnerability scanning
- form interaction
- credential testing
- file downloads
- attribution claims

## Technical Analysis

The strongest issue is the pattern of indicators rather than any single item.

The domain name appears designed around account security language. The simulated WHOIS data shows a very recent creation date, which is a common feature of short-lived phishing domains. DNS records show generic nameservers and a low TTL. The domain also lacks visible SPF and DMARC records in the simulated checks.

The HTTP header response redirects to `/login/verify`, which fits the initial phishing hypothesis. The TLS certificate is valid, but it was issued shortly after the simulated domain creation date. That supports the idea of recently deployed infrastructure, not trust.

## IoC List

| Type | Value | Notes |
| --- | --- | --- |
| Domain | `secure-login-alert-example.com` | Fictional lab domain |
| IPv4 | `198.51.100.42` | Documentation-range IP used for simulation |
| URL path | `/login/verify` | Simulated redirect path |
| Nameserver | `ns1.temp-hosting-example.net` | Fictional nameserver |
| Nameserver | `ns2.temp-hosting-example.net` | Fictional nameserver |

## Risk Level

High

## Recommendations

- Treat the domain as suspicious in the context of the reported email.
- Preserve the original email with full headers if this were a real case.
- Check whether any users clicked the link.
- Search proxy, DNS, and email gateway logs for the domain.
- Add temporary detections for the domain and related URL path.
- Review similar domains using the same naming pattern.

## Limitations

This case is simulated. In a real investigation I would need:

- original email headers
- full URL from the message
- page content captured in a controlled environment
- passive DNS history
- certificate transparency history
- user telemetry or proxy logs

I would also avoid claiming attribution from this evidence alone.

## Personal Note

This case helped me practice not jumping straight from "suspicious" to "confirmed malicious." The domain looks bad in context, but the useful part is explaining why the indicators matter and where the evidence stops.
