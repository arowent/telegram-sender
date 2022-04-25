from django import forms
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(label='title', widget=forms.TextInput)
    description = forms.Textarea(label='description', widget=forms.Textarea)
