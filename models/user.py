#!/usr/bin/python3
"""
User Class
"""
import models
from models import *


class User(BaseModel):
    """ User Classes that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ initializes email, password, first_name and last_name """
        super().__init__(*args, **kwargs)
    email = ""
    password = ""
    first_name = ""
    last_name = ""
