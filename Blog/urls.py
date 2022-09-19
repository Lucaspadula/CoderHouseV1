
from django.contrib import admin
from django.urls import path,include

from AppBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/',include('AppBlog.urls'))
]
