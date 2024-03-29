from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile(request, owner):
    profile = get_object_or_404(Profile, url_tag=owner)
    return render(request, 'profile.html', {'profile': profile})
