from django.shortcuts import render
from django.utils import timezone
from UntitledApp.apps.profile.models import Profile
from django.contrib.auth.models import User

# Create your views here.


def homepage(request):
    profiles = Profile.objects.filter(
        updated_date__lte=timezone.now()).order_by('updated_date')
    return render(request, 'home.html', {
        'profiles': profiles
    })
