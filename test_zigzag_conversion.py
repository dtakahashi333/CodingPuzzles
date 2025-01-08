from unittest import TestCase
from zigzag_conversion import ZigzagConversion


class TestZigzagConversion(TestCase):

    def test_solve(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(expected, ZigzagConversion.solve(s, numRows))
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        ZigzagConversion.solve(s, numRows)
        self.assertEqual(expected, ZigzagConversion.solve(s, numRows))
