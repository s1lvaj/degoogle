# Media Tools

If you don't want to open youtube directly to watch videos, mpv is a great alternative. This is an opensource multimedia player, working for every type of file, and even youtube links. If you use windows, you can install it in https://mpv.io/, or install the `7z` file directly from here: https://github.com/zhongfly/mpv-winbuild/releases

The next step is to extract the files to `C:\Program Files\mpv` and add this to path. To do that:
1. Search for `Edit the system environment variables`.
2. Click `Environment Variables`.
3. Under `System variables`, select `Path` and `Edit`.
4. Add `C:\Program Files\mpv`.
5. Test it by opening the terminal and typing `mpv --version`. If it prints the version, it works.

The only remaining step is to install yt-dlp (mpv uses it to play youtube URLs) by typing `pip install yt-dlp` (it should work by default if you already have python in path). Then, the command `mpv <youtube-link>` should work as intended and play the youtube video.

You can even ditch the entire mpv installation and simply use `yt-dlp <youtube-link>` to download the videos, if you prefer to watch them offline. However, you do need explicit permission from the content creator in order to download their videos.