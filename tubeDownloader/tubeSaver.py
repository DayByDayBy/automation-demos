from pytube import YouTube, Playlist
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)                  # not necessary, just handy to check it's the expected video
print("Description: ", yt.description)      #likewise, just handy to make sure it's the vid you wanted
yd = yt.streams.get_highest_resolution()    # other options include "get_audio_only", "get_lowest_resolution"
yd.download('downloads')                    # this is what actually downloads the video, places in named folder


# to use, run pytyhon3 tubeDownloader.py <link>