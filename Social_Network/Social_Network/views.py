from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse("About")


def welcome(request):
    return render(request, 'base_layout.html')
