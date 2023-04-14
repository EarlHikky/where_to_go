from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from .models import Places, Images


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Images
    extra = 0
    fields = ('image', 'get_html_photo', 'position')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=200>")

    get_html_photo.short_description = "Просмотр"


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ImagesInline,
    ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_html_photo', 'position')
    ordering = ('place', 'position',)
    list_filter = ('place',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200>")

    get_html_photo.short_description = "Фото"


admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
