from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(_('title'), max_length=150)
    content = models.TextField(_('content'))
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_(
        'post'), on_delete=models.CASCADE, related_name='comments')
