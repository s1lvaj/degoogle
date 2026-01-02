import subprocess
import time

def main(video, retry_interval=10, max_retries=500):

    if 'youtube' or 'youtu.be' in video:
        command = 'yt-dlp.exe ' + video
    elif 'watch?v=' in video:
        command = 'yt-dlp.exe youtube.com/' + video
    else:
        command = 'yt-dlp.exe youtube.com/watch?v=' + video

    count = 0

    while count < max_retries:
        count += 1
        print(f"Running: {command}")

        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

            error_flag = False
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    # while the command is still running, process.poll() returns None
                    break
                if output:
                    print(output.strip())
                if 'ERROR' in output.upper():
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

    videos = ['...']

    for video in videos:
        main(video)
