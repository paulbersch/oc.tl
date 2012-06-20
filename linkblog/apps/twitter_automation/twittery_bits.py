import os, sys

sys.path.insert(0, '/mnt/web/oc.tl.django/linkblog/linkblog/')
sys.path.insert(0, '/mnt/web/oc.tl.django/linkblog/linkblog/' + '/apps/')
sys.path.insert(0, '/mnt/web/oc.tl.django/linkblog/linkblog/' + '/../')
sys.path.insert(0, '/mnt/web/oc.tl.django/linkblog/linkblog/' + '/../../lib/python2.7/site-packages/')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linkblog.settings")

import requests
from oauth_hook import OAuthHook
from django.conf import settings
from links.models import Tweet
import json
from django.db import IntegrityError
from datetime import datetime

def get_authenticated_client():
    oauth_hook = OAuthHook(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET, settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_HEADER_AUTH)

    client = requests.session(hooks={'pre_request': oauth_hook})

    return client

def load_tweets():
    client = get_authenticated_client()

    r = client.get('http://api.twitter.com/statuses/user_timeline.json')

    for tweet in r.json:
        print tweet
        t = Tweet()
        t.tweet_id = tweet['id_str']
        t.text = tweet['text']
        t.created = datetime.strftime(datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
        t.name = tweet['text']
        t.raw_tweet_json = json.dumps(tweet, indent=2)
        try:
            t.save()
        except IntegrityError:
            pass
        

if __name__ == '__main__':
    load_tweets()
