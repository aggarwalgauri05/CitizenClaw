# gov-fetcher Skill

This skill allows fetching content from specific, approved government domains. It acts as a safeguard to ensure that external data retrieval is limited to trusted sources.

## Functionality

1.  **Domain Whitelisting**: The skill maintains a strict list of approved domains (all ending in `.gov.in`). Any attempt to fetch content from a domain not on this whitelist will be blocked. 
2.  **URL and Query Parameters**: It accepts a `--url` argument specifying the target web address and an optional `--query` argument (though the query parameter itself is not used for filtering by this skill, it's expected for compatibility with broader systems).
3.  **Fetching Content**: If the URL's domain is approved, the skill uses the `requests` library to fetch the content with a 10-second timeout.
4.  **Output**: 
    *   If a domain is blocked, it prints a specific `[BLOCKED]` message and `[REASON]`.
    *   If a domain is allowed, subsequent fetches will print `[ALLOWED]`, `[SOURCE]`, and the first 3000 characters of the fetched content.

## Usage

```bash
python fetch.py --url <URL> [--query <some_query>]
```

## Approved Domains

- `myscheme.gov.in`
- `pmkisan.gov.in`
- `pmjay.gov.in`
- `nrega.nic.in`
- `scholarships.gov.in`
- `pmaymis.gov.in`
- `india.gov.in`
- `labour.gov.in`
- `nfsa.gov.in`

