from unittest import TestCase
from gcd_of_strings import GcdOfStrings


class TestGcdOfStrings(TestCase):

    def test_solve(self):
        self.assertEqual("ABC", GcdOfStrings.solve("ABC", "ABCABC"))
        self.assertEqual("AB", GcdOfStrings.solve("ABABAB", "ABAB"))
        self.assertEqual("", GcdOfStrings.solve("LEET", "CODE"))
        self.assertEqual("CXTXN", GcdOfStrings.solve("CXTXNCXTXNCXTXNCXTXNCXTXN",
                                                     "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"))
        self.assertEqual("FBFKOX", GcdOfStrings.solve("FBFKOXFBFKOXFBFKOXFBFKOXFBFKOX",
                                                      "FBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOXFBFKOX"))
