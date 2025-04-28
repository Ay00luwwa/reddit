# Scraping Reddit Data Respectfully

This guide outlines how to scrape Reddit data while **adhering to** the platform's [`robots.txt`](https://www.reddit.com/robots.txt) rules and avoiding potential misuse of public content.

---

## Problem

When attempting to scrape Reddit's `/r/funny/` subreddit using Scrapy, the following message appears:

```
2025-04-28 22:02:26 [scrapy.core.engine] INFO: Spider opened
2025-04-28 22:02:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.reddit.com/robots.txt> (referer: None)
2025-04-28 22:02:28 [scrapy.downloadermiddlewares.robotstxt] DEBUG: Forbidden by robots.txt: <GET https://www.reddit.com/r/funny/>
```

This indicates that Scrapy, by default, **respects the `robots.txt` file**, which disallows scraping of `/r/funny/`.

---

## Solution

To access Reddit data **without violating `robots.txt` rules**, use the **JSON endpoint** for public subreddits.

---

### Step 1: Access the JSON Endpoint

Public subreddits expose their posts in **JSON format**, which can be accessed without authentication.

**Example URL:**

```
https://www.reddit.com/r/funny/.json
```

This endpoint provides subreddit data in a structured JSON format, making it easier to parse and extract information.

---

### Important Disclaimer

Always adhere to Reddit's official policies:

- [Reddit Public Content Policy](https://support.reddithelp.com/hc/en-us/articles/26410290525844-Public-Content-Policy)
- [Reddit Robots.txt](https://www.reddit.com/robots.txt)

Respect their guidelines when accessing or using Reddit content.

