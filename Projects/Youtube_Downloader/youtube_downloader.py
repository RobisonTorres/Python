from pytube import YouTube
from pytube.cli import on_progress
import sys, subprocess
subprocess.run('cls', shell=True)
print('Youtube Downloader.')
print()

def download():

    # This function downloads youtube videos.
    link = input("Please, type in the videos's url you want to download... ")
    youtube_video = YouTube(link, on_progress_callback=on_progress)
    youtube_video = youtube_video.streams.get_highest_resolution()
    try:
        youtube_video.download(r'C:\Users\Robison Torres\Downloads')  # Chose the directory.
        return 'Download successfully.'
    except: return 'Sorry, something went wrong.'

print(download())