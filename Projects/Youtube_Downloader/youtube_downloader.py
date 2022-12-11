from pytube import YouTube, Playlist
from pytube.cli import on_progress
from pathlib import Path
import sys, subprocess
subprocess.run('cls', shell=True)
print('Youtube Downloader.')
print()

def download():

    # This function downloads youtube videos.
    option = int(input('Press 1 to download Video or Press 2 to download Playlist: '))
    downloads_path = str(Path.home() / "Downloads")
    print()
    directory = (input("Download Location - \n\nType in the directory's path or hit enter to chose the default directory (Downloads):\n ")
                or downloads_path)

    if option == 1:
        print()
        link = input("Type in the videos's url that you want to download:\n ")
        youtube_video = YouTube(link, on_progress_callback=on_progress)
        youtube_video = youtube_video.streams.get_highest_resolution()
        try:
            youtube_video.download(directory)
            return 'Download successfully.'
        except: return 'Sorry, something went wrong.'

    elif option == 2:
        print()
        link = input("Type in the playlist's url that you want to download:\n ")
        playlist = Playlist(link)
        playlist_videos = list(playlist.video_urls)
        try:
            for video in playlist_videos:
                youtube_video = YouTube(video, on_progress_callback=on_progress)
                youtube_video = youtube_video.streams.get_highest_resolution()
                youtube_video.download(directory)
            return 'Download successfully.'
        except: return 'Sorry, something went wrong.'
    
    else:
        return 'Wrong option.'

print(download())
