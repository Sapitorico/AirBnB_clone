#!/usr/bin/python3
""" this a parent class, it is in charge of creating your data model
manage (create, update, destroy, etc.)
objects through a console/command interpreter"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Public instance attribute:
    * ID: assign with an UUID -String when an instance is created
    * CREATED_AT: assign with the current date and time when
        an instance is created
    * UPDATE_AT: assign with the current date and
        time when an instance is created and each will be updated
    """

    def __init__(self, *args, **kwargs):
        """ instances attributes
        if kwargs is not empty:
            * Each key to this dictionary is an attribute name
            (Kwargs __class__ is the only one that should
            not be added as an attribute)
            * Each value of this dictionary is the value of this attribute name
            * Tunas to keep created_at and updated_at in datetime format
        otherwise:
            create id and created_at as you did previously (new instance)
        """
        """ Now to get the current date and time """
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    """ Public instance methods:
    Save: Update the Datetime
    TO_DICT: Dictionary representation of an instance
    __Str__: Dictionary representation of a class
    """
    def save(self):
        """ Update the UPDATED_AAT public
            instance attribute with the current date and time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary that contains all the
            __ct__ keys/values of the instance
        My_Ded = Self .__ dict__ returns only the
            attributes of the established inst usual
        CREATED_AT and UPDATED_AT must become an ISO format object
        """
        my_dict = []
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict.append((key, value.isoformat()))
            else:
                my_dict.append((key, value))
        my_dict.append(("__class__", self.__class__.__name__))
        return dict(my_dict)

    """ Representation of classes like strings """
    def __str__(self):
        """ You must print [<class name>] (<self.id) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
