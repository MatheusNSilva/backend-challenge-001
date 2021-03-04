from django.contrib import admin
from .models import Topic

admin.site.register(Topic)
class Topics(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'author', 'description', 'urlName', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'name', )
    list_per_page = 20

