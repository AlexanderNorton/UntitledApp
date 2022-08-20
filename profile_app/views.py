from django.shortcuts import render

def profile_list(request):
    return render(request, 'profile_list.html', {})