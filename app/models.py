from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Places(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Место")
    description_short = models.CharField(max_length=255, verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Описание")
    coordinates_lng = models.CharField(max_length=25, verbose_name="Долгота")
    coordinates_lat = models.CharField(max_length=25, verbose_name="Широта")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Places, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('place', kwargs={'place_id': self.slug})
