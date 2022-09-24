from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):#no lo usamos como Form 
    email = forms.EmailField()
    last_name = forms.CharField(max_length=40)
    

    class Meta:
        model = User 
        fields = ('username', 'email', 'last_name')# no nos preocupemos por la contraseña ya que eso se ocupa django. /// El username se vuelve a ingresar ya que se borra nuevmaente el meta.  
        