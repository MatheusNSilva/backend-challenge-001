from django.contrib import admin
from .models import Post

admin.site.register(Post)
class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'topic')
    list_display_links = ('id', 'title')
    list_per_page = 20