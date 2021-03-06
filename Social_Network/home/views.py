from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import forms
from .models import Post, Friend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import json

@login_required
def status(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            # display_posts(request)
            return redirect('home:post')
    else:
        posts = Post.objects.all().order_by('-date')
        # users = User.objects.all()
        # query = request.GET.get("q")
        # if query:
        #     posts = posts.filter(Q(body__icontains=query) |
        #                          Q(author__username__icontains=query)).distinct()
        # friend = Friend.objects.get(current_user=request.user)
        # friends = friend.users.all()
        # flag=False
        # for post in posts:
        #     for friend in friends:
        #         if post.author == friend :
        #                 posts = posts.filter(Q(body__icontains=post.body) |
        #                                      Q(author__username__icontains=post.author))
        #                 flag=True
        # if flag is True:
        #     args = {'posts': posts}
        # else:
        #     args = {}
        filtered_posts = []
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except ObjectDoesNotExist:
            friends = []
        for post in posts:
            if post.author == request.user:
                filtered_posts.append(post)
                continue
            for friend in friends:
                if post.author in friends:
                    filtered_posts.append(post)
                    break
        args = {
            'posts': filtered_posts
        }
        return render(request, 'home/home.html', args)


# def display_posts(request):
#     posts = Post.objects.all().order_by('-date')
#     friend = Friend.objects.get(current_user=request.user)
#     friends = friend.users.all()
#     flag = False
#     for post in posts:
#         for friend in friends:
#             if post.author == friend or post.author == request.user:
#                 posts = posts.filter(Q(body__icontains=post.body) |
#                                      Q(author__username__icontains=post.author))
#                 flag = True
#     if flag is True:
#         args = {'posts': posts}
#     else:
#         args = {}
#     return render(request, 'home/home.html', args)


def change_friends(request, operation, pk):
    #pk = pk
    friend = User.objects.get(pk=pk)
    if operation == "add":
        Friend.make_friend(request.user, friend)
    elif operation == "remove":
        Friend.lose_friend(request.user, friend)
    return redirect('accounts:friends')


def like_posts(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.likes.add(request.user)
        # count = posts.likes
        # count += 1
        # posts.likes = count
        # if count == 1:
        #     count -= 1
        #     posts.save()
        # return redirect('home:post')
    return redirect('home:post')

def unlike_posts(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.likes.remove(request.user)
    return redirect('home:post')


