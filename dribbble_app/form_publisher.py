from .models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.FileField(upload_to="")
    title = forms.CharField(max_length=200)
    tags = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    # setting = forms.IntegerField()
    created_at = models.DateField(default=timezone.now(), blank=True)
    
    class Meta :
        model = form_publisher
        fields = '__all__'