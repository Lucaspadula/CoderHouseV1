from django import  forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from ckeditor.fields import RichTextField

from AppBlog.models import post


class BlogForms(forms.ModelForm):
    class Meta:
        
        model = post
        fields = ['titulo',
                    'breve',
                    'contenido',
                    'user',
                    'image',
                    'created_at'
                    ]


class EditForms(forms.ModelForm):
    class Meta:
        
        model = post
        fields = ['titulo',
                    'breve',
                    'contenido',
                    'image',
                    'created_at'
                    ]
