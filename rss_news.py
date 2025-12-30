import urllib.request
import time
import json
import os
from xmltodict import parse


def get_news(
        urls: dict,
):
    """
    Get information from the news source, and form a message to be sent.

    Args:
        urls: Dictionary with the new's site name and their rss-feed url.
    
    Returns:
        body: String with the updated body of the message.
    """

    body = ""

    # Compute 12h ago in RFC3339 format
    published_after = time.strftime(
        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (12 * 60 * 60))
    )

    for name, rss_url in urls.items():
        new_body = ""
        response = urllib.request.urlopen(rss_url)
        response_parsed = parse(response.read().decode('utf-8'))

        try:
            # Try to get the info from this news source
            i = 0
            while True:
                try:
                    # get the title, but if there is none, get the description
                    news = response_parsed['rss']['channel']['item'][i]['title']
                except:
                    news = response_parsed['rss']['channel']['item'][i]['description']
                    news = news[:news.find('\n')]  # limit the size to the content of a single line

                # get the date, ignoring the timezone
                news_published_str = response_parsed['rss']['channel']['item'][i]['pubDate'][:-6]

                try:
                    # most rss feeds are in one of these 2 time formats
                    news_published_obj = time.strptime(news_published_str, "%a, %d %b %Y %H:%M:%S")
                except:
                    news_published_obj = time.strptime(news_published_str, "%d %b %Y %H:%M")
                
                news_published = time.strftime("%Y-%m-%dT%H:%M:%SZ", news_published_obj)

                if news_published < published_after:
                    break  # if the news is older than 12h, we don't want it
                
                new_body += f"- {news}\n"

                i += 1
                if i == 5:
                    break

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
