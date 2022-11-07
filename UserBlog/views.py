

from email.mime import image
from functools import cache
import os
from telnetlib import LOGOUT
from urllib import request
import django
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from UserBlog.forms import *
#from UserBlog.models import Avatar


@csrf_protect
def login_request(request):   

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password=contrasenia) 
            
            
            if user:
                login(request, user)
                #return render(request,"AppBlog/index.html"),
                messages.info (request,'Inicio de sesion satisfactorio!' )
            else:
                #return render(request,"AppBlog/index.html"),{"mensaje": "Error, datos incorrectos"}
                messages.info (request, 'No pudo ingresar ')
            
        else:
            
            #return render(request,"AppBlog/index.html"),{"mensaje": "Error, formulario incorrectos"}
            messages.info (request, 'formulario incorrecto ')
            
        return redirect('AppBlogInicio')
        
    contexto = {
    'form': AuthenticationForm(),
    'accion_form': 'Login',
    'titulo_form': 'Login User'
    }
    #'name_submit':'Login'    

    return render(request,'base_formulario.html',contexto)



@csrf_protect
def register(request):
    
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST) #capturamos la inf en el formulario 
        form = UserRegisterForm(request.POST)

        
        if form.is_valid(): #validamos 
            
            form.save()
            
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('AppBlogInicio')    

    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'accion_form': 'Registro',
        'titulo_form': 'Registro Usuario'
    }
    return render(request,'base_formulario.html',contexto)

def eliminar_user(request):
    usuario = request.user.id
    print(f'Usuario{usuario}')
    try:
        delete_user = User.objects.get(id = usuario)
    except User.DoesNotExist:
        messages.info(request, 'El Usuario que quieres eliminar no existe!')    
        return redirect("AppBlogInicio")
    
    if  request.user.is_superuser == True: 
        
        delete_user.delete()
        messages.info(request, f'El Usuario : {delete_user} fue eliminado!')
        return redirect("AppBlogPost")
    else:
        messages.info(request, f' No puede ser eliminado el usuario porque no es un Super Usuario')
        return redirect("AppBlogInicio")


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST) #capturamos la inf en el formulario 
        form = PerfilForm(request.POST, instance=usuario)
        print(f'form:{form}')
        if form.is_valid(): #validamos 
            
            data = form.cleaned_data
            
            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')
            usuario.save()

            
            messages.info(request, 'Tu usuario fue editado satisfactoriamente!')
        else:
            user_form = PerfilForm(instance=request.user)
            messages.info(request, 'Tu usuario no pudo ser editado!')
        return redirect('AppBlogInicio')    
    
    

    contexto = {
        'form':PerfilForm(
            initial={
                'username':usuario.username,
                'email':usuario.email,
                'last_name':usuario.last_name,
                
                
            }),
        'accion_form': 'Editar',
        'titulo_form': 'Editar Usuario'
    }    

    return render(request,'base_formulario.html',contexto)



def upload_avatar(request):
    if request.method == "POST":
        user = request.user.id
        print(f'User: {user}')
        try:
            avatar = Avatar.objects.filter( user_id = user).update(               
            )
            avatar1 = Avatar.objects.filter( user_id = user)
            
            print(f'avatar  {len(avatar1)} == 0' )
            if len(avatar1) == 0:
                
                form = AvatarForm(request.POST, request.FILES)
                if form.is_valid(): 
                    
                    print('primer if')
                    data = form.cleaned_data
                    avatar = Avatar(
                        user = data.get('user'),
                        imagen = data.get('imagen'),
                        imgPort = data.get('imgPort')
                        
                    )
                    
                    avatar.save()
                    messages.info(request, 'Tu imagen fue creada satisfactoriamente!')
                
            else:
                print(f'avatar  {len(avatar1)} != 0' )
                old_imag = Avatar.objects.get (user_id = user)
                form = AvatarForm(request.POST, request.FILES, instance = old_imag)
                print(f"avatar {avatar}")
                
                if form.is_valid(): 
                    imagen_path = old_imag.imagen.path
                    
                    if os.path.exists(imagen_path):
                        os.remove(imagen_path)
                        
                    form.save()    
                    
                    messages.info(request, 'Tu imagen fue editada satisfactoriamente!')
                        
                    return redirect('AppBlogInicio')
        except django.db.utils.IntegrityError:
            messages.error(request, "El Formulario tiene un Error")
                        
    
    contexto={
        "form":AvatarForm(),
        'accion_form': 'Crear',
        'titulo_form': 'Crear Avatar'
    }
    return render(request, 'base_formulario.html',contexto)




