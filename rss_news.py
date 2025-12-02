import urllib.request
import json
import time


def get_news(
        rss_url: str,
        title: str,
        body: str,
):
    """
    Get information from the news source, and form a message to be sent.

    Args:
        rss_url: String of the news rss website whose content you want.
        title: String of this section for the email.
        body: String with the current body of the email, to which the new information will be appended.
    
    Returns:
        body: String with the updated body of the email.
    """

    try:
        # Compute 24h10min ago in RFC3339 format
        published_after = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (24 * 60 * 60) - (10 * 60))
        )
    except Exception as e:
        body += f"{e}"

    new_body = ""

    try:
        response = json.load(urllib.request.urlopen(rss_url))
        content = ""  # GET THE CONTENT
        new_body += f"{content}\n"
    except:
        pass
    
    if new_body != "":  # there's information to be added
        body += f"{title}:\n{new_body}\n"  # extra blank line at the end

    print("Done " + title)

    return body


if __name__ == '__main__':

    body = ""

    # SOME GENERAL NEWS
    body = get_news('https://www.rtp.pt/noticias/rss/pais', 'RTP Noticias Portugal', body)  # example of the rss of rtp, a portuguese news source
    body = get_news('https://www.rtp.pt/noticias/rss/mundo', 'RTP Noticias Mundo', body)
    body = get_news('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'RTP Noticias Portugal', body)  # example of the rss of another news source
    body = get_news('https://rss.nytimes.com/services/xml/rss/nyt/World.xml', 'RTP Noticias Mundo', body)

    # SOME PURELY POSITIVE NEWS
    body = get_news('https://www.goodnewsnetwork.org/category/news/world/feed/', 'Good News World', body)
    body = get_news('https://www.goodnewsnetwork.org/category/news/science/feed/', 'Good News Science', body)
    body = get_news('https://www.goodnewsnetwork.org/category/news/health/feed/', 'Good News Health', body)
    body = get_news('https://www.goodnewsnetwork.org/category/news/inspiring/feed/', 'Good News Inspiring', body)