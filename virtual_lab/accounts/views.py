from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.middleware.csrf import get_token

# views.py
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

@login_required
def update_score(request, score):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_profile.score = score
    user_profile.save()
    return redirect('quiz.html')  # Ganti dengan URL yang sesuai

@csrf_exempt  # Hapus ini setelah debugging
def register(request):
    if request.method == 'POST':
        print(request.META.get('HTTP_X_CSRFTOKEN'))  # Debugging

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@csrf_exempt  # Hapus ini setelah debugging

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Ganti dengan URL yang sesuai
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})