from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Место")
    description_short = models.CharField(max_length=255, verbose_name="Короткое описание")
    description_long = HTMLField(verbose_name="Описание", blank=True, default='')
    coordinates_lng = models.FloatField(max_length=25, verbose_name="Долгота")
    coordinates_lat = models.FloatField(max_length=25, verbose_name="Широта")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Places, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('places', kwargs={'place_id': self.pk})


class Images(models.Model):
    def choose_folder(self, filename):
        return f'./photos/{self.place.slug}/{filename}'

    place = models.ForeignKey(Places, verbose_name='Место', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=choose_folder, verbose_name="Фото")
    position = models.PositiveIntegerField(verbose_name='Позиция')

    # slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('place', 'position',)
        # ordering = ('position',)

    # def save(self, *args, **kwargs):
    #     self.name = str(len(Images.objects.filter(place_id=self.place)) + 1) + " " + self.place.__str__()
    #     return super(Images, self).save(*args, **kwargs)

# def get_absolute_url(self):
#     return reverse('image', kwargs={'image_id': self.slug})
