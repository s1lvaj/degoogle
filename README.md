# Why degoogle your life?

This repository serves as a guide to degoogle your life. This act serves to take control of your software, choosing better (and sometime opensource) alternatives. Technology is supposed to be a helpful tool, also allowing us to consume content, but always as a means to serve and enrich our lives, NEVER in order overwhelm us and consider our life and attention as a market niche to be explored.

## 1. Browser and Search Engine

Don't use Google Chrome or Edge. Firefox is a great alternative, as well as Brave. An adblocker is also crucial. Navigating the internet without an adblocker is like crossing the street without looking to both sides. Ads are mostly malware, so you need to be safe.

Then go to your browser settings and change the default search engine to something like duckduckgo, instead of google. It can also help to tell your browser to delete all your cookies, history and data every time you close it.

Some 5 minutes are enough to do this.

## 2. VPN

A Virtual Private Network (VPN) is crucial when navigating the internet. Choose a safe one and use it.

## 3. Email

Now we get to the difficult and tedious part, specially if your email is old and has a lot of necessary services linked to it, like government and madical services. Changing from your gmail can be quite difficult, and for these two examples given, maybe seeing your email as a "necessary evil" can be the most sane solution.

Protonmail is a good alternative to google when it comes to email.

## 4. Calendar and Cloud Storage

Protonmail can also be a solution when it comes to calendar and cloud storage (however, for projects, creating an opensource github repository can be better, as long as you don't share anything too personal).

## 5. Maps

Very hard to replace. Apple Maps is safer than Google Maps. But opensource alternatives can also be good to look at.

## 6. Content

You can get content from youtube channels, and even news articles, by using their RSS feeds.

For instance, on youtube, have account turned off. The script in this repository can be used for this.

For other news/content, the same can be made.

With time, you'll see u dont care about some of the channels.

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

## 7. MPV on Windows

If you don't wanna open youtube directly to watch the videos, mpv is a great alternative: https://mpv.io/installation/

This is an opensource multimedia player, working for every type of file, and even youtube links. If you use windows, you can use the link above, or install the `7z` file directly from here: https://github.com/zhongfly/mpv-winbuild/releases

The next step is to extract the files to `C:\Program Files\mpv` and add this to path. To do that:
1. Search for `Edit the system environment variables`.
2. Click `Environment Variables`.
3. Under `System variables`, select `Path` and `Edit`.
4. Add `C:\Program Files\mpv`.
5. Test it by opening the terminal and typing `mpv --version`. If it prints the version, it works.

The only remaining step is to install yt-dlp (mpv uses it to play youtube urls) by typing `pip install yt-dlp` (it should work by default if you already have python in path). Then, the command `mpv <youtube-link>` should work as intended. It is also possible to record the video with `mpv --stream-record=video.mkv`, although this feature is experimental and may break. The command manual can be seen here: https://mpv.io/manual/stable/

## 8. Operating Systems

A final step would be to even ditch windows for linux. This isn't really related to google, but to privacy more in general. Linux ricing and choosing a distribution can also be quite fun, but it requires a lot of work and willingness to learn. However, it will give you much more control over your technology.

Regarding your phone, its operating system is design to distract you, to notify you of things that don't matter, and to make you the product. Changing your operating system to something like GrapheneOS can make you take control of it once again. Apps don't run and see what you do on the background, you can choose what they have access to (even if they have access to the internet or not), you can create different profiles with different apps, etc. Using apps now feels intentional.

## 9. Next Steps

If all of these steps have been completed, you are already way better when it comes to online privacy. Some next steps would be to limit social media usage. While ditching it is not needed, for it can be quite fun to share advetures with friends, it shouldn't define your life, and you should also pay attention to what you post. Do NOT share your entire life, specially with people you do not know. Use different names or personas when possible. Know how to identify scams.

Using apps like signal to commnicate, instead of whatsapp, could also be good, but it isn't critical, like using Tor as your default browser, encrypting all your email and information, only using cash to pay for things, etc. It can be overkill unless you are an activist.

And not really regarding pc/phone stuff, it is crucial that you buy products that you can own. Buying a futuristic car can be fun, but if it can be hacked, locks you in for software updates, or locks functions behind a subscription, is it really worth it? You deserve to not watch an ad every time you reach a red light. Research before investing into it.