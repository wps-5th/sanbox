import requests
from django.shortcuts import render


def youtube_search(request):
    url_youtube_list = 'https://www.googleapis.com/youtube/v3/search'
    q = request.GET.get('q')
    if q:
        url_youtube_params={
            'key':'AIzaSyCFSwQ62GMdmQBU-C6qtjlC00JuBhnFKcQ',
            'q':q,
            'part':'snippet',
            'maxResults':10,
            'type':'video'
        }
        response = requests.get(url_youtube_list, params=url_youtube_params)
        context={
            'response':response.json(),
        }
    else:
        context={

        }


    return render(request, 'post/youtube.html', context)
