from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Место")
    description_short = models.TextField(verbose_name="Короткое описание", blank=True)
    description_long = HTMLField(verbose_name="Описание", blank=True)
    coordinates_lng = models.FloatField(max_length=25, verbose_name="Долгота", blank=True)
    coordinates_lat = models.FloatField(max_length=25, verbose_name="Широта", blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('places', kwargs={'place_id': self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Places, self).save(*args, **kwargs)


class Images(models.Model):
    def choose_folder(self, filename):
        return f'./photos/{self.place.slug}/{filename}'

    place = models.ForeignKey(Places, verbose_name='Место', related_name='place_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=choose_folder, verbose_name="Фото")
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('position',)

    def __str__(self):
        return f'{self.position} {self.place.title}'
