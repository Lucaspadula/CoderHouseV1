
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import forms

from UserBlog.models import Avatar

class UserRegisterForm(UserCreationForm):#no lo usamos como Form 
    email = forms.EmailField()
    last_name = forms.CharField(max_length=40)
    is_superuser = forms.IntegerField(help_text="1: Super Usuario, 0: Usuario Normal")
    

    class Meta:
        model = User 
        fields = ('username', 'email', 'last_name','is_superuser')
        # no nos preocupemos por la contraseña ya que eso se ocupa django. /// El username se vuelve a ingresar ya que se borra nuevmaente el meta.  
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields =  [
                    'user',
                    'imagen',
                    'imgPort'
                    
        ]

class PerfilForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields= ('username',
                'email', 
                'last_name'
        )
        