# Degoogle

This repository serves as a guide to degoogle your life. This act serves to take control of your software, choosing better (and sometimes opensource) alternatives, making technology a better tool, instead of a simple time sink.

This repository combines:

- A structured degoogling guide.
- Useful automation scripts.
- GitHub Actions workflows for privacy-friendly automation.

## Project Structure

```bash
degoogle/
├── .github/workflows/     # Automation via GitHub Actions
├── docs/                  # Extra Documentation/Guides for Scripts and Automation
├── examples/              # Examples of json files
├── scripts/               # Python tools (RSS, YouTube, etc.)
├── LICENSE                # MIT License
├── README.md              # Degoogling Guide
└── requirements.txt       # External libraries to be installed with Python
```

## Degoogle Techniques

1. **Browser and Search Engine**

    Don't use Google Chrome or Microsoft Edge. Firefox is a great alternative, as well as Brave. And be sure you have an adblocker with it, so that you don't have malicious content preying on you.

    Then go to your browser settings and change the default search engine to something like duckduckgo, instead of google. It can also be helpful to setup your browser to delete all your cookies, history and data every time you close it.

    Some 5 minutes are enough to do this.

2. **VPN**

    A Virtual Private Network (VPN) is crucial when navigating the internet. Choose a reputable one and use it.

3. **Email**

    Now we get to the difficult and tedious part, the email. Specially if it is old and has a lot of necessary services linked to it, like government and medical services. Changing from your gmail can be quite difficult, and for these two examples given, keeping your email can be the most sane solution.

    But if you want the challenge, protonmail is a good alternative to google when it comes to email. Changing your other services first is the best solution, keeping track of what you actually use, and having your gmail forwarding all other stuff, while you still get used to proton.

4. **Calendar and Cloud Storage**

    Protonmail can also be a solution when it comes to calendar and cloud storage (however, for projects, creating an opensource github repository can be better, as long as you don't share anything too personal). For family photos and alike, moving them from a format like .png to a modern one like .avif can also help, and a tool to do that can be accessed in the folder `scripts/resources`.

5. **Maps**

    Google Maps is very hard to replace. Apple Maps is safer than Google Maps, but opensource alternatives can also be good to look at. Open Street Maps (OSM) is a great collaborative map alternative.

    For Android, OSMAnd or Organic Maps are great tools, letting you download maps in advance, so that you don't have roaming problems. It can also be useful to slowly get used at looking at offline maps, to be able to locate yourself physically.

6. **Mobile Phone**

    Regarding your phone, changing your operating system to something like GrapheneOS (in the case of pixel phones), CalyxOS, LineageOS, etc. can make you take control of it once again.

    If you're using Android, you can opt out from the Play Store. Install F-Droid (for free and opensource applications) and there you can install Aurora Store, to access the Play Store without a google account. You can also install all of these directly from the APK, but F-Droid allows for an easier management.

    After that, you may use to install what we discussed above, such as a good browser and search engine, VPN, protonmail and its other services (if you decided to use those), maps alternative, and whatever other applications you want.

## How to Use the Scripts (Optional)

This repository includes automation tools. The requirements are as follows:
- Python 3.10+
- Dependencies listed in `requirements.txt`

Install:

```bash
pip install -r requirements.txt
```

Run a script:

```bash
python scripts/youtube.py
```

See `docs/...` for configuration details and automation via GitHub Actions.