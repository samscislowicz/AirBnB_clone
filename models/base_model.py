#!/usr/bin/python3
"""
Base Model
"""
import uuid
import datetime
import models
import sys


class BaseModel():
    """ Defines all common attributes and methods for all classes """
    def __init__(self, *args, **kwargs):
        """ intializes id, created_at, and updated_at instance vars """
        flag = 0
        if len(args) > 0 and type(args[0]) is dict:
            flag = 1
        if flag == 1:
            create_datetime_str = args[0]['created_at']
            args[0]['created_at'] = (datetime.datetime.strptime(
                create_datetime_str, "%Y-%m-%d %H:%M:%S.%f"))
            update_datetime_str = args[0]['updated_at']
            args[0]['updated_at'] = (datetime.datetime.strptime(
                update_datetime_str, "%Y-%m-%d %H:%M:%S.%f"))
            self.__dict__ = args[0]
        else:
            self.id = str(uuid.uuid1())
            self.created_at = (datetime.datetime.now())
            models.storage.new(self)

    def save(self):
        """ updates public instance attr. updated_at with current datetime """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_json(self):
        """ Return a dictionary containing all keys/values of __dict__ """
        my_dict = {}
        for item in self.__dict__.keys():
            if (isinstance(self.__dict__[item], datetime.datetime)):
                my_dict[item] = str(self.__dict__[item])
            else:
                my_dict[item] = (self.__dict__[item])
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def __str__(self):
        """ Return a str represetation as:
            [<class name>] (<self.id>) <self.__dict__> """
        string = ""
        string += "[{}] ({}) {}]".format(type(self).__name__,
                                         self.id, self.__dict__)
        return string
