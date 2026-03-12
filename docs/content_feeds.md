# Content Feeds

This repository allows you to consume online content without using a Google account.

Instead of logging into YouTube or visiting news websites directly, the scripts use **RSS feeds** to retrieve updates from:

- YouTube channels
- News websites

This allows you to track new content while avoiding account-based tracking.

---

## YouTube RSS feeds

Every YouTube channel exposes a public RSS feed:

https://www.youtube.com/feeds/videos.xml?channel_id=<CHANNEL_ID>

The script `scripts/youtube.py` reads these feeds and retrieves the latest uploaded videos.

Your channel subscriptions must be provided using the environment variable:

`CHANNEL_GROUPS`

Example:

```json
{
  "Science": {
    "3Blue1Brown": "UCYO_jab_esuFRV4b17AJtAw",
    "Veritasium": "UCHnyfMqiRRG1u-2MsSQLbXA"
  }
}
```

---

## News RSS feeds

News websites often provide RSS feeds as well.

The script `scripts/rss_news.py` retrieves articles from those feeds.

The feeds are defined in the environment variable:

`RSS_NEWS_WEBSITES`

Example:

```json
{
  "New York Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
}
```

---

After defining the environment variables, the scripts can be executed:

```bash
python scripts/youtube.py
python scripts/rss_news.py
```

These scripts will fetch the most recent content and return the updates.