#!/usr/bin/python3
"""Defining Base Model class"""
import models
from models import storage
import uuid
from datetime import datetime

class BaseModel:
    """Representing Base Model of the hbnb"""

    def __init__(self, *args, **kwargs):
        """Initializing new BaseModel
        
        Args:
            *args: Var-length arg list (not using it)
            **kwargs: Keyword args to recreate an instance from a dic representation. 
        """
        timef = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, val in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, timef)
                setattr(self, k, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
    
    def __str__(self):
        """Returns a string representation of the instance"""

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        """Update the 'updated_at' attrib with the current datetime"""
        storage.save()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert the instance to a dic representation
        
        Returns:
            dict: A dictionnary containing the attribs and values of the instance.
        """
        classname = self.__class__.__name__
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = classname
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict