# Lab Journal

These are my own notes from building the lab. I am keeping them separate from the final reports because the reports should stay clean, while this file is closer to how I actually think while working through the cases.

## Why I chose these two cases

I picked a phishing-style domain first because it is a common investigation path for junior SOC or CTI work. It also forced me to be careful with the wording. A domain can look suspicious without being proven malicious.

The fake company case was added because not every OSINT task is a clear phishing page. Sometimes the question is more basic: does this organization look real enough to trust? I wanted to practice that kind of judgement too.

## What I tried to avoid

I did not want this project to become a big list of tools. Tools are useful, but a recruiter or analyst reviewing the work should be able to see why I checked each thing.

I also tried not to write conclusions that are stronger than the evidence. For example, missing DMARC is a weakness, not automatic proof of fraud.

## Things I would improve later

The scoring system is still simple. It works for a lab, but I would not use it as-is in a real investigation. I would separate technical risk from business-context risk.

I would also like to add screenshots from a safe local lab environment. I avoided that in the first version because I wanted the repo to stay clean and based on fictional data only.

## Small lesson learned

The hardest part was not the DNS checks. The harder part was writing findings in a way that sounds honest: enough detail to be useful, but not pretending to know more than I actually know.
