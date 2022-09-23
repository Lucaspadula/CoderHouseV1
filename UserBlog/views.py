from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages



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
    #'name_submit':'Login'    
    }
    return render(request,'UserBlog/login.html',contexto)