from django.urls import path, include
from .views import index, place_view

urlpatterns = [
    path("", index, name="index"),
    path("places/<int:place_id>/", place_view, name="places"),
    path('tinymce/', include('tinymce.urls')),

]
