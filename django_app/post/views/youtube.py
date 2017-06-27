import re

import requests
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from utils import youtube
from ..models import Video, Post, Comment

__all__ = (
    'youtube_search',
    'post_create_with_video',
)


def youtube_search(request):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    q = request.GET.get('q')
    # video_id = Video.objects.all()
    video_em = []
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
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_thumbnail = item['snippet']['thumbnails']['medium']['url']

            p = re.compile(r'.*\.([^?]+)')
            file_ext = re.search(p, video_thumbnail).group(1)
            file_name = '{}.{}'.format(
                item['id']['videoId'],
                file_ext,
            )

            temp_file = NamedTemporaryFile()

            response = requests.get(video_thumbnail)
            temp_file.write(response.content)

            video_list, video_created = Video.objects.get_or_create(
                video_id=video_id,
                video_title=video_title,
                # video_thumbnail=video_thumbnail,
            )

            video_list.video_thumbnail.save(file_name, File(temp_file))
            video_em.append(video_list)
            # youtube_q = video_list.objects.filter(q=q)

            context = {
                'youtube_keyword': video_em,
            }

    else:
        context = {}

    return render(request, 'post/youtube_search.html', context)


def youtube_search_ori(request):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    q = request.GET.get('q')

    if q:
        search_list_params = {
            'part': 'snippet',
            'maxResults': '10',
            'key': 'AIzaSyCFSwQ62GMdmQBU-C6qtjlC00JuBhnFKcQ',
            'q': q,
            'type': 'video',
        }
        response = requests.get(url_api_search, params=search_list_params)
        data = response.json()

        for item in data['item']:
            pass

        # videos = Video.objects.filter(title__contains=q)
        # videos = Video.objects.filter(Q(title__contains=q)|Q(description__contains=q))
        # videos = Video.objects.all()
        # for cur_q in q.split(''):
        #     videos.filter(title__contains=cur_q)
        # # regex 사용법
        # # and 연산
        # re_pattern = ''.join(['(?=.*{})'.format(item) for item in q.split()])
        # # or 연산
        # # re_pattern = '|'.join(['(?=.*{})'.format(item) for item in q.split()])
        # videos = Video.objects.filter(title__regex=r'{}'.format(re_pattern))
        # # Video.objects.filter(title__regex=r'')
        # # videos.filter(title__contains='fastcampus').filter(title__contains='web').filter(title__contains='programing')
        #
        #
        # # title 과 description
        # # videos = Video.objects.filter(
        # #   Q()

        # context={
        #     'videos':videos,
        #     'response':response.json(),
        # }

        context = {}

        return render(request, context=context)


def youtube_search(request, q=None):
    context = dict()
    q = request.GET.get('q')
    if q:
        data = youtube.search(q)

        for item in data['item']:
            Video.objects.create_from_search_result(item)
        re_pattern = ''.join(['(?=.*{}'.format(item) for item in q.split()])
        videos = Video.objects.filter(
            Q(title_regex=re_pattern) |
            Q(description__regex=re_pattern)
        )
        context['videos'] = videos
    return render(request, 'post/youtube_search.html', context)


@login_required
@require_POST
def post_create_with_video(request):
    video_pk = request.POST['video_pk']
    video = get_object_or_404(Video, pk=video_pk)

    post = Post.objects.create(
        author=request.user,
        video=video,
    )
    post.my_comment = Comment.objects.create(
        author=request.user,
        content=video.title,
    )

    return redirect('post:post_detail')
