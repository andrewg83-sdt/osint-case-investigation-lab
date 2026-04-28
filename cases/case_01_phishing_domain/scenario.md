# Case 01: Phishing Domain Investigation

## Context

A user reports receiving a login warning email that appears to come from a security notification system. The link in the message points to:

`secure-login-alert-example.com`

The email text claims that the user's account will be locked unless they verify their login activity.

This case is simulated. The domain and all outputs are fictional.

## Investigation Goal

Determine whether the domain shows signs commonly associated with phishing infrastructure.

I am not trying to prove attribution. The goal is to assess risk and document the evidence clearly enough that another analyst could understand my reasoning.

## Target Asset

- Domain: `secure-login-alert-example.com`
- Indicator type: domain name
- Related suspected technique: MITRE ATT&CK T1566 - Phishing

## Initial Hypothesis

The domain may be intended to look like a generic login security alert page. My starting assumption is that the name itself is suspicious, but not enough to conclude malicious activity.

I want to check whether DNS, mail records, headers, and certificate behavior support or weaken the phishing hypothesis.

## Rules of Engagement

- Passive OSINT only
- No vulnerability scanning
- No brute forcing
- No form submission
- No authentication attempts
- No file downloads
- No interaction beyond basic header and certificate checks in the simulated output

## Expected Output

- suspicious indicators
- weak or missing indicators
- IoC list
- risk level
- recommendations
- limitations
