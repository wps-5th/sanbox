from django.conf.urls import url
from . import views

# URL Namespace
# https://docs.djangoproject.com/en/1.11/topics/http/urls/#url-namespaces
app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),

    # post_create와 매칭
    url(r'^create/$', views.post_create, name='post_create'),

    # post_modify와 매칭
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify'),

    # post_delete와 매칭
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    # post_like와 매칭
    url(r'^(?P<post_pk>\d+)/like-toggle/$', views.post_like_toggle, name='post_like_toggle'),

    # comment_create와 매칭
    url(r'^(?P<post_pk>\d+)/comment/create/$', views.comment_create, name='comment_create'),

    # comment_modify와 매칭
    url(r'^comment/(?P<comment_pk>\d+)/modify/$', views.comment_modify, name='comment_modify'),

    # comment_delete와 매칭
    url(r'^comment/(?P<comment_pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

    # hashtag_post_list와 매칭
    url(r'^tag/(?P<tag_name>\w+)/$', views.hashtag_post_list, name='hashtag_post_list'),

    # 위쪽의 결과들과 매칭되지 않을 경우
    # url(r'^.*/$', views.post_anyway, name='post_anyway'),
]
