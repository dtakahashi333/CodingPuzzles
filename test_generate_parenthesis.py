from unittest import TestCase
from generate_parenthesis import GenerateParenthesis


class TestGenerateParenthesis(TestCase):

    def test_solve(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertListEqual(expected, GenerateParenthesis.solve(n))
        n = 1
        expected = ["()"]
        self.assertListEqual(expected, GenerateParenthesis.solve(n))
