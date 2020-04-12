from django.contrib import admin

from .models import User, UserDesign, CommentLike
# Register your models here.

admin.site.register(User)
admin.site.register(UserDesign)
admin.site.register(CommentLike)
