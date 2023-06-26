from django.shortcuts import render
from .models import Tweet
from django.contrib.auth.decorators import login_required

def feed(request):
    all_tweets = Tweet.objects.all()
    return render(request, "feed.html", {'tweets': all_tweets})


def home(request):
    return render(request, "home.html")

@login_required
def profile(request):
    return render(request, "profile.html")
