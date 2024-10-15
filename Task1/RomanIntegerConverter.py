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
 
Problem 2: Roman to english.
Take a string with a roman numeral as input and returns the value in english language.
Use the previous function to convert the roman numeral to integer and then convert the integer to english.
'''
 
 
import unittest
 
def roman_to_integer(s: str) -> int:
    roman_to_int = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    result = 0
    prev = 0
    for char in s:
        current = roman_to_int[char]
        if prev < current:
            result += current - 2 * prev
        else:
            result += current
        prev = current
       
    return result
 
# Takes roman numeral as input and returns the value in english language
def roman_to_english(s: str) -> str:
    integer_value = roman_to_integer(s)
    result = integer_to_english(integer_value)
    # Remove leading and trailing whitespaces
    result = result.strip()
    return result
 
def integer_to_english(n: int) -> str:
    if n == 0:
        return "Zero"
    result = ""
    roman_to_int = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
        15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
        19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
        50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
        90: "Ninety", 100: "Hundred", 1000: "Thousand", 1000000: "Million",
        1000000000: "Billion"
    }
    if n >= 1000000000:
        result += integer_to_english(n // 1000000000) + " " + roman_to_int[1000000000]
        n %= 1000000000
    if n >= 1000000:
        result += integer_to_english(n // 1000000) + " " + roman_to_int[1000000]
        n %= 1000000
    if n >= 1000:
        result += integer_to_english(n // 1000) + " " + roman_to_int[1000]
        n %= 1000
    if n >= 100:
        result += integer_to_english(n // 100) + " " + roman_to_int[100]
        n %= 100
    if n >= 20:
        result += " " + roman_to_int[n // 10 * 10]
        n %= 10
    if n > 0:
        result += " " + roman_to_int[n]
    return result
 
class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        self.assertEqual(roman_to_integer("III"), 3)
        self.assertEqual(roman_to_integer("IV"), 4)
        self.assertEqual(roman_to_integer("IX"), 9)
        self.assertEqual(roman_to_integer("LVIII"), 58)
        self.assertEqual(roman_to_integer("MCMXCIV"), 1994)
        self.assertEqual(roman_to_integer("MMXXI"), 2021)
        self.assertEqual(roman_to_integer("V"), 5)
        self.assertEqual(roman_to_integer("MMXXI"), 2021)
 
    def test_roman_to_english(self):
        self.assertEqual(roman_to_english("III"), "Three")
        self.assertEqual(roman_to_english("IV"), "Four")
        self.assertEqual(roman_to_english("IX"), "Nine")
        self.assertEqual(roman_to_english("LVIII"), "Fifty Eight")
        self.assertEqual(roman_to_english("MCMXCIV"), "One Thousand Nine Hundred Ninety Four")
        self.assertEqual(roman_to_english("MMXXI"), "Two Thousand Twenty One")
        self.assertEqual(roman_to_english("V"), "Five")
        self.assertEqual(roman_to_english("MMXXI"), "Two Thousand Twenty One")
 
if __name__ == "__main__":
    unittest.main()