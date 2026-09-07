# Advanced Phishing Threat Tracker

An entropy-based domain analyzer and HTTP redirect tracker built in Python for Kali Linux.

## Features
- **Entropy Analysis:** Calculates Shannon Entropy to catch algorithmically generated random domains.
- **Homograph Defense:** Captures IDN homograph impersonation attacks using Punycode conversion filters.
- **Redirect Unpacking:** Automatically follows layered redirect chains to expose target payloads.
