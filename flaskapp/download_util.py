from pytube import YouTube

def download_mp3(youtube_url, download_path):
    yt_video = YouTube(youtube_url)
    stream = yt_video.streams.filter(only_audio=True).first()
    stream.download(output_path=download_path)
