from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from .models import Places, Images
from .utils import get_html_photo


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Images
    extra = 0
    fields = ('image', get_html_photo, 'position')
    readonly_fields = (get_html_photo,)


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ImagesInline,
    ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('__str__', get_html_photo, 'position')
    ordering = ('place', 'position',)
    list_filter = ('place',)
    get_html_photo.short_description = 'Просмотр'


admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
