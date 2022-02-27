"""
Given lists of unsorted list of integers, merge them into one large sorted list.

Example 1
Input
lists = [[], [3, 3, 13], [], [10, 12], [], [22, 7], [3], [10]]

Output
[3, 3, 3, 7, 10, 10, 12, 13, 22]
"""

import unittest


def merge_unsorted_list(nums):
    #start writing your code here
     sum=[]
    for i in nums:
        sum=sum+i
    return sorted(sum)


# DO NOT TOUCH THE BELOW CODE
class TestMergeUnsortedList(unittest.TestCase):

    def test_01(self):
        input_nums = [[], [3, 3, 13], [], [10, 12], [], [22, 7], [3], [10]]
        output_nums = [3, 3, 3, 7, 10, 10, 12, 13, 22]

        self.assertEqual(merge_unsorted_list(input_nums), output_nums)

    def test_02(self):
        input_nums = [[98, 58, 22, 75], [3, 0, 13],
                      [80], [45, 22], [], [0, 7], [], [10]]
        output_nums = [0, 0, 3, 7, 10, 13, 22, 22, 45, 58, 75, 80, 98]

        self.assertEqual(merge_unsorted_list(input_nums), output_nums)

    def test_03(self):
        input_nums = [[]]
        output_nums = []

        self.assertEqual(merge_unsorted_list(input_nums), output_nums)

    def test_04(self):
        input_nums = [[0, 0, 0, 0, 0, 0], [3, 13],
                      [80], [45, -2, 22], [], [10, 7], [], [98, -858]]
        output_nums = [-858, -2, 0, 0, 0, 0,
                       0, 0, 3, 7, 10, 13, 22, 45, 80, 98]

        self.assertEqual(merge_unsorted_list(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
