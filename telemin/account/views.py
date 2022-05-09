from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User


def profile_page(request):
    user = User
    context = {
        'user': user
    }
    return render(request, 'account/profile.html', context)