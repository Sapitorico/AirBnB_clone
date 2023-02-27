#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
import os.path


class FileStorage:
    """
    Private class attributes:
        __file_path: string -Route to the JSON file (for example: file.json)
        __objects: Dictionary: Vacuum
    """
    __file_path = "file.json"
    __objects = {}

    """
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        create file json
    """

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    if value['__class__'] == "BaseModel":
                        obj = BaseModel(**value)
                    elif value['__class__'] == "User":
                        obj = User(**value)
                    else:
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
