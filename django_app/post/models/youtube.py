from django.db import models

__all__ = (
    'Video',
    # 'Video_ori',
    'VideoManager',
)


class VideoManager(models.Manager):
    def created_from_search_result(self, result):
        """
        :param result: YouTube Search API 사용 후 , 검색
        :return: Video object
        """
        youtube_id = result['id']['videoId']
        title = result['snippet']['title']
        description = result['snippet']['description']
        url_thumbnail = result['snippet']['thumbnails']['high']['url']

        video, video_created = Video.objects.get_or_create(
            youtube_id=youtube_id,
            defaults={
                'title': title,
                'description': description,
                'url_thumbnail': url_thumbnail,
            }
        )
        print('Video({})is {}'.format(
            video.title,
            'created' if video_created else 'already exists',
        ))
        return video


class Video(models.Model):
    youtube_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url_thumbnail = models.CharField(max_length=50)

    objects = VideoManager()

    def __str__(self):
        return self.title

#
# class Video(models.Model):
#     video_id = models.CharField(max_length=50)
#     video_title = models.CharField(max_length=50)
#     video_thumbnail = models.ImageField(upload_to='thumbnail', blank=True)
#
#     objects = VideoManager()
#
#     def __str__(self):
#         return self.video_id
#
#
