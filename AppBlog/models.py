from asyncio.proactor_events import BaseProactorEventLoop
import email
from email.mime import image
from re import A
from django.db import models

class user(models.Model):
    nombre = models.CharField(max_length=40)
    apelllido = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    image = models.CharField(max_length=40)
    status =  models.IntegerField()
    created_time  = models.DateField()



class Commentario(models.Model):
    name = models.CharField(max_length=40)
    Comentario = models.TextField()
    created_at= models.DateField()
    
    

class post(models.Model):
    titulo = models
    breve = models.CharField(max_length=40)
    contenido = models.TextField()
    image= models.CharField(max_length=40)
    created_at= models.DateField()
    