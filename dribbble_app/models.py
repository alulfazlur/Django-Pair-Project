from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.FileField(upload_to="")

    def __str__(self):
        return self.fullname

class Design(models.Model):
    fullname = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.ImageField(upload_to="")
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateField(default=timezone.now(), blank=True)
    like = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str(self):
        return self.title
        
class CommentLike(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null= True, blank = True)
    name = models.CharField(max_length=50)
    avatar = models.FileField(upload_to="", default ='AVATAR.png')
    comment = models.TextField(blank=False, null=False)
    like = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now(), blank=True)

    class Meta:
        ordering = ['-id']

    def __str(self):
        return self.name
