from django import forms

from ..models import Post, Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True

    comment = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )

    class Meta:
        model = Post
        fields = (
            'photo',
            'comment',
        )

    def save(self, **kwargs):
        commit = kwargs.get('commit', True)
        author = kwargs.pop('author', None)
        self.instance.author = author
        instance = super().save(**kwargs)
        # if commit and not (author and author.pk):
        #     raise ValueError(
        #         'author is require field'
        #     )
        # if commit:
            # instance.author = author
        comment_string = self.cleaned_data['comment']
        # if commit and comment_string:

        if commit and comment_string:
            if instance.my_comment:
                instance.my_comment.content = comment_string
                instance.my_comment.save()
            else:
                instance.my_comment = Comment.objects.get_or_create(
                    post=instance,
                    author=author,
                    defualt={'content':comment_string}
                )
                # if not comment_created:
                #     instance.comment_set.create(
                #         author=instance.author,
                #         content=comment_string,
                #     )

        return instance
