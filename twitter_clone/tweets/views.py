from django.shortcuts import render
from .models import Tweet

def feed(request):
    all_tweets = Tweet.objects.all()
    return render(request, "feed.html", {'tweets': all_tweets})
