from django import forms
from .models import *
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class SignUp(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
