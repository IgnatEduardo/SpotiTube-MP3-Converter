from flask import Flask, render_template, request, send_file
import os
from pytube import YouTube
from download_util import download_mp3
from spotify_util import authenticate_spotify, get_playlist_tracks
from youtube_util import search_youtube

app = Flask(__name__)

def sanitize_filename(title):
    # Replace spaces and special characters with underscores
    return ''.join(c if c.isalnum() or c in '._-' else '_' for c in title)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    playlist_url = request.form['playlist_url']
    #check the playlist url is the correct format https://open.spotify.com/playlist/yourplaylistid
    playlist_url = playlist_url.split('playlist/')[1]
    playlist_url = playlist_url.split('?')[0]
    download_path = 'converted_tracks'  # Set your download directory

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    spotify_client = authenticate_spotify()
    playlist_tracks = get_playlist_tracks(spotify_client, playlist_url)

    for track in playlist_tracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        search_query = f"{track_name} {artist_name} official audio"

        youtube_urls = []

        try:
            youtube_url = search_youtube(search_query)
            if youtube_url:
                youtube_urls.append(youtube_url)
            else:
                print(f"Video not found for query: {search_query}")
        except Exception as e:
            print(f"An error occurred while searching for '{search_query}': {e}")

        for youtube_url in youtube_urls:
            download_mp3(youtube_url, download_path)
    return render_template('convert.html')

if __name__ == "__main__":
    app.run()