import requests
from django.shortcuts import render

from post.models import Video

__all__ = (
    'youtube_search',
)


def youtube_search(request):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    q = request.GET.get('q')
    video_id = Video.objects.all()
    print(video_id)
    if q:
        search_list_params = {
            'part': 'snippet',
            'maxResults': '10',
            'key': 'AIzaSyCFSwQ62GMdmQBU-C6qtjlC00JuBhnFKcQ',
            'q': q,
            'type': 'video',
        }
        response = requests.get(url_api_search, params=search_list_params)
        # context = {
        #     'response': response.json()
        # }
        for item in response.json()['items']:
            videoid = item['id']['videoId']
            videotitle = item['snippet']['title']
            videothumbnail = item['snippet']['thumbnails']['high']['url']

            Video.objects.update_or_create(
                video_id=videoid,
                q=q,
                video_title=videotitle,
                video_thumbnail=videothumbnail,
            )

            youtube_play = Video.objects.filter(q=q)
            context = {
                'youtube_play': youtube_play,
            }
    else:
        context = {}

    return render(request, 'post/youtube_search.html', context)


