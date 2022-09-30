from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView
import random
from django.contrib import messages
from AppBlog.models import post

def consulta(id):
    return post.objects.get(id = id)

class inicio(ListView):
    
    def get(self,request,*args,**kwargs):
        
        posts = list(post.objects.all().values_list('id', flat = True))
        print(posts)
        #if posts > 1:
        try:        
            principal = random.choice(posts)
            posts.remove(principal)
            principal  = consulta(principal)
        except:
            posts = None
        contexto={
            
            'principal': principal,
            'post':posts,
        }    
            
        
        return render(request, 'index.html',contexto)
    
    
@login_required
def posts(request):
    
    posts = post.objects.all()
    print("Posts ", posts )
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(posts,1)
        posts= paginator.page(page)
    except:
        messages.info(request, 'No hay ningun posts!!')
    
    contexto = {
        'entity':posts,
        'paginator':paginator,
    }
    return render(request, 'post.html',contexto)


 

@login_required
def about(request):
    return render(request, 'about.html')




def user(request):
    return render(request, 'contact.html')