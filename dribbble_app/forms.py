from django import forms
from .models import Design

class DesignForm(forms.ModelForm):
    class Meta :
        model = Design
        fields = '__all__'

class DesignSearchForm(forms.Form):
    search= forms.CharField(max_length=100)