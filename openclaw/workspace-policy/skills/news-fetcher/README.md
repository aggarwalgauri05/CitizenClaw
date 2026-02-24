# news-fetcher Skill

This skill fetches recent news articles related to government schemes and civic topics.

## Functionality

1. **Input arguments**:
   - `--query` (required) – Search query string.
   - `--days` (required) – Number of days back to search (used for logging, not directly sent to GNews).

2. **Civic keyword filter**:
   The script checks whether the query contains any of the following keywords (case‑insensitive):
   - `scheme`
   - `yojana`
   - `government`
   - `ministry`
   - `welfare`
   - `pension`
   - `subsidy`
   - `benefit`
   - `policy`
   - `PM`
   - `CM`

   If none are present, the script prints a block message and exits with error code 1.

3. **Allowed queries**:
   When a civic keyword is found, the script prints an allowed message and proceeds.

4. **Fetching news**:
   - Primary source: **GNews API** using the provided API key `78a09a07215aef7b226b55b03dd02c94`.
   - Request URL: `https://gnews.io/api/v4/search` with query parameters:
       - `q` = `<query> India government`
       - `lang` = `en`
       - `country` = `in`
       - `max` = `5`
   - If the request fails (e.g., missing API key or network issue), the script falls back to the **PIB RSS feed** (`https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3`).

5. **Output**:
   For each of the top 5 articles (or items from the RSS feed if falling back), print:
   - Title
   - Source (or feed title)
   - Publication date
   - URL

   Format example:
   ```
   Title: <title>
   Source: <source>
   Date: <date>
   URL: <url>
   ```

6. **Error handling**:
   - If the query is blocked, exit with code 1 after printing the block message.
   - If both the GNews request and the RSS fallback fail, print an error and exit with code 1.

## Usage example
```bash
python news.py --query "new pension scheme" --days 2
```