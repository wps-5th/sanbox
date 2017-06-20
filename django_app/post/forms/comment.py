from django import forms
from django.contrib.auth import get_user_model

from ..models import Comment

User = get_user_model()


class CommentForm(forms.ModelForm):
    # comment = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput,
    # )

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets={
            'content':forms.TextInput(
                attrs={
                    'class':'input-comment',
                    'placeholder':'댓글입력',
                }
            )
        }
        # 수정을 위해 list 로 작성 tuple 인 경우 수정이 불가능하기 때문에

    # def save(self, **kwargs):
    #     commit = kwargs.get('commit', True)
    #     author = kwargs.pop('author', None)
    #
    #     if not self.instance.pk or isinstance(author, User):
    #         self.instance.author = author
    #     instance = super().save(**kwargs)
    #
    #     comment_string = self.cleaned_data['content']
    #     if commit and comment_string:
    #         if instance.my_comment:
    #             instance.my_comment.content = comment_string
    #             instance.my_comment.save()
    #
    #         else:
    #             instance.my_comment = Comment.objects.create(
    #                 comment=instance,
    #                 author=author,
    #                 content=comment_string,
    #             )
    #         instance.save()
    #     return instance
