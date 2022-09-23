from django.urls import path
from UserBlog.views import *

urlpatterns = [
    path('login',login_request, name='Login')
]