# Findings

## Summary

The simulated domain `secure-login-alert-example.com` shows multiple indicators that are commonly seen in phishing setups. None of the indicators prove malicious activity alone, but together they create a concerning pattern.

## Suspicious Indicators

### Recent Domain

The simulated WHOIS output shows the domain was created on `2026-04-18`, two days before the investigation date.

Recent domains are often used in phishing campaigns because they can be created quickly and abandoned quickly. This indicator alone is not conclusive.

### Phishing-Style Naming

The domain contains `secure`, `login`, and `alert`.

These words are often used to make a user feel urgency or trust. The name is generic and does not clearly identify a real brand or service.

### Weak or Missing Email Authentication

The simulated TXT lookup did not show SPF, and the DMARC lookup returned NXDOMAIN.

Missing SPF and DMARC can make it harder to protect against spoofing. This indicator alone is not conclusive because some legitimate domains are poorly configured.

### Infrastructure Inconsistency

The nameservers point to generic temporary hosting, while the domain presents itself as a security login alert service.

That mismatch does not prove phishing, but it weakens the credibility of the domain.

### Login Verification Redirect

The simulated HTTP response redirects to:

`/login/verify`

That path matches the theme of the suspected lure.

## Risk Level

High

## Confidence

Medium

The evidence is consistent with phishing infrastructure, but this lab does not include email headers, page content, user telemetry, or historical reputation data.

## Notes on False Positives

A new domain with weak email records can still be legitimate. A valid TLS certificate also does not mean a site is trustworthy. I would not block or report a real domain based on one of these indicators alone.
