
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, null = False, on_delete=models.CASCADE)# si elimino un user se elimna la imagen
    imagen = models.ImageField(default = 'pro2.jpeg',upload_to='avatares', null = True, blank = True)
    imgPort = models.ImageField(default = 'pro2.jpeg',upload_to='avatares', null = True, blank = True)