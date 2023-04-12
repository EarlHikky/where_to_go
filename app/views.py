from django.shortcuts import render
from app.models import Places


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
