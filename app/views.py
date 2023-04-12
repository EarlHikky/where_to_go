import collections
import json

from django.shortcuts import render

from app.models import Places


def findex(request):
    """Вью главной страницы."""
    places_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "static/app/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "static/app/places/roofs24.json"
                }
            }
        ]
    }

    return render(
        request,
        'app/index.html',
        context={'places_geojson': places_geojson}
    )


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
                    "title": 'place.title',
                    "placeId": place.pk,
                    "detailsUrl": 'detailsUrl[i]'
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": places_points
    }

    return render(request, 'app/index.html', {'places_geojson': places_geojson})

# def place_page_view(request):
#     places_points = collections.defaultdict(list)
#     for wine in wines_list[1:]:
#         wines[wine[0]].append({_param: _item for _param, _item in zip(params, wine)})
#     place_detales = {
#         "title": place.title,
#         "imgs": [img.image.url for img in place.images.all()],
#         "description_short": place.short_description,
#         "description_long": place.long_description,
#         "coordinates": {
#             "lng": place.lng,
#             "lat": place.lat,
#             }
#         }
#     context = {
#         'json': json.dumps(place_detales, ensure_ascii=False, indent=4),
#     }
#     return render(request, 'app/index.html', context=context)
