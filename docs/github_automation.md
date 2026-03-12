# Github Automation

This repository has GitHub Actions running daily scripts to gather YouTube videos and recent news, sending them to me using a personalized discord bot (but it can also easily be made with telegram, slack, etc.).

To use the automation workflow, the following secrets must be defined in your repository:

- `CHANNEL_GROUPS`: YouTube creators you want to follow, as indicated in `examples/CHANNEL_GROUPS.json`.
- `RSS_NEWS_WEBSITES`: News websites you want to follow, as indicated in `examples/RSS_NEWS_WEBSITES.json`.
- `DISCORD_BOT_TOKEN`: Token for your discord bot (if you want the output to be sent to you over discord).
- `DISCORD_USER_ID`: Your discord user-id (if you want the output to be sent to you over discord).

These should be added in:

Repository Settings → Secrets → Actions

If you wanted to include in your script the function to directly send you an email using a gmail account, that would also be possible with the script below. But since this is a degoogle repository, that option will not be used.

```python Sending Email
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
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    return
```