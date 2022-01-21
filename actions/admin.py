from django.contrib import admin

from .models import Action

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'verb', 'target', 'created')
   list_display_links = ('id', 'user', 'verb', 'target', 'created')
   list_filter = ('created',)
   search_fields = ('verb',)