from .models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    media = forms.FileField()
    title = forms.CharField(max_length=200)
    tags = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)
    # setting = forms.IntegerField()
    attach_file = form.FileField()
    add_project = form.FileField()
    for_sale = form.FileField()
    
    class Meta :
        model = Blog
        fields = '__all__'