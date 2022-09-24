from django.urls import path
from django.contrib.auth.views import LogoutView
from UserBlog.views import *

urlpatterns = [
    path('login/',login_request, name='UserBlogLogin'),
    path('registro/',register, name='UserBlogRegistro'),
    path('logout/',LogoutView.as_view(template_name='UserBlog/logout.html'), name='UserBlogLogout')

]