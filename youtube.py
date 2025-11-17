import urllib.request
import json
import time
import smtplib
from email.mime.text import MIMEText

"""
1. You only get news from your subscriptions, not youtube trying to recommend you stuff, and organized in sections that YOU create.
2. Having no youtube account and no cookies on the website makes the search function more useful and you get more variety of recommendations.
"""

def get_channel_info(
        api_key: str,
        channels: dict,
        title: str,
        body: str,
):
    """
    Get information from the channels, and form a message to be sent.

    Args:
        api_key: String with the API key of the account which will access youtube's information.
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
        try:
            url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channels[name]}"
            response = ...
            video_title = ...
            new_body += f"{name}: {video_title}\n"
        except:
            pass
    
    if new_body != "":  # there's information to be added
        body += f"{title}:\n{new_body}\n"  # extra blank line at the end

    print("Done " + title)

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

    SENDER_EMAIL = ""
    SENDER_PASSWORD = ""
    RECEIVER_EMAIL = ""

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

    body = "\
        *---------------------*\n\
        *YOUTUBE SUBSCRIPTIONS*\n\
        *---------------------*"
    
    body = get_channel_info(API_KEY, stem, 'STEM', body)
    # body = get_channel_info(API_KEY, other, 'Other Stuff', body)
    send_email(body, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)