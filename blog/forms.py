from django import forms
from .models import Comment
from .models import Post
from .models import Belangrijkbericht


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'categorie']

class ImportantForm(forms.ModelForm):
    class Meta:
        model = Belangrijkbericht
        fields = ['content', 'categorie']
