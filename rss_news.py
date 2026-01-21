import urllib.request
import json
import os
from datetime import datetime, timedelta, timezone
from xmltodict import parse


def get_news(
        urls: dict
) -> str:
    """
    Get information from the news source, and form a message to be sent.
    
    :param urls: Dictionary with the news site name and their rss-feed url.
    :type urls: dict

    :return: String with the updated body of the message.
    :rtype: str
    """

    body = ""

    # Compute 12 hours ago in UTC
    published_after = datetime.now(timezone.utc) - timedelta(hours=12)

    for name, rss_url in urls.items():
        new_body = ""
        response = urllib.request.urlopen(rss_url)
        response_parsed = parse(response.read().decode('utf-8'))

        try:
            # Try to get the info from this news source
            items = response_parsed['rss']['channel']['item']
            for i in range(min(5, len(items))):
                item = items[i]

                # get the title or, if it doesn't exist (returns None), get the description
                news = item.get('title') or item.get('description', '')
                news = news.split('\n')[0]  # limit the size to the content to a single line

                # get the published date
                news_published_str = item['pubDate']
                try:
                    # most rss feeds are in one of these 2 time formats
                    news_published = datetime.strptime(news_published_str, "%a, %d %b %Y %H:%M:%S %z").replace(tzinfo=timezone.utc)
                except:
                    news_published = datetime.strptime(news_published_str, "%d %b %Y %H:%M %z").replace(tzinfo=timezone.utc)

                if news_published < published_after:
                    break  # if the news is older than 12h, we don't want it

                new_body += f"- {news}\n"

            if new_body != "":  # there's information to be added
                body += f"**{name}:**\n{new_body}\n"

        except:
            pass
    
    return body


if __name__ == '__main__':
    
    # Fetch RSS_NEWS_WEBSITES from environment variables
    RSS_NEWS_WEBSITES = json.loads(os.getenv("RSS_NEWS_WEBSITES", '{}'))  # Default to empty if not set

    body = "**Some News From Today:**\n\n"
    body += get_news(RSS_NEWS_WEBSITES)

    print(body)
