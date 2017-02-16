#!/usr/bin/python3
"""
File Storage Class
"""
import os
import json
from models import *

class FileStorage():
    """ Serializes instances to a JSON file and deserializes
        JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all Objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Create a new object in __objects with key obj.id """
        obj_dict = FileStorage.__objects
        obj_dict[obj.id] = obj

    def save(self):
        """ Serialize __objects to the JSON file given __file_path"""
        serialized_dict = {}
        unserialized_dict = FileStorage.__objects
        for key in unserialized_dict.keys():
            serialized_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode='w+') as f:
            s_json = json.dumps(serialized_dict)
            f.write(s_json)

    def reload(self):
        """ Deserialize the JSON file to __objects, only if JSON file exist """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r+') as f:
                d_json = json.load(f)
            for key in d_json.keys():
                # search for the string BaseModel or User
                inst_dict = d_json[key]
                inst_class = inst_dict['__class__']
                if "BaseModel" in inst_dict['__class__']:
                    FileStorage.__objects[key] = BaseModel(d_json[key])
                if "User" in inst_dict['__class__']:
                    FileStorage.__objects[key] = User(d_json[key])
                if "State" in inst_dict['__class__']:
                    FileStorage.__objects[key] = State(d_json[key])
                if "Amenity" in inst_dict['__class__']:
                    FileStorage.__objects[key] = Amenity(d_json[key])
                if  "City" in inst_dict['__class__']:
                    FileStorage.__objects[key] = City(d_json[key])
                if "Place" in inst_dict['__class__']:
                    FileStorage.__objects[key] = Place(d_json[key])
                if "Review" in inst_dict['__class__']:
                    FileStorage.__objects[key] = Review(d_json[key])
