# Numeronym
"""
Given a string s with length greater than 2, return a new string where the first and last letter are the same, but the letters in between are replaced by their length.

Example 1
Input
s = "croneberry"
Output
"c8y"

Example 2
Input
s = "extracurricular"
Output
"e13r"

"""
import unittest


def numeronym(s):
    #start writing your code here
    a=str(s[0])+str(len(s[1:len(s)-1]))+str(s[len(s)-1])
    return a

# DO NOT TOUCH THE BELOW CODE


class TestNumeronym(unittest.TestCase):

    def test_01(self):
        input_nums = "extracurricular"

        self.assertEqual(numeronym(input_nums), "e13r")

    def test_02(self):
        input_nums = "croneberry"

        self.assertEqual(numeronym(input_nums), "c8y")


if __name__ == '__main__':
    unittest.main(verbosity=2)
