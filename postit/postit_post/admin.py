from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.PostLikes)
admin.site.register(models.CommentLikes)
