#!/usr/bin/python3
"""define BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel of HBnB"""

    def __init__(self, *args, **kwargs):
        """Initializes new BaseModel

        Arguments:
            *args - any: Unused
            **kwargs - dict: Key/value pairs attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime, saves the instance"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel instance

        Includes key/value pair __class__ representing 
        class name of the object
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return print/str representation of BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
