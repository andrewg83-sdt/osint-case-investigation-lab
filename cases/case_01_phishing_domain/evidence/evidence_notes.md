# Evidence Notes

Case:

`case_01_phishing_domain`

Target:

`secure-login-alert-example.com`

## Evidence Log

| Time | Source / Tool | Observation | Analyst Note |
| --- | --- | --- | --- |
| 2026-04-20 09:20 UTC | WHOIS simulation | Domain created `2026-04-18` | Recent registration supports phishing hypothesis |
| 2026-04-20 09:25 UTC | `dig A` | A record resolves to `198.51.100.42` | Lab documentation IP, used as simulated hosting |
| 2026-04-20 09:29 UTC | `nslookup NS` | Generic temporary nameservers | Weak trust signal |
| 2026-04-20 09:35 UTC | `dig TXT` | No SPF found | Email authentication appears weak |
| 2026-04-20 09:37 UTC | `dig _dmarc` | NXDOMAIN | DMARC missing in simulation |
| 2026-04-20 09:44 UTC | `curl -I` | Redirect to `/login/verify` | Matches suspected lure |
| 2026-04-20 09:50 UTC | `openssl s_client` | Valid recent certificate | TLS validity does not equal legitimacy |

## Chain of Evidence Notes

These notes are not legal evidence. They are meant to show what was checked, when it was checked, and how I interpreted it.

The simulated outputs were kept in the investigation file so the case can be reviewed without needing to query real infrastructure.
