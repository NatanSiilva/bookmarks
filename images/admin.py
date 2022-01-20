from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'url', 'user', 'image', 'created')
    list_filter = ('created', 'user')
    search_fields = ('title', 'description', 'url', 'user')
    prepopulated_fields = {'slug': ('title',)}
