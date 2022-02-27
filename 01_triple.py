"""
Given a list of integers nums, return whether a number and its triple exist in the list.

Constraints
Length of nums is at most 5000.

Example 1
Input
nums = [2, 3, 10, 7, 6]
Output
True
Explanation
6 is a triple of 2

Example 2
Input
nums = [3, 4, 5]
Output
False
Explanation
There's no 9, 12, or 15.

Example 3
Input
nums = [0, 2, 0]
Output
True
Explanation
0 is a triple of 0

"""

import unittest


def number_and_its_triple(nums):
    #start writing your code here
    for i in nums:
        if i*3 in nums:
            return True
    return False

# DO NOT TOUCH THE BELOW CODE
class TestnumberAndItsTriple(unittest.TestCase):

    def test_01(self):
        input_nums = [2, 3, 10, 7, 6]

        self.assertEqual(number_and_its_triple(input_nums), True)

    def test_02(self):
        input_nums = [3, 4, 5]

        self.assertEqual(number_and_its_triple(input_nums), False)

    def test_03(self):
        input_nums = [1, 4, 5, 9, 12]

        self.assertEqual(number_and_its_triple(input_nums), True)

    def test_04(self):
        input_nums = [12, 13, 14, 15, 16, 17, 18, 19,
                      20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

        self.assertEqual(number_and_its_triple(input_nums), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
