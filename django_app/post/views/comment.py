from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from post.decorators import post_owner
from post.forms.comment import CommentForm
from post.models import Post, Comment


__all__=(
    'comment_create',
    'comment_modify',
    'comment_delete',
)


@post_owner
@login_required
def comment_create(request, post_pk):
    # content = Comment.objects.get(pk=post_pk)
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            # ModelForm의 save()메서드를 사용해서 Post객체를 가져옴
            # post = form.save(content=request.POST)
            comment = form.save(commit=False)
            form.save()
            return redirect('post:post_detail', post_pk=post.pk)
    # else:
    #     # post/post_create.html을 render해서 리턴
    #     form = CommentForm()
    # context = {
    #     'content': form,
    # }
    # return render(request, 'post/post_list.html', context)


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
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    post = get_object_or_404(Comment, pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post:post_list')
    else:
        context = {
            'post': post
        }
        return render(request, 'post/post_delete.html', context)

