from django.contrib import admin

from .models import User, UserDesign, DesignComment, DesignLike, CommentLike
# Register your models here.

admin.site.register(User)
admin.site.register(UserDesign)
admin.site.register(DesignComment)
admin.site.register(DesignLike)
admin.site.register(CommentLike)
