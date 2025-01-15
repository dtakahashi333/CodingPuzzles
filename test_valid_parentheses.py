from unittest import TestCase
from valid_parentheses import ValidParentheses


class TestValidParentheses(TestCase):

    def test_solve(self):
        s = "()"
        expected = True
        self.assertEqual(expected, ValidParentheses.solve(s))
        s = "()[]{}"
        expected = True
        self.assertEqual(expected, ValidParentheses.solve(s))
        s = "(]"
        expected = False
        self.assertEqual(expected, ValidParentheses.solve(s))
        s = "([])"
        expected = True
        self.assertEqual(expected, ValidParentheses.solve(s))
        s = "["
        expected = False
        self.assertEqual(expected, ValidParentheses.solve(s))
