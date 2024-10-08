''' 
---- Problem: Roman to Integer (Roman2Int)

Problem Statement:

You are given a string representing a Roman numeral. Write a function that converts this Roman numeral into an integer. 
Roman numerals are typically written as combinations of the following symbols:

| Symbol | Value  |
|--------|--------|
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

Roman numerals are generally written from largest to smallest from left to right. 
However, in certain cases, subtractive notation is used where a smaller numeral precedes a larger numeral to indicate subtraction. 
For example:
- **IV** = 4 (5 - 1)
- **IX** = 9 (10 - 1)
- **XL** = 40 (50 - 10)
- **XC** = 90 (100 - 10)
- **CD** = 400 (500 - 100)
- **CM** = 900 (1000 - 100)

Given a valid Roman numeral, return its integer equivalent.

Example:
Input: s = "VI"
Output: 6 since (5 + 1 = 6)

Input: s = "IV"
Output: 4 since (5 - 1 = 4)
'''

# Run the test cases by running the file using the command `python <filename>.py`

import unittest

# Tips: tab is your friend, use it to auto-complete the function signature
# If you get stuck, there are comments at the bottom of the file that can help you get unstuck

def roman_to_integer(s: str) -> int:
    pass

class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        self.assertEqual(roman_to_integer("III"), 3)
        self.assertEqual(roman_to_integer("IV"), 4)
        self.assertEqual(roman_to_integer("IX"), 9)
        self.assertEqual(roman_to_integer("LVIII"), 58)
        self.assertEqual(roman_to_integer("MCMXCIV"), 1994)
        self.assertEqual(roman_to_integer("MMXXIII"), 2023)
        self.assertEqual(roman_to_integer("CDXLIV"), 444)
        self.assertEqual(roman_to_integer("CMXCIX"), 999)

if __name__ == "__main__":
    unittest.main()














# Tip 1
# Try letting CoPilot decide what to do by creating a new-line (maybe 2 new lines), starting to write a comment (# in python)
# or asking coPilot in the chat

# Tip 2
# Or asking a question to CoPilot by writing a comment
# Ex. # How do I convert a roman numeral to an integer?

# Tip 3
# You can also ask CoPilot to write the code for you by writing a comment
# Ex. # Write the code to convert a roman numeral to an integer

# Tip 4
# You can also ask CoPilot to write the code for you by writing a comment
# Ex. # Write the code to convert a roman numeral to an integer