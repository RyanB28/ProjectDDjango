from django import forms
from .models import Comment
from .models import Post


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'categorie']