from asyncio.proactor_events import BaseProactorEventLoop
import email
from email.mime import image
from re import A
from django.db import models



class Commentario(models.Model):
    name = models.CharField(max_length=40)
    Comentario = models.TextField()
    created_at= models.DateField()
    
    

class post(models.Model):
    titulo = models
    breve = models.CharField(max_length=40)
    contenido = models.TextField()
    image= models.ImageField(upload_to='avatares', null=True, blank=True)
    created_at= models.DateField()
    