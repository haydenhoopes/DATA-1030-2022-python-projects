from __future__ import unicode_literals
import youtube_dl
from urllib.error import HTTPError
print("Insert the link")
songs_to_download = []
done = False

while not done:
    inp = input("Paste the link to a song: ")
    if inp == "":
        done = True
    else:
        songs_to_download.append(inp)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '300',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for link in songs_to_download:
        try:
            ydl.download([link])
        except HTTPError:
            pass