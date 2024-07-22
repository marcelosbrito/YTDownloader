import yt_dlp # type: ignore
from sys import argv

link = argv[1]

ydl_opts = {
    'format': 'best',
    'outtmpl': 'D:/Marcelo/Downloads/%(title)s.%(ext)s'  # Update with your desired download path
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])  # Replace with any valid YouTube URL

