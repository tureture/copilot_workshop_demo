'''
Valid Parentheses Problem

Problem Statement
Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False
'''

# Run the test cases by running the file using the command `python <filename>.py`

import unittest

def valid_paranthesis(s: str) -> bool:
    pass

# Tips: tab is your friend, use it to auto-complete the function signature

class TestValidParanthesis(unittest.TestCase):
    def test_valid_paranthesis(self):
        self.assertEqual(valid_paranthesis("()"), True)
        self.assertEqual(valid_paranthesis("()[]{}"), True)
        self.assertEqual(valid_paranthesis("(]"), False)
        self.assertEqual(valid_paranthesis("([)]"), False)
        self.assertEqual(valid_paranthesis("{[]}"), True)
        self.assertEqual(valid_paranthesis("]"), False)

if __name__ == "__main__":
    unittest.main()