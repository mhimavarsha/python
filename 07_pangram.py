# Pangram
"""
Given a string s, representing a sentence, return whether every letter (case-insensitive) of the alphabet is used at least once.

Example 1
Input
s = "A quick brown fox jumps over the lazy dog"
Output
True

Example 2
Input
s = "The jay, pig, fox, tiger and my wolves quack!"
Output
False

Explanation
This sentence is missing a "z"
"""

import unittest


def pangram(s):
    """
    Return whether every letter (case-insensitive) of the alphabet is used at least once.
    """
    s1 = "abcdefghijklmnopqrstuvwxyz"
    # s=("".join(s.split())).lower()
    s2 = ""
    for i in s:
        if i.isalpha():
            s2 = "".join([s2, i])
    if set(s1) == set(s2.lower()):
        return True
    return False

# DO NOT TOUCH THE BELOW CODE


class TestPangram(unittest.TestCase):

    def test_01(self):
        input_string = "A quick brown fox jumps over the lazy dog"

        self.assertEqual(pangram(input_string), True)

    def test_02(self):
        input_string = "The jay, pig, fox, tiger and my wolves quack!"

        self.assertEqual(pangram(input_string), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
