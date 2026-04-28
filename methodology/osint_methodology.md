# OSINT Methodology

This is the workflow I used for the simulated cases in this lab. It is practical on purpose. I wanted something I could follow during a real entry-level investigation without pretending that OSINT gives perfect answers.

## 1. Scope Definition

Before collecting anything, I define:

- the target domain, company, email, or indicator
- what question I am trying to answer
- what sources are allowed
- what activity is out of scope
- what output is expected

For this lab, the scope is passive OSINT only. No scanning, exploitation, login attempts, credential testing, or contacting people.

I also write down the initial hypothesis. This helps me avoid drifting into random collection.

## 2. Data Collection

Typical passive sources and checks:

- DNS records
- WHOIS/RDAP style registration data where available
- certificate transparency references
- HTTP response headers
- public search engine results
- archived pages if relevant
- public social/company presence
- email security records

The goal is not to collect everything. The goal is to collect enough data to answer the investigation question with a reasonable confidence level.

## 3. Source Validation

I try to avoid relying on a single source. If one tool says a record exists, I prefer to confirm with another source or another query type.

Things I check:

- whether the source is current
- whether the result could be cached
- whether the domain is parked or inactive
- whether a missing record is meaningful or just normal for that domain
- whether the indicator could be shared hosting or a CDN

This is where false positives and false negatives matter. A domain can look suspicious and still be benign. A malicious domain can also have normal-looking records.

## 4. DNS and WHOIS Analysis

For DNS, I usually check:

- A records
- NS records
- MX records
- TXT records
- DMARC record at `_dmarc.domain`
- CNAME records if the domain uses hosted services

For WHOIS/RDAP-style data, I look for:

- registration date or first-seen date
- registrar
- nameserver changes
- privacy protection
- mismatches between claimed company identity and domain age

Privacy protection is not suspicious by itself. It is common. It becomes more interesting when combined with other indicators.

## 5. IP and ASN Analysis

If an A record resolves, I check:

- hosting provider
- ASN ownership
- geolocation at a rough level
- whether the provider is commonly used for temporary hosting
- whether multiple domains share the same IP

Shared infrastructure is not proof of malicious activity. I treat it as context.

## 6. Email Security Checks

I check the following records:

- MX: can the domain receive mail?
- SPF: does the domain define allowed sending sources?
- DKIM: not always easy to check without selectors, so I note the limitation
- DMARC: is there a policy for handling failed authentication?

For phishing-related cases, missing SPF or DMARC can increase risk, but it is not conclusive. Some legitimate small businesses have weak email security.

## 7. Correlation of Indicators

I do not treat one indicator as enough. I look for clusters:

- suspicious domain naming
- recent registration
- missing mail authentication
- inconsistent hosting
- no credible web presence
- vague business claims
- mismatch between claimed company maturity and public footprint

Each item is an Indicator of Compromise, or IoC, only when it is useful for detection or investigation. Some observations are just weak signals.

## 8. Risk Scoring Logic

For this lab I use simple scoring:

- Low: limited suspicious signals, normal infrastructure
- Medium: multiple weak indicators or one strong concern
- High: several related suspicious indicators and likely user risk

I keep the score explainable. A score without reasoning is not very useful.

## 9. MITRE ATT&CK Mapping

For phishing cases, I map activity to:

- MITRE ATT&CK T1566 - Phishing

This mapping is not a verdict. It is a way to describe the likely tactic or technique if the domain was being used for credential theft, malicious links, or impersonation.

## 10. OPSEC

Even passive OSINT needs basic OPSEC:

- avoid logging into suspicious sites
- avoid submitting personal data
- avoid opening unknown files
- avoid interacting with forms
- avoid using personal accounts for investigation
- record what was checked and when

For real suspicious infrastructure, I would use a controlled environment and follow the organization's rules.

## 11. Chain of Evidence

For each case I keep notes on:

- date of observation
- tool or source used
- command or query
- result summary
- interpretation

This is not a legal evidence process, but it helps make the work repeatable and easier to review.

## 12. Report Writing

My report structure:

- executive summary
- scope
- key findings
- technical details
- IoC list
- risk level
- recommendations
- limitations

I try to separate facts from interpretation. For example, "DMARC was not found" is a fact in the lab. "This may increase phishing risk" is interpretation.

## 13. Limitations of OSINT

OSINT can miss important context:

- private registration data
- internal mail logs
- takedown history
- user reports
- threat actor intent
- backend infrastructure hidden by CDNs
- short-lived DNS changes

Because of this, OSINT findings should usually support a decision, not replace a full investigation.
