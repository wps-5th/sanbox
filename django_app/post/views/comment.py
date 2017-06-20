from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from ..forms import CommentForm
from ..models import Post

__all__ = (
    'comment_create',
    'comment_modify',
    'comment_delete',
)


@require_POST
@login_required
def comment_create(request, post_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    # CommentForm을 만들어서 해당 ModelForm안에서 생성/수정가능하도록 사용
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    next = request.GET.get('next')
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        form.save()
    else:
        messages.error(request, form.errors)
    if next:
        return redirect(next)
    return redirect('post:post_detail', post_pk=post.pk)


# @require_POST
# @login_required
def comment_modify(request, post_pk):
    pass


#     comment = Comment.objects.get(pk=post_pk)
#     post=get_object_or_404(Post, pk=post_pk)
#     # if request.method == 'POST':
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('post:post_detail', post_pk=post.pk)
#         # comment 의 경우 POST 경우에만 작동 GET 에 대해서 아무 작동도 하지 않는다
#     # else:
#     #     form = CommentForm(instance=comment)
#     # context = {
#     #     'form': form,
#     # }
#     # return render(request, 'post/post_modify.html', context)


def comment_delete(request, post_pk, comment_pk):
    # # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    # post = get_object_or_404(Comment, pk=post_pk)
    # if request.method == 'POST':
    #     post.delete()
    #     return redirect('post:post_list')
    # else:
    #     context = {
    #         'post': post
    #     }
    #     return render(request, 'post/post_delete.html', context)
    pass
