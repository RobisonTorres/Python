from pytube import YouTube, Playlist
from pytube.cli import on_progress
import sys, subprocess
subprocess.run('cls', shell=True)
print('Youtube Downloader.')
print()

def download():

    # This function downloads youtube videos.

    option = int(input('Press 1 for Video or Press 2 for Playlist: '))
    directory = (input(r"Type in the directory's path or hit enter to save it on default directory (Downloads): ")
                or r'C:\Users\Robison Torres\Downloads')

    if option == 1:
        link = input("Type in the videos's url you want to download: ")
        youtube_video = YouTube(link, on_progress_callback=on_progress)
        youtube_video = youtube_video.streams.get_highest_resolution()
        try:
            youtube_video.download(directory)
            return 'Download successfully.'
        except: return 'Sorry, something went wrong.'

    elif option == 2:
        link = input("Type in the playlist's url you want to download... ")
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
