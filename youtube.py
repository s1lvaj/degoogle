import urllib.request
import time
import json
import os
from xmltodict import parse


def get_channel_info(
        channels: dict,
        title: str,
        body: str,
) -> str:
    
    """
    Get video information from youtube channels, and form a message with it.
    
    :param channels: Dictionary with the channel's name and their channel id.
    :type channels: dict
    :param title: String with the desired title for this section of the message.
    :type title: str
    :param body: String with the current body of the message, to which the new information will be appended.
    :type body: str

    :return: String with the updated body of the message.
    :rtype: str
    """

    # Compute 25h30min ago in RFC3339 format (github actions can take quite a long time to run)
    published_after = time.strftime(
        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (25 * 60 * 60) - (30 * 60))
    )

    new_body = ""
    for name, channel in channels.items():

        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel}"
        response = urllib.request.urlopen(url)
        response_parsed = parse(response.read().decode('utf-8'))

        try:
            # Try to get the info from this youtube channel
            i = 0
            while True:
                entry = response_parsed['feed']['entry'][i]
                video_title = entry['title']
                video_id = entry['yt:videoId']
                video_published = entry['published']

                if video_published < published_after:
                    break  # if the video is older than 1 day, we don't want it

                if '/shorts/' not in entry['link']['@href']:
                    # if the video is NOT a youtube short, it is added
                    new_body += f"**{name}:** {video_title} #watch?v={video_id}\n"
                
                i += 1
        except:
            pass
    
    if new_body != "":  # there's information to be added
        body += f"**{title}:**\n{new_body}\n"  # extra blank line at the end

    return body


if __name__ == '__main__':
    # Fetch CHANNEL_GROUPS from environment variables
    GROUPS = json.loads(os.getenv("CHANNEL_GROUPS", '{}'))  # Default to empty if not set

    body = "**Your Daily Subscription Activity:**\n\n"
    for group_title, channels in GROUPS.items():
        body = get_channel_info(channels, group_title, body)
    
    print(body)
