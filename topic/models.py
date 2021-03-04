from django.db import models
from settings.settings import AUTH_USER_MODEL


class Topic(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='topic',on_delete = models.CASCADE)
    description = models.CharField(max_length=500)
    urlName = models.SlugField,
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
