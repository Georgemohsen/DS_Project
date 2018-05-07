from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Friend
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:editProfile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup..html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home:post')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')


@login_required
def profile_view(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else :
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


@login_required(login_url="/accounts/login/")
def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfile(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')
    else:
        user = request.user
        profile = user.userprofile
        form = forms.EditProfile(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def user_friends(request):
    others = User.objects.exclude(id=request.user.id)
    try:
        friend = Friend.objects.get(current_user=request.user)
    except ObjectDoesNotExist:
        return render(request, 'accounts/friends.html', {'others': others, 'friends': []})
    friends = friend.users.all()
    args = {'others': others, 'friends': friends}
    return render(request, 'accounts/friends.html', args)

from django.http import JsonResponse
@login_required
def download_my_data(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        profile = user.userprofile
        obj = {
            'name': user.username,
            'about': profile.about,
            'date of Birth': profile.date_of_birth,
            'phone': profile.phone,
            'city': profile.city,
            'friends': []
        }
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        for friend in friends:
            obj['friends'].append(friend.username)
        response = JsonResponse(obj, content_type='application/json', json_dumps_params={'indent': 4})
        response['Content-Disposition'] = 'attachment; filename="data.json"'
        return response
