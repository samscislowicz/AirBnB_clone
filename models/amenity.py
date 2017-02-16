#!/usr/bin/python3
"""Amenity modeule. Creates state class a subclass of basemodel"""
import models
from models import *


class Amenity(BaseModel):
    """Amenity class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """ initializes super class """
        super().__init__(*args, **kwargs)

    name = ""
