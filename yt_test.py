import time

print("Hello World for YT Test!!!1!")

published_after = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - (24 * 60 * 60) - (10 * 60))
        )

print(published_after)