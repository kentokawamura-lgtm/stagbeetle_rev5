from django import forms
from .models import Adultmodel
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Adultmodel
        fields = ['image', 'name', 'gender','size','gener','date','memo']