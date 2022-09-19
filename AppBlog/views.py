from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def samplepost(request):
    return render(request, 'post.html')


def user(request):
    return render(request, 'contact.html')