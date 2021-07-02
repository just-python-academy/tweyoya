from django.contrib import auth
import tweepy
from django.utils import timezone
from django.conf import settings

from .models import Tweet


def get_oauth_handler():
    consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
    cosumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
    auth = tweepy.OAuthHandler(consumer_key, cosumer_secret)
    return auth

def get_api(auth):
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_TOKEN_SECRET
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def send_tweets():
    expired_tweets = Tweet.objects.filter(
        is_sent=False,
        is_deleted=False,
        tweeted_at__lte=timezone.now()
    )
    auth = get_oauth_handler()
    api = get_api(auth)
    for tweet in expired_tweets:
        if tweet.img:
            file = settings.BASE_DIR / 'media' / str(tweet.img)
            api.update_with_media(filename=file, status=tweet.text)
        else:
            api.update_status(tweet.text)
        tweet.is_sent = True
        tweet.save()