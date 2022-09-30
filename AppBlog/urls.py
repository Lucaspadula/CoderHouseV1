from django.urls import path
from AppBlog.models import post
from AppBlog.views import *


urlpatterns = [
    path('', inicio.as_view(), name='AppBlogInicio'),
    path('About/', about, name='About'),
    path('Post/', posts, name='AppBlogPost'),
    path('User/', user, name='User')
]