#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
import os


class FileStorage:
    """
    Private class attributes:
        __file_path: string -Route to the JSON file (for example: file.json)
        __objects: Dictionary: Vacuum
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

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
        key = f"{type(obj.__class__.__name__)}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                self.__objects = json.load(f)
        else:
            with open(self.__file_path, "w", encoding='utf-8') as f:
                json.dump(self.__objects, f)
