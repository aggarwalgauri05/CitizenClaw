#!/usr/bin/env python3
import sys
import argparse
import requests
from urllib.parse import urlparse

APPROVED_DOMAINS = [
    'myscheme.gov.in',
    'pmkisan.gov.in',
    'pmjay.gov.in',
    'nrega.nic.in',
    'scholarships.gov.in',
    'pmaymis.gov.in',
    'india.gov.in',
    'labour.gov.in',
    'nfsa.gov.in'
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--query', required=False)
    args = parser.parse_args()

    url = args.url
    domain = urlparse(url).netloc
    # Normalize domain for comparison (strip www, etc.)
    domain = domain.lstrip('www.')

    if not any(d in domain for d in APPROVED_DOMAINS):
        print(f"[BLOCKED] Domain not in approved whitelist: {domain}")
        print("[REASON] Policy constraint: only .gov.in domains")
        sys.exit(1)

    print(f"[ALLOWED] Fetching from approved domain: {url}")
    print(f"[SOURCE] {url}")
    try:
        resp = requests.get(url, timeout=10)
        text = resp.text[:3000]
        print(text)
    except requests.RequestException as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
