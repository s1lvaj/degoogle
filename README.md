# Why degoogle your life?

Take control of your software. There are opensource alternatives.

Tech is supposed to be a helpful tool, also allowing us to consume content, but always as a means to

Information to degoogle and have more control over your tech.

This is not about "having something to hide", it's about the right to privacy.

## 1. Browser and Search Engine

Don't use Google Chrome or Edge. Firefox is a great alternative, as well as Brave. An adblocker is also crucial. Navigating the internet without an adblocker is like crossing the street without looking to both sides. Ads are mostly malware, so you need to be safe.

Then go to your browser settings and change the default search engine to something like duckduckgo, instead of google.

Some 5 minutes are enough to do this.

## 2. VPN

A Virtual Private Network (VPN) is crucial when navigating the internet. Choose a safe one and use it.

## 3. Email

Now we get to the difficult and tedious part, specially if your email is old and has a lot of necessary services linked to it, like government and madical services. Changing from your gmail can be quite difficult, and for these two examples given, maybe seeing your email as a "necessary evil" can be the most sane solution.

Protonmail is a good alternative to google when it comes to email.

## 4. Calendar and Cloud Storage

Protonmail can also be a solution when it comes to calendar and cloud storage (however, for projects, creating an opensource github repository can be better to save storage).

## 5. Maps

Very hard to replace. Apple Maps is safer than Google Maps. But opensource alternatives can also be good to look at.

## 6. Phone

Your phone's operating system is design to distract you, to notify you of things that don't matter, and to make you the product. Changing your operating system to something like GrapheneOS can make you take control of it once again.

Apps don't run and see what you do on the background, you can choose what they have access to (even if they have access to the internet or not), you can create different profiles with different apps, etc. Using apps now feels intentional.

## 7. Content

You can get content from youtube channels, and even news articles, by using their RSS feeds.

For instance, on youtube, have account turned off. The script in this repository can be used for this.

For other news/content, the same can be made.

With time, you'll see u dont care about some of the channels. This is not to pass the idea of "phone bad", but "being overwhelmed and with no autonomy is bad". Content is great, but you need to be able to clearly choose what you want to see. And after a quarter of a life consuming a lot of content, maybe clearly controling it is the best. Again, technology is supposed to help you out, not consider your life and attention as a market niche to be explored.

```javascript Sending Email
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
```