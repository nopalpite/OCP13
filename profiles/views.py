from django.shortcuts import render
from .models import Profile


def index(request):
    """
    View function for the index page displaying a list of user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function for displaying details of a specific user profile.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
