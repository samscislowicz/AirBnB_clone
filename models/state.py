#!/usr/bin/python3
"""State modeule. Creates state class a subclass of basemodel"""
import models
from models import *


class State(BaseModel):
    """State class. Subclass of basemodel"""
    def __init__(self, *args, **kwargs):
        """ initializes from super """
        super().__init__(*args, **kwargs)

    name = ""
