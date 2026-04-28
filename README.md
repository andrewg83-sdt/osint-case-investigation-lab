# OSINT Case Investigation Lab

This repository is a small OSINT and Cyber Threat Intelligence lab that I built to practice documenting investigations in a way that is close to how I would work through a real junior analyst task.

The cases are simulated. The domains, companies, infrastructure, outputs, and findings are fictional and are only used for training and portfolio purposes.

## Why I Built This Lab

I wanted a project that shows more than just running tools. In OSINT work, the hard part is usually deciding what an indicator means, what it does not mean, and how confident I should be before writing it down.

This lab helped me practice:

- defining investigation scope before collecting data
- checking DNS, WHOIS-style data, web headers, and email security records
- separating weak indicators from stronger patterns
- writing short reports with limitations included
- thinking about false positives and missing context
- keeping investigations passive and ethical

## Repository Structure

```text
osint-case-investigation-lab/
├── methodology/              OSINT workflow and investigation logic
├── cases/                    Simulated investigation cases
│   ├── case_01_phishing_domain/
│   └── case_02_fake_company/
├── tools/                    Small passive DNS helper script and report template
└── docs/                     Interview notes and future roadmap
```

## Cases Included

### Case 01: Phishing Domain Investigation

This case looks at a fictional domain:

`secure-login-alert-example.com`

The goal is to evaluate whether the domain shows signs commonly associated with phishing infrastructure, such as suspicious naming, weak mail authentication, and inconsistent infrastructure.

### Case 02: Fake Company Investigation

This case looks at a fictional company:

`NovaTrust Digital Services`

Domain:

`novatrust-digital-example.com`

The goal is to practice validating whether a business has a believable digital footprint and whether its domain/email setup matches the claimed identity.

## Python Tool

The repository includes a simple passive DNS checker:

```bash
python tools/osint_domain_check.py example.com
```

It checks:

- A records
- MX records
- TXT records
- NS records
- SPF presence
- DMARC presence
- basic risk score based on missing records or DNS errors

Install dependencies:

```bash
pip install -r requirements.txt
```

The script uses `dnspython` and optionally uses `rich` for nicer terminal output. If `rich` is not installed, it falls back to normal print output.

## Ethical Scope

This lab is limited to passive OSINT techniques. It does not include exploitation, vulnerability scanning, brute forcing, credential testing, social engineering, or interaction with real suspicious infrastructure.

In a real investigation I would only collect data that is permitted by scope, law, and the rules of engagement.

## Personal Note

I created this project because I wanted to get better at writing down my reasoning, not just collecting indicators. I also wanted to practice being careful with conclusions. A suspicious domain name or missing DMARC record can be useful context, but it does not prove malicious activity by itself.

What I wanted to improve most was the habit of explaining confidence level, limitations, and what I would check next if this was a real case.

## License

This project is released under the MIT License.
