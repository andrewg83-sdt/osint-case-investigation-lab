# Analyst Log

This is my rough note file for Case 02. I wanted this case to feel a bit less obvious than the phishing-domain case.

## First impression

The company name sounded believable enough at first glance. That was the point of the scenario. A fake company does not always look ridiculous or obviously malicious.

The first thing that made me cautious was the request for identity documents. Even if the website had looked fine, that kind of request raises the impact of being wrong.

## What felt inconsistent

The main mismatch was between the claimed company profile and the weak public footprint.

The domain had SPF and DMARC, so I could not honestly say the email setup was completely poor. But the business story still felt thin:

- recent domain
- no older archive history in the simulated notes
- generic website setup
- claimed international offices
- no strong independent references

## Why I marked it medium risk

I chose medium instead of high because some technical controls were present. It would be lazy to call everything fake just because the company is new.

In a real case, I would want to validate business registration and look for independent employee/company references before making a stronger call.

## What I learned from this one

This case made me think more about context. Technical records can look acceptable while the business claim still does not fully make sense.
