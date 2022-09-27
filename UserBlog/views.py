

from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from UserBlog.forms import *
from UserBlog.models import Avatar



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



@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST) #capturamos la inf en el formulario 
        form = UserRegisterForm(request.POST)
        
        if form.is_valid(): #validamos 
            
            data = form.cleaned_data
            
            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')
            usuario.save()

            
            messages.info(request, 'Tu usuario fue editado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser editado!')
        return redirect('AppBlogInicio')    
    
    

    contexto = {
        'form':UserRegisterForm(
            initial={
                'username':usuario.username,
                'email':usuario.email,
                'last_name':usuario.last_name
            }),
        'accion_form': 'Editar',
        'titulo_form': 'Editar Usuario'
    }    

    return render(request,'base_formulario.html',contexto)


def upload_avatar(request):
    if request.method == "POST":
        
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user = data.get("user"))
            
            if len(avatar)> 0:
                
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data("imagen")
                avatar.save()
                
                messages.info(request, 'Tu imagne fue editada satisfactoriamente!')
            else:
                avatar = Avatar(user=data.get("user"), imagen= data.get("imagen"))
                avatar.save()
                
                messages.info(request, 'Tu imagen fue creada satisfactoriamente!')
                
        return redirect('AppBlogInicio')
                
    
    contexto={
        "form":AvatarForm(),
        'accion_form': 'Crear',
        'titulo_form': 'Crear Avatar'
    }
    return render(request, 'base_formulario.html',contexto)




