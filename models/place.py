#!/usr/bin/python3
"""Place modeule. Creates state class a subclass of basemodel"""
import models
from models import *


class Place(BaseModel):
    """Place class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """ initailizes Place with Super models """
        super().__init__(*args, **kwargs)
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenities = []
