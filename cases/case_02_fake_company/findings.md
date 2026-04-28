# Findings

## Summary

`NovaTrust Digital Services` has a weak and recently established simulated public presence. The domain setup is not obviously malicious, but the business claims are not well supported by the available evidence.

The main concern is not one technical failure. It is the mismatch between the sensitive request and the limited public footprint.

## Fraud Indicators

### Recent Domain

The simulated WHOIS data shows the domain was created on `2026-03-29`.

This is recent for a company claiming international clients and multiple offices.

### Thin Digital Presence

The simulated search results show only:

- the company website
- one low-detail directory listing
- no older archive history
- no independent references

This would require further validation in a real investigation.

### Generic Business Claims

The company describes itself as a digital trust and payment security provider, but the public footprint does not support that level of maturity.

This could be a new small company. It could also be a fake identity.

### Sensitive Request

The message asks for identity documents during onboarding.

That increases the risk because the impact of trusting the wrong entity is high.

### Basic Website Infrastructure

The simulated headers indicate a basic site builder.

That is not suspicious by itself, but it does not match the claimed business profile very well.

## Email Security Findings

### MX

MX exists:

`mail.novatrust-digital-example.com`

### SPF

SPF exists:

`v=spf1 include:mail.simple-site-example.org ~all`

### DMARC

DMARC exists:

`v=DMARC1; p=none; rua=mailto:dmarc@novatrust-digital-example.com`

The policy is monitoring-only. This is better than no DMARC, but it does not enforce rejection or quarantine.

## Risk Level

Medium

## Confidence

Medium

The case has several concerns, but it does not contain enough evidence to label the company as confirmed fraudulent.

## Analyst Assessment

I would not provide documents or personal information based only on the received message. I would try to validate the company through independent channels first.
