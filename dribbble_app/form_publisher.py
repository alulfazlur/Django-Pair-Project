from .models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    image = forms.CharField(max_length=200)
    judul_blog = forms.CharField(max_length=200)
    pesan = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()
    komen = forms.IntegerField()
    
    class Meta :
        model = Blog
        fields = '__all__'