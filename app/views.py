from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from app.models import Places, Images


def index(request):
    places = Places.objects.all()
    places_points = []
    detailsUrl = ["./static/app/places/moscow_legends.json", "./static/app/places/roofs24.json"]

    for i, place in enumerate(places):
        places_points.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_lng, place.coordinates_lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.slug,
                    "detailsUrl": detailsUrl[i]
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": places_points
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
