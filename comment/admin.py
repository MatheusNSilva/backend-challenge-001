from django.contrib import admin
from .models import Comment

admin.site.register(Comment)

class Comments(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'post')
    list_display_links = ('id', 'title')
    list_per_page = 20
