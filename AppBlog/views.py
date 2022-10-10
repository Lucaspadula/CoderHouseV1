from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView,View
import random
import django
from django.contrib import messages
from AppBlog.forms import BlogForms, EditForms
from AppBlog.models import *
from UserBlog.forms import PerfilForm
from django.contrib.auth.models import User

from UserBlog.models import Avatar


def consulta(id):
    return post.objects.get(id = id)

class inicio(ListView):
    
    def get(self,request):
        
        ususario = request.user
        avatar = Avatar.imagen
        
        
        return render(request, 'index.html',{'user':ususario, 'avatar':avatar})
    
    
@login_required
def posts(request):
    
    posts = post.objects.all()
    print("Posts ", posts )
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(posts,1)
        posts = paginator.page(page)
        
        if len(posts) == 0:
            messages.info(request, 'No hay ningun posts!!')
    except:
            messages.info(request, 'No se encontro ningun posts!!')
        
    
    
    
    contexto = {
        'entity':posts,
        'paginator':paginator,
    }
    return render(request, 'post.html',contexto)


@login_required
def CrearPost(request):
    try:
        if request.method == "POST":
            form = BlogForms(request.POST, request.FILES)
        
            if form.is_valid():
                data = form.cleaned_data 
                posts = post(
                    titulo = data.get('titulo'),
                    breve  = data.get('breve'),
                    contenido = data.get('contenido'),
                    user = data.get('user'),
                    image=data.get('image'),
                    created_at = data.get('created_at')
                )
                if request.user.is_superuser == True: 
                    posts.save()
                    messages.info(request, f'Se creo el Post{posts.titulo} de manera correcta ') 
                    return redirect('AppBlogPost')
                else:
                    messages.info(request, f'La publicacion no puede ser Creada porque no es un Super Usuario')
                    return redirect("AppBlogInicio")

            else: 
                messages.info(request, 'El formulario se creo de manera incorrecta') 
        contexto= {
            'form': BlogForms(),
            'titulo_form': 'Crear Blog',
            'accion_form':'Crear'
        }
        return render(request, 'base_formulario.html', contexto)    
    except:
        messages.info(request, 'ERROR') 

@login_required
def eliminarPost(request, id):
    try:
        delete_post = post.objects.get(pk = id)
    except post.DoesNotExist:
        messages.info(request, 'El post que quieres eliminar no existe!')    
        return redirect("AppBlogInicio")
    

    if (delete_post.user != request.user) :
        print(f' User: {delete_post.user} y {request.user}' )
        
        messages.info(request, 'No eres el autor de este post!')    
        return redirect("AppBlogInicio")
    
    if  request.user.is_superuser == True: 
        delete_post.delete()
        messages.info(request, f'Tu Publicacion con Titulo: {delete_post} fue eliminado!')
        return redirect("AppBlogPost")
    else:
        messages.info(request, f'La publicacion no puede ser Borrada porque no es un Super Usuario')
        return redirect("AppBlogInicio")

@login_required
def EditarPost(request, id):
    editarPost = post.objects.get(pk = id)
    
    if request.method == 'POST':
        
        forms = EditForms(request.POST, request.FILES, instance=editarPost)
        try:
            if forms.is_valid():
                data = forms.cleaned_data
                
                editarPost.titulo = data.get('titulo')
                editarPost.breve = data.get('breve')
                editarPost.contenido = data.get('contenido')
                editarPost.image = data.get('image')
                editarPost.created_at = data.get('created_at')
                
                
                if  (editarPost.user != request.user):
                    print(f' User: {editarPost.user} y {request.user} ' )
                    
                    messages.info(request, 'No eres el autor de este post para editarlo!')
                    return redirect('AppBlogPost')  
                try:
                    if  request.user.is_superuser == True:    
                        print(f'si es superusuario {request.user.is_superuser}')
                        editarPost.save()
                        messages.error(request, "Se pudo Editar de manera Exitosa")
                        return redirect('AppBlogPost') 
                    else:
                        messages.error(request, "No se pudo Editar ya que no es Super Usuario")
                except django.db.utils.IntegrityError:
                    messages.error(request, "la modificacion fallo por que la Post esta repedita")
                return redirect('AppBlogPost')
            else:
                forms = EditForms(instance=post)
                messages.error(request, "El Formulario tiene un Error")
                return render(request, 'base_formulario.html',{'forms': forms})
                
        except django.db.utils.IntegrityError:
                    messages.error(request, "validacion de formulario")
    contexto = {
        'form': EditForms(
            initial = {
                "titulo":editarPost.titulo,
                "breve":editarPost.breve,
                "contenido":editarPost.contenido,
                "image":editarPost.image,
                "created_at": editarPost.created_at  
            }
        ),
        'titulo_form': 'Editar Blog',
        'accion_form':'Editar'
    }
    return render(request, 'base_formulario.html',contexto)



def profile(request,username = None):
    current_user = request.user
    if username == current_user.username:
        print(f'Username: {username} = current_user: {current_user.username}')
        user = current_user
        posts = post.objects.filter(user = current_user)
        perfiles = perfil.objects.filter(user = current_user)
        

        print(f'perfil {perfiles}')
        
    
    
    #return render(request, 'AppBlog/registroUser.html',{'user': user,'perfil':perfil,'posts':posts,'titulo_form':'Perfil User' } )
    return render(request, 'AppBlog/registroUser.html',{'user': user,
                                                        'perfils':perfiles,
                                                        'posts':posts,
                                                        'titulo_form':'Perfil User' } )


@login_required
def about(request):
    return render(request, 'about.html')

