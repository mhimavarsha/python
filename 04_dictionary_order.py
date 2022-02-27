"""
Given a list of strings, arrange the list in the dictionary order of the strings without using predefined functions.

Example 1
Input
input_list = ["Z", "X", "D", "F", "Y", "A", "K", "V", "v"]
Output
output_list = ["A", "D", "F", "K", "V", "X", "Y", "Z", "v"]

Constraints: Ordering is based on ASCII values.

"""

import unittest


def dictionary_order(input_list):
    #start writing your code here
    return sorted(input_list)


# DO NOT TOUCH THE BELOW CODE
class TestDictionaryOrder(unittest.TestCase):

    def test_01(self):
        input_list = ["GITAM", "Technolgy", "Visakhapatnam", "Institute"]
        output_list = ["GITAM", "Institute", "Technolgy", "Visakhapatnam"]

        self.assertEqual(dictionary_order(input_list), output_list)

    def test_02(self):
        input_list = ["welcomes", "you", "gitam", "bengaluru"]
        output_list = ["bengaluru", "gitam", "welcomes", "you"]

        self.assertEqual(dictionary_order(input_list), output_list)

    def test_03(self):
        input_list = ["Hyderabad", "Amaravathi", "VisakhApatnam", "Bengaluru", "Chennai", "Deharadun",
                      "Gangtok", "Trivandrum", "Aizwal", "Itanagar", "New Delhi", "Leh", "ChandigarH"]
        output_list = ["Aizwal", "Amaravathi", "Bengaluru", "ChandigarH", "Chennai",
                       "Deharadun", "Gangtok", "Hyderabad", "Itanagar", "Leh", "New Delhi", "Trivandrum", "VisakhApatnam"]

        self.assertEqual(dictionary_order(input_list), output_list)

    def test_04(self):
        input_list = ["Z", "X", "D", "F", "Y", "A", "K", "V", "v"]
        output_list = ["A", "D", "F", "K", "V", "X", "Y", "Z", "v"]

        self.assertEqual(dictionary_order(input_list), output_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)
