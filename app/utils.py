from django.utils.html import format_html


def get_html_photo(photo):
    if photo.image:
        return format_html('<img src="{}" width=200>', photo.image.url)
