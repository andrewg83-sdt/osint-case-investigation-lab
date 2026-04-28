# Analyst Log

This is a rougher note file for Case 01. It is not written like a final report on purpose.

## First impression

The domain name immediately looked suspicious because it uses the words `secure`, `login`, and `alert`. That said, I did not want to mark it as phishing only because of the name. A lot of weak investigations start by assuming the conclusion too early.

## Checks I cared about most

The checks that mattered most to me were:

- domain age
- SPF and DMARC
- where the domain redirects
- whether the TLS certificate was new
- whether the infrastructure looked temporary

The HTTP redirect to `/login/verify` was the most interesting simulated result because it matched the original lure idea.

## What I would ask for in a real ticket

If this came from a real alert or user report, I would ask for:

- the full email headers
- the exact URL from the email
- timestamp of the user report
- whether the user clicked anything
- proxy or DNS logs around the time of the email

Without that, the domain analysis is useful, but still incomplete.

## My conclusion

I would treat this as high risk in the lab scenario. I would still avoid saying it is confirmed malicious unless I had the original email and more telemetry.
