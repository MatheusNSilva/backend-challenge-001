from django.db import models

from post.models import Post


class Comment(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)