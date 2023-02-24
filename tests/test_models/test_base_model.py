#!/usr/bin/python3
""" test from class BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    test class:
    test_is_instances
        id - string
        create_at and create_at instances form datetime
    """
    def tests_is_instances(self):
        """ Verify if the attributes are instances of a class or object"""
        my_model = BaseModel()
        my_model.number = 89
        self.assertIsInstance(my_model.number, int)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.__str__(), str)

    def test_save(self):
        """ Save test verify two -values inequality"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """ TO_DICT test if the type of data is a dictionary"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        """ Check an expected result """
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(type(my_model_dict["created_at"]), str)
        self.assertEqual(type(my_model_dict["updated_at"]), str)

    def test_str(self):
        """Str test if the type of data is a string """
        my_model = BaseModel()
        my_model_str = my_model.__str__()
        my_model.name = "sapitorico"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual
        self.assertEqual(type(my_model_str), str)
        (my_model_str, f"[BaseModel] ({my_model.id}) {my_model.__dict__}")

    def test_kwargs(self):
        """ KWARGS test if the type of data is a dictionary"""
        my_model = BaseModel()
        my_model.name = "sapitorico"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_new_model.__dict__, my_model.__dict__)
        self.assertIsNot(my_new_model, my_model)
        self.assertEqual(my_new_model.name, "sapitorico")
        self.assertEqual(my_new_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
