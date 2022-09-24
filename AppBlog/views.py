from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def samplepost(request):
    return render(request, 'post.html')


def user(request):
    return render(request, 'contact.html')