import requests


def search(q):
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
