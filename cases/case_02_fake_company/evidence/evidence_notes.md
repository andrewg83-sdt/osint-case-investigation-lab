# Evidence Notes

Case:

`case_02_fake_company`

Target:

`novatrust-digital-example.com`

## Evidence Log

| Time | Source / Tool | Observation | Analyst Note |
| --- | --- | --- | --- |
| 2026-04-21 10:10 UTC | WHOIS simulation | Domain created `2026-03-29` | Recent for claimed established business |
| 2026-04-21 10:18 UTC | `dig A` | A record resolves to `203.0.113.76` | Lab documentation IP |
| 2026-04-21 10:21 UTC | `host NS` | Generic site-provider nameservers | Not conclusive |
| 2026-04-21 10:25 UTC | `dig MX` | MX record exists | Positive/neutral finding |
| 2026-04-21 10:29 UTC | `dig TXT` | SPF exists | Better than no SPF |
| 2026-04-21 10:32 UTC | `dig _dmarc` | DMARC exists with `p=none` | Monitoring only |
| 2026-04-21 10:40 UTC | Search simulation | Thin public footprint | Main business-consistency concern |
| 2026-04-21 10:48 UTC | Archive simulation | No older snapshots | Supports recent-presence concern |

## Chain of Evidence Notes

The simulated evidence is documented so the case can be reviewed offline.

I kept technical findings separate from interpretation because some findings are positive or neutral. For example, SPF and DMARC exist, but the business identity still needs validation.
