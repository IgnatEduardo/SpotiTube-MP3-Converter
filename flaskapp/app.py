from flask import Flask, render_template, request, send_file
import os
import json
from download_util import download_mp3
from spotify_util import authenticate_spotify, get_playlist_tracks
from youtube_util import search_youtube

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', config.get('YOUTUBE_API_KEY', ''))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    playlist_id = request.form['playlist_id']
    download_path = 'downloads'  # Set your download directory
    youtube_api_key = YOUTUBE_API_KEY

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    spotify_client = authenticate_spotify()
    playlist_tracks = get_playlist_tracks(spotify_client, playlist_id)

    mp3_files = []

    for track in playlist_tracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        search_query = f"{track_name} {artist_name} official audio"

        try:
            youtube_url = search_youtube(youtube_api_key, search_query)
            if youtube_url:
                mp3_file_path = download_mp3(youtube_url, download_path)
                mp3_files.append(mp3_file_path)
            else:
                print(f"Video not found for query: {search_query}")
        except Exception as e:
            print(f"An error occurred while searching for '{search_query}': {e}")

    if mp3_files:
        zip_file_path = os.path.join(download_path, 'downloaded_mp3.zip')
        # Compress the downloaded MP3 files into a ZIP archive
        import shutil
        shutil.make_archive(zip_file_path[:-4], 'zip', download_path)

        # Return the ZIP file as an attachment
        return send_file(zip_file_path, as_attachment=True)

    return "No MP3 files downloaded."

if __name__ == "__main__":
    app.run()