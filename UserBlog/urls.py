from django.urls import path
from django.contrib.auth.views import *
from UserBlog.views import *

urlpatterns = [
    path('login/',login_request, name='UserBlogLogin'),
    path('registro/',register, name='UserBlogRegistro'),
    path('logout/',LogoutView.as_view(template_name='UserBlog/logout.html'), name='UserBlogLogout'),
    path('editar/',editar_usuario,name='UserEditar'),
    path('avatar/',upload_avatar,name='UserBlogAvatar'),
    path('borrarUser/',eliminar_user,name = 'UserDelete')
    

]