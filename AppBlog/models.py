from asyncio.proactor_events import BaseProactorEventLoop
import email
from email.mime import image
from re import A
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(null=True)
    
    
    class Meta:
        abstract = True 

class Commentario(models.Model):
    name = models.CharField(max_length=40)
    Comentario = models.TextField()
    created_at= models.DateField()
    
    

class post(ModelBase):
    titulo = models.CharField('titulo del post',max_length=100, unique=True,null=True )
    slug = models.CharField('slug',max_length=150, unique=True, null=True)
    breve = models.CharField('breve',max_length=40)
    contenido = RichTextField(null=True)
    user = models.OneToOneField(User, null = False, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatares', null=True, blank=True)
    created_at = models.DateField(null=True)   
    
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'    
    
    def __str__(self):
        return self.titulo

class perfil(models.Model):
    user = models.OneToOneField(User, null = False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    github =  models.CharField(max_length=100)
    facebook= models.CharField(max_length=100)
    photo_portada = models.ImageField(upload_to='avatares')
    
    