## Assumptions & Risks

### Assumptions
- The Alpha Vantage API returns data with consistent columns: `timestamp`,`close`
- The HTML table on `https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average` contains data.
- The ticker `AAPL` is valid and has data for the requested date range.
- Network connectivity is available and API key is valid.

### Risks
- If the API rate limit is exceeded, the request may fail.
- The website may change its HTML structure, breaking the scraper.
- Missing values in the scraped table may cause type inference issues.
- The `.env` file might be missing in a new environment, causing authentication errors.