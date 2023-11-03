import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open('config.json') as config_file:
    config = json.load(config_file)

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID', config.get('SPOTIFY_CLIENT_ID', ''))
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET', config.get('SPOTIFY_CLIENT_SECRET', ''))

def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri='http://localhost:8888/callback'
    ))

def get_playlist_tracks(spotify_client, playlist_id):
    playlist = spotify_client.playlist_items(playlist_id)
    return playlist['items']