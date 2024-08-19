# -*- coding: utf-8 -*-
"""
Youtube to Mp3 converter
"""

import os
import yt_dlp

def download_audio():
    url = input("Enter the URL of the video you want to download: \n>> ")
    destination = input("Enter the destination (leave blank for current directory): \n>> ") or '.'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    download_audio()
