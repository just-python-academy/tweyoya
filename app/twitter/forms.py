from django import forms
from django.db import models

from .models import Tweet


class TweetForm(forms.ModelForm):

    class Meta:

        model = Tweet
        fields = ('tweeted_at', 'text', 'img')
