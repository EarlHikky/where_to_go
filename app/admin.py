from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Places, Images


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

class ImagesAdmin(admin.ModelAdmin):
    # list_display = ('position', 'place',)
    list_display = ('__str__',)
    # list_display_links = ('position', 'place',)
    # list_display_links = ('place',)
    # search_fields = ('name',)
    # prepopulated_fields = {"name": ("name",)}
    # exclude = ('name',)



admin.site.register(Places, PlacesAdmin)
admin.site.register(Images, ImagesAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
