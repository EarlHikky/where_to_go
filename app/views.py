from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from app.models import Places, Images


def index(request):
    places = Places.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_lng, place.coordinates_lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.slug,
                    "detailsUrl": reverse('places', args=[place.pk])
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'app/index.html', {'places_geojson': places_geojson})


def place_view(request, place_id):
    place = get_object_or_404(Places, pk=place_id)
    images = Images.objects.filter(place=place)
    place_json = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coordinates_lat,
            "lng": place.coordinates_lng
        }
    }

    return JsonResponse(place_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
