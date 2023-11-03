from pytube import YouTube
import os

def download_mp3(youtube_url, download_path):
    yt_video = YouTube(youtube_url)
    stream = yt_video.streams.filter(only_audio=True).first()
    mp3_file_path = os.path.join(download_path, f'{yt_video.title}.mp3')
    stream.download(output_path=download_path, filename=yt_video.title)
    return mp3_file_path
