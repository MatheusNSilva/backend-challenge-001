from django.db import models

from topic.models import Topic


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)