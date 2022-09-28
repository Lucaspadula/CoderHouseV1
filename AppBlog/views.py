from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import  ListView
import random
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
        }    
            
        
        return render(request, 'index.html',contexto)

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def samplepost(request):
    return render(request, 'post.html')


def user(request):
    return render(request, 'contact.html')