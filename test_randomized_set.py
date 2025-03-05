from unittest import TestCase
from randomized_set import RandomizedSet


class TestRandomizedSet(TestCase):

    def test_get_random(self):
        obj = RandomizedSet()
        self.assertEqual(True, obj.insert(1))
        self.assertEqual(False, obj.remove(2))
        self.assertEqual(True, obj.insert(2))
        self.assertTrue(1 <= obj.getRandom() <= 2)
        self.assertEqual(True, obj.remove(1))
        self.assertEqual(False, obj.insert(2))
        self.assertEqual(2, obj.getRandom())
