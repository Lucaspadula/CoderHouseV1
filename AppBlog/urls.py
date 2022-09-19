from django.urls import path
from AppBlog.models import post
from AppBlog.views import *


urlpatterns = [
    path('', inicio, name='AppInicio'),
    path('About', about, name='About'),
    path('Post', samplepost, name='Samplepost'),
    path('User', user, name='User')
]