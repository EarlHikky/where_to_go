from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Places, Images


class ImagesInline(admin.TabularInline):
    model = Images
    fields = ('image', 'get_html_photo', 'position')
    readonly_fields = ('get_html_photo',)


    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=200>")

    get_html_photo.short_description = "Просмотр"

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ImagesInline,
    ]


class ImagesAdmin(admin.ModelAdmin):
    # list_display = ('position', 'place',)
    list_display = ('__str__', 'get_html_photo', 'position')

    # list_display_links = ('position', 'place',)
    # list_display_links = ('place',)
    # search_fields = ('name',)
    # prepopulated_fields = {"name": ("name",)}
    # exclude = ('name',)
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200>")

    get_html_photo.short_description = "Фото"


admin.site.register(Places, PlacesAdmin)
admin.site.register(Images, ImagesAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
