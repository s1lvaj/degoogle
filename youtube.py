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
    Get information from the channels, and form a message with the information.

    Args:
        channels: Dictionary with the channel's name and their channel id.
        title: String of this section for the email.
        body: String with the current body of the email, to which the new information will be appended.
    
    Returns:
        body: String with the updated body of the email.
    """

    try:
        # Compute 25h30min ago in RFC3339 format (github actions can take quite a long time to run)
        published_after = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (25 * 60 * 60) - (30 * 60))
        )
    except Exception as e:
        body += f"{e}"

    new_body = ""
    for name, channel in channels.items():
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel}"
        i = 0
        while True:
            try:
                response = urllib.request.urlopen(url)
                response_parsed = parse(response.read().decode('utf-8'))
                video_title = response_parsed['feed']['entry'][i]['title']
                video_id = response_parsed['feed']['entry'][i]['yt:videoId']
                video_published = response_parsed['feed']['entry'][i]['published']

                if video_published < published_after:  # if the video is older than 1 day, we don't want it
                    break

                new_body += f"**{name}**: {video_title} #watch?v={video_id}\n"
                i += 1
            except:
                break
    
    if new_body != "":  # there's information to be added
        body += f"**{title}:**\n{new_body}\n"  # extra blank line at the end

    return body


def get_channel_groups_info(channel_groups: dict) -> str:
    """
    Get information from the channels, and form a message with the information.

    Args:
        channel_groups: Dictionary linking the group's title to the group's dictionary.
    
    Returns:
        body: String with the updated body of the email.
    """

    body = ""

    for group_title, channels in channel_groups.items():
        body = get_channel_info(channels, group_title, body)

    return body


if __name__ == '__main__':
    # Fetch CHANNEL_GROUPS from environment variables
    GROUPS = json.loads(os.getenv("CHANNEL_GROUPS", '{}'))  # Default to empty if not set

    body = "**Your Daily Subscription Activity:**\n\n"
    body += get_channel_groups_info(GROUPS)
    
    print(body)