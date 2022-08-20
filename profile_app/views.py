from django.shortcuts import render
from django.utils import timezone
from .models import Profile

def profile_list(request):
    profiles = Profile.objects.filter(updated_date__lte=timezone.now()).order_by('updated_date')
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile(request):
    return render(request, 'profile.html', {})
