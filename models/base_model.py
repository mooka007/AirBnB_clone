#!/usr/bin/python3

from datetime import datetime
import json
from uuid import uuid4
import models


class Basemodel:
    """ Class defines all attributes for other classes """

    def __init__(self, *args, **kwards):
        """ Initialization of Class """

        if kwargs:
            for keys, values in kwargs.items():
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        values = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, values)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
    
    def __str__(self):
        """ Presentation of string """
        return ("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute with the current date and time """
        self.update_at = datetime.today()
        models.storage.save()
    
    def to_dict(self):
        """ Returns a dictionary that includes all the keys and their corresponding values of the instance """
        new = self.__dict__.copy()
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        new["__class__"] = self.__class__.__name__
        return new 
