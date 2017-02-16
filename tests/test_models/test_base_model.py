#!/usr/bin/python3
import unittest
from  models import *
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class """
    def setUp(self):
        """sets up objects for testing"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.model2.save()

    def test_basic_setup(self):
        """test for to_json method of BaseModel class """
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "__class__"))
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.assertTrue(hasattr(self.model2, "updated_at"))
        self.assertTrue(self.model1.id != self.model2.id)
        m1c = self.model1.created_at
        m2c = self.model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """testing attributes to ensure proper typing"""
        self.assertIsInstance(self.model1.id, str)
        self.assertIsInstance(self.model1.__class__, type)
        self.assertIsInstance(self.model1.created_at, datetime.datetime)
        self.model2.save()
        self.assertIsInstance(self.model2.updated_at, datetime.datetime)

    def test_save(self):
        """testing whether save updates the updated_at attribute"""
        self.model2.save()
        m1u = self.model2.updated_at
        self.model2.save()
        m1u_saved = self.model2.updated_at
        self.assertFalse(m1u == m1u_saved)

    def test_to_json(self):
        """tests to_json method with diffs in output & in-memory objects"""
        m1_dict = self.model1.to_json()
        m2_dict = self.model2.to_json()
        self.assertTrue(hasattr(m1_dict, "__class__"))
        self.assertTrue(m1_dict != self.model1.__dict__)
        self.assertEqual(m1_dict["id"], self.model1.__dict__["id"])
        self.assertNotEqual(m1_dict["created_at"],
                            self.model1.__dict__["created_at"])
        self.assertNotEqual(type(m1_dict["created_at"]),
                            type(self.model1.__dict__["created_at"]))
        self.assertNotEqual(m1_dict, m2_dict)

if __name__ == '__main__':
    unittest.main()
