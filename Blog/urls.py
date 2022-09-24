
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include

from AppBlog.views import *

urlpatterns = [
    path('',lambda req: redirect('AppBlogInicio')),
    path('admin/', admin.site.urls),
    path('AppBlog/',include('AppBlog.urls')),
    path('UserBlog/', include('UserBlog.urls')),

]
