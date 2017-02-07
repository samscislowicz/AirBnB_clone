#!/usr/bin/python3
""" Base Model """
import uuid
import datetime


class BaseModel():
    """ Defines all common attributes and methods for all classes"""
    def __init__(self, id="", created_at="", updated_at=""):
        """ intializes id, created_at, and updated_at instance vars"""
        self.id = str(uuid.uuid1());
        self.created_at = str(datetime.datetime.utcnow());

    def save(self):
        """ updates the update_at time instance """
        self.updated_at = str(datetime.datetime.utcnow());

    def to_json(self):
        """ Return a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__
        my_dict["__class__"] = str(type(self).__name__);
        return my_dict

    def __str__(self):
        """ Return a str represetation as:
            [<class name>] (<self.id>) <self.__dict__> """

        class_name = type(self).__name__
        id_str = str(self.id);
        return "[" + class_name + "] (" + id_str + ") " + str(self.__dict__)
