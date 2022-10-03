from . import views
from django.urls import path
from AppBlog.models import post
from AppBlog.views import *


urlpatterns = [
    path('', inicio.as_view(), name='AppBlogInicio'),
    path('About/', about, name='About'),
    path('Post/', posts, name='AppBlogPost'),
    path('CrearPost/', CrearPost, name = 'AppBlogCrearPost'),
    path('DeletePost/<int:id>',eliminarPost, name='AppBlogDeletePost' ),
    path('EditarPost/<int:id>',EditarPost, name='AppBlogEditarPost' ),
    path('Perfil/<str:username>',views.profile, name='AppBlogPerfil' )
    
]