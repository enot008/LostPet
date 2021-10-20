from django.shortcuts import render


def index(request):
    return render(request, 'myServer/index.html')


def tasks(request):
    return render(request, 'myServer/tasks.html')


def maps(request):
    return render(request, 'myServer/map.html')


def profile(request):
    return render(request, 'myServer/profile.html')