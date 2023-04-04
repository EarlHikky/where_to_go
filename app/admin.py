from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Places


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Places, PlacesAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
