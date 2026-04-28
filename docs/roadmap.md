# Roadmap

These are improvements I would like to add later. I kept the first version simple so the investigation notes stay readable.

## Planned Improvements

- HTML/PDF report export
- VirusTotal API integration
- AbuseIPDB integration
- graph correlation with `networkx`
- Streamlit dashboard
- improved scoring logic
- MITRE ATT&CK mapping section for each case
- certificate transparency lookup support
- passive DNS history support
- optional JSON output from the Python tool

## Notes

The main thing to improve is the scoring logic. Right now it is intentionally basic. A better version should separate domain risk, email-security risk, hosting risk, and business-context risk.

I would also like to make the reports exportable, but I do not want the project to become just a dashboard. The writing and reasoning are the point of this lab.
