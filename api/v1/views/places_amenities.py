#!/usr/bin/python3
"""
Module to retrieve all amenities of a Place
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place


@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def get_amenities_of_place(place_id):
    """
    Retrieves the list of all Amenities of a Place object
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    amenities = []
    for amenity in place.amenities:
        amenities.append(amenity.to_dict())

    return jsonify(amenities)
