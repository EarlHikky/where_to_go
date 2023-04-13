from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("places/<int:place_id>/", place_view, name="places"),

]
