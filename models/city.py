#!/usr/bin/python3
"""City modeule. Creates state class a subclass of basemodel"""
import models
from models import *


class City(BaseModel):
    """City class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """ initialize super class """
        super().__init__(*args, **kwargs)
    name = ""
    state_id = ""
