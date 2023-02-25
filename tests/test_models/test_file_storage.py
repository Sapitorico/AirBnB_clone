#!/usr/bin/python3
"""Tests form  FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    def test_init(self):
        self.assertTrue(hasattr(FileStorage, "__init__"))
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        self.assertTrue(hasattr(storage, "all"))
        self.assertEqual(type(storage.all()), dict)
        self.assertTrue(hasattr(storage, "all"))
        self.assertEqual(type(storage.all()), dict)


if __name__ == '__main__':
    unittest.main()

