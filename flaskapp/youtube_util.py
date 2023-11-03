from googleapiclient.discovery import build

def search_youtube(youtube_api_key, query):
    youtube = build('youtube', 'v3', developerKey = youtube_api_key)
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
