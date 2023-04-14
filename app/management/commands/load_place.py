import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from io import BytesIO
from app.models import Places, Images


class Command(BaseCommand):
    help = 'Add place from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('place_url', help='ссылка на json', type=str)

    def handle(self, *args, **options):
        place_response = requests.get(options['place_url'])
        place_response.raise_for_status()
        place_raw = place_response.json()
        place, created = Places.objects.get_or_create(
            title=place_raw['title'],
            defaults={
                'description_short': place_raw['description_short'],
                'description_long': place_raw['description_long'],
                'coordinates_lng': place_raw['coordinates']['lng'],
                'coordinates_lat': place_raw['coordinates']['lat']
            }
        )
        if not created:
            return
        for index, img_url in enumerate(place_raw['imgs'], 1):
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            filename = os.path.basename(img_url)
            picture = Images.objects.create(place=place, position=index)
            picture.image.save(
                filename,
                ContentFile(BytesIO(img_response.content).getvalue()),
                save=False
            )
            picture.save()
