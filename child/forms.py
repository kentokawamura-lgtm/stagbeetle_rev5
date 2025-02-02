from django import forms
from .models import Childmodel

class PostForm(forms.ModelForm):
    class Meta:
        model = Childmodel
        fields = ['number','size_ad','ad_date', 'name','gender','gener','date','date_1','date_2','date_3','date_4','date_5','weight_1','weight_2','weight_3','weight_4','memo']