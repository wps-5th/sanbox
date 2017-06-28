import requests
from googleapiclient.discovery import build


def search_original(q):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    search_list_params = {
        'part': 'snippet',
        'maxResults': '10',
        'key': 'AIzaSyCFSwQ62GMdmQBU-C6qtjlC00JuBhnFKcQ',
        'q': q,
        'type': 'video',
    }
    response = requests.get(url_api_search, params=search_list_params).json()

    return response


DEVELOPER_KEY = "AIzaSyCFSwQ62GMdmQBU-C6qtjlC00JuBhnFKcQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def search(q):
    pass
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        part="id,snippet",
        maxResults=10,
        type='video',
    ).execute()
    return search_response
