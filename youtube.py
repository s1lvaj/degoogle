import urllib.request
import time
import json
import os
import smtplib
from email.mime.text import MIMEText
import xmltodict


def get_channel_info(
        channels: dict,
        title: str,
        body: str,
):
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
        # Compute 24h10min ago in RFC3339 format
        published_after = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (24 * 60 * 60) - (10 * 60))
        )
    except Exception as e:
        body += f"{e}"

    new_body = ""
    for name in channels.keys():
        i = 0
        while True:
            try:
                url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channels[name]}"
                data = urllib.request.urlopen(url)
                data_read = data.read().decode('utf-8')
                data_parsed = xmltodict.parse(data_read)
                video_title = data_parsed['feed']['entry'][i]['title']
                video_id = data_parsed['feed']['entry'][i]['yt:videoId']
                video_published = data_parsed['feed']['entry'][i]['published']

                if video_published < published_after:  # if the video is older than 1 day, we don't want it
                    break

                new_body += f"{name}: {video_title}, https://www.youtube.com/watch?v={video_id}\n"
                i += 1
            except:
                break
    
    if new_body != "":  # there's information to be added
        body += f"{title}:\n{new_body}\n"  # extra blank line at the end

    return body


def get_channel_groups_info(channel_groups: dict):
    """
    Get information from the channels, and form a message with the information.

    Args:
        channel_groups: Dictionary linking the group's title to the group's dictionary.
    
    Returns:
        body: String with the updated body of the email.
    """

    body = ""

    for group in channel_groups.keys():
        body = get_channel_info(channel_groups[group], group, body)

    return body


def send_email(
        body: str,
        sender_email: str,
        sender_password: str,
        receiver_email: str,
        ):
    
    """
    Sends an email with the subscription's activity.

    Args:
        body: Body of the email to be sent, with the subscription's name and latest activity.
        sender_email: String with the email of the sender.
        sender_password: String with the password of the sender.
        receiver_email: String with the email of the receiver.
    
    Returns:
        None.
    """
    
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Your YouTube Subscriprion Activity'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    return


if __name__ == '__main__':

    """
    EXAMPLE:

    stem = {
        "3Blue1Brown": "UCYO_jab_esuFRV4b17AJtAw",
        "Aleph 0": "UCzBjutX2PmitNF4avysL-vg",
        "Andrew Dotson": "UCnFmWQbVW_YbqPQZGNuq8sA",
        "Domain of Science": "UCxqAWLTk1CmBvZFPzeZMd9A",
        "Fireship": "UCsBjURrPoezykLs9EqgamOA",
        "Kyle Hill": "UCFbtcTaMFnOAP0pFO1L8hVw",
        "Kurzgesagt": "UCsXVk37bltHxD1rDPwtNM8Q",
        "ScienceClic English": "UCWvq4kcdNI1r1jZKFw9TiUA",
        "Veritasium": "UCHnyfMqiRRG1u-2MsSQLbXA",
        "VSauce": "UC6nSFpj9HTCZ5t-N3Rm3-HA",
        "Zach Star": "UCpCSAcbqs-sjEVfk_hMfY9w",
    }

    other = {
        "": "",
    }

    groups = {'STEM': stem, 'Other Channels': other}
    """

    GROUPS = json.loads(os.getenv("CHANNEL_GROUPS"))  # I'll fetch it directly from my environmental variables, as a json
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    body = get_channel_groups_info(GROUPS)
    send_email(body, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)