#!/usr/bin/python3
"""Review modeule. Creates state class a subclass of basemodel"""
import models
from models import *


class Review(BaseModel):
    """Review class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """ initailizes with Super variables """
        super().__init__(*args, **kwargs)
    user_id = ""
    place_id = ""
    text = ""
