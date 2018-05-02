from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def status(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            display_posts(request)
            return redirect('home:post')
    else:
        posts = Post.objects.all().order_by('-date')
        return render(request, 'home/home.html', {'posts': posts})


def display_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'home/home.html', {'posts': posts})