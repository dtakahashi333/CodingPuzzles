from unittest import TestCase
from product_except_self import ProductExceptSelf


class TestProductExceptSelf(TestCase):

    def test_solve1_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertListEqual(expected, ProductExceptSelf.solve1(nums))

    def test_solve1_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertListEqual(expected, ProductExceptSelf.solve1(nums))

    def test_solve2_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertListEqual(expected, ProductExceptSelf.solve2(nums))

    def test_solve2_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertListEqual(expected, ProductExceptSelf.solve2(nums))
