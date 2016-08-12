from  django import forms

from .models import Post


class PostCreatedForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_time']

