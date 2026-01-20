import subprocess
import time
import os

def download(video, retry_interval=10, max_retries=500, location=None, subtitles=False):

    """
    Download youtube video.
    
    :param video: String of the video's URL or ID.
    :param retry_interval: Integer of seconds between each download attempt, in the case of failure.
    :param max_retries: Integer of macimum number of download attempts.
    :param location: Path where the download will be saved.
    :param subtitles: Bool to download subtitles or not.
    """

    command = 'yt-dlp.exe '
    if subtitles:
        command += '--write-subs --sub-lang en --embed-subs '

    if ('youtube' in video) or ('youtu.be' in video):
        command += video
    elif 'watch?v=' in video:
        command += 'youtube.com/' + video
    else:
        command += 'youtube.com/watch?v=' + video

    count = 0

    while count < max_retries:
        count += 1
        print(f"Running: {command}")

        try:

            if location is not None:
                os.chdir(location)  # Change the working directory
            
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

            error_flag = False
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    # while the command is still running, process.poll() returns None
                    break
                if output:
                    print(output.strip())
                if 'ERROR: ' in output:
                    error_flag = True

            # Check for the presence of "ERROR" in the output
            if error_flag:
                print(f'"ERROR" detected in output. Retrying in {retry_interval} seconds (attempt {count} of {max_retries})...')
                time.sleep(retry_interval)
            else:
                print("Command succeeded.")
                return 0
            
        except Exception as e:
            # If there's an error, print it out
            print(e)
            print(f'And error has occurred. Retrying in {retry_interval} seconds (attempt {count} of {max_retries})...')
            time.sleep(retry_interval)

    print(f"Command failed after {max_retries} attempts.")
    return 1


if __name__ == "__main__":

    DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    INPUT_FILE = os.path.join(DESKTOP, 'videos.txt')

    VIDEOS = []  # get the video list from a .txt file in the desktop
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            VIDEOS.append(line.replace('\n', ''))

    for video in VIDEOS:
        download(video, location=DESKTOP, subtitles=False)
