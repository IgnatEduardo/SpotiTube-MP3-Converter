from googleapiclient.discovery import build
import json
import os

with open('config.json') as config_file:
    config = json.load(config_file)

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', config.get('YOUTUBE_API_KEY', ''))

def search_youtube(query):
    youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=1
    ).execute()
    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    return None
