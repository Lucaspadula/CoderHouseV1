
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path,include
from django.conf import settings

from AppBlog.views import *

urlpatterns = [
    path('',lambda req: redirect('AppBlogInicio')),
    path('admin/', admin.site.urls),
    path('AppBlog/',include('AppBlog.urls')),
    path('UserBlog/', include('UserBlog.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)