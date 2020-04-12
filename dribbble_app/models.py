from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    Bio = models.TextField(blank=True, null=True)

    avatar = models.FileField(upload_to="")


    def __str__(self):
        return self.username + ' : ' + self.email

class UserDesign(models.Model):
    design = models.FileField(upload_to="")
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateField(default=timezone.now(), blank=True)

    def __str(self):
        return self.username + ' : ' + self.title
class CommentLike(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.FileField(upload_to="", default ='AVATAR.png')
    comment = models.TextField(blank=False, null=False)
    like = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now(), blank=True)

    def __str(self):
        return self.name
