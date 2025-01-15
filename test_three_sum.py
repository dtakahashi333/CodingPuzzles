from unittest import TestCase
from three_sum import ThreeSum
import json


class TestThreeSum(TestCase):

    def test_solve(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
        nums = [0, 1, 1]
        expected = []
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
        nums = [-2, 0, 0, 2, 2]
        expected = [[-2, 0, 2]]
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
        nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
        expected = [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2],
                    [-1, 0, 1]]
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
        with open("./data/three_sum/input.txt", "r") as input_file:
            nums = json.load(input_file)
        with open("./data/three_sum/output.txt", "r") as output_file:
            expected = json.load(output_file)
        self.assertCountEqual(expected, ThreeSum.solveByOptimal(nums))
