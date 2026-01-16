# Why to degoogle your life?

This repository serves as a guide to degoogle your life. This act serves to take control of your software, choosing better (and sometimes opensource) alternatives, making technology a better tool, instead of a simple time sink.

## 1. Browser and Search Engine

Don't use Google Chrome or Microsoft Edge. Firefox is a great alternative, as well as Brave. And be sure you have an adblocker with it, so that you don't have malicious content preying on you.

Then go to your browser settings and change the default search engine to something like duckduckgo, instead of google. It can also be helpful to setup your browser to delete all your cookies, history and data every time you close it.

Some 5 minutes are enough to do this.

## 2. VPN

A Virtual Private Network (VPN) is crucial when navigating the internet. Choose a safe one and use it.

## 3. Email

Now we get to the difficult and tedious part, the email. Specially if it is old and has a lot of necessary services linked to it, like government and medical services. Changing from your gmail can be quite difficult, and for these two examples given, keeping your email can be the most sane solution.

But if you want the challenge, protonmail is a good alternative to google when it comes to email. Changing your other services first is the best solution, keeping track of what you actually use, and having your gmail forwarding all other stuff, while you still get used to proton.

## 4. Calendar and Cloud Storage

Protonmail can also be a solution when it comes to calendar and cloud storage (however, for projects, creating an opensource github repository can be better, as long as you don't share anything too personal). For family photos and alike, moving them from a format like .png to a modern one like .avif can also help, and a tool to do that can be accessed in the folder `resources`.

## 5. Maps

Google Maps is very hard to replace. Apple Maps is safer than Google Maps, but opensource alternatives can also be good to look at. Open Street Maps (OSM) is a great collaborative map alternative.

## 6. Mobile Phone

Regarding your phone, changing your operating system to something like GrapheneOS (in the case of pixel phones), CalyxOS, LineageOS, etc. can make you take control of it once again.

If you're using Android, you can opt out from the Play Store. Install F-Droid (for free and opensource applications) and there you can install Aurora Store, to access the Play Store without a google account. You can also install all of these directly from the APK, but F-Droid allows for an easier management.

After that, you may use to install what we discussed above:
- Good browser with good default search engine.
- A VPN service.
- Protonmail, calendar and drive (if you decided to use those).
- Maps alternative. For Android, OSMAnd or Organic Maps are great tools, letting you download maps in advance, so that you don't have roaming problems. It can also be useful to slowly get used at looking at offline maps, to be able to locate yourself physically.
- And then whatever other application you want...

## 7. Content Feeds

You can get content from youtube channels, and even news articles, by using their RSS feeds. The scripts in this repository can be used for that. This way, you can even navigate youtube with your account turned off. For other news and content, the same can be made.

This repository has github actions running daily scripts to gather the recent news and publications from some online content, and sending them using a personalized discord bot (but it can also easily be made with telegram, slack, etc.).

Below is an example of a `CHANNEL_GROUPS` json for you to run the youtube code.

```json
{
  "Science": {
    "3Blue1Brown": "UCYO_jab_esuFRV4b17AJtAw",
    "Veritasium": "UCHnyfMqiRRG1u-2MsSQLbXA",
    "VSauce": "UC6nSFpj9HTCZ5t-N3Rm3-HA"
  },
  "Tech": {
    "Fireship": "UCsBjURrPoezykLs9EqgamOA"
  }
}
```

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

## 8. Watching Content

If you don't want to open youtube directly to watch videos, mpv is a great alternative. This is an opensource multimedia player, working for every type of file, and even youtube links. If you use windows, you can install it in https://mpv.io/, or install the `7z` file directly from here: https://github.com/zhongfly/mpv-winbuild/releases

The next step is to extract the files to `C:\Program Files\mpv` and add this to path. To do that:
1. Search for `Edit the system environment variables`.
2. Click `Environment Variables`.
3. Under `System variables`, select `Path` and `Edit`.
4. Add `C:\Program Files\mpv`.
5. Test it by opening the terminal and typing `mpv --version`. If it prints the version, it works.

The only remaining step is to install yt-dlp (mpv uses it to play youtube URLs) by typing `pip install yt-dlp` (it should work by default if you already have python in path). Then, the command `mpv <youtube-link>` should work as intended and play the youtube video. You can also use `yt-dlp <youtube-link>` to download it directly, and there is a script in the folder `resources` to help you with that. You can even ditch the entire mpv installation and simply use yt-dlp to download the videos, if you prefer to watch them offline.

## 9. Next Steps

A final step would be to even ditch windows for linux. This isn't really related to google, but to privacy more in general. Changing to linux requires a lot of work and willingness to learn; however, it will give you much more control over your technology.

Some next steps would be to limit social media usage, or even ditching or deleting most of them. Using apps like signal to commnicate, instead of whatsapp, could also be good, but it isn't critical, like using Tor as your default browser, encrypting all your emails and information, only using cash to pay for things (or, if buying online, using a one-time phone number/email and a one-time card), using alias when creating accounts, turning off your internet when not using it, keep in touch with tech news, and even change to better options if they appear. However, this can be overkill unless you are an activist or paranoid, and it's not the goal of this repository.

If all of the steps 1-8 have been completed, you are already way better when it comes to online privacy, and even if just some of the steps are followed. With this, we hope to have motivated even more to make sure you own your software, and that looking through and contributing to opensource alternatives can be quite useful.
