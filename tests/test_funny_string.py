import unittest
from main_code.funny_string import funnyString

class test_funnyString(unittest.TestCase):
    def test_cases_1(self):
        self.assertAlmostEqual(funnyString("acxz"), "Funny")
    def test_cases_2(self):
        self.assertAlmostEqual(funnyString("bcxz"), "Not Funny")
    def test_cases_3(self):
        self.assertAlmostEqual(funnyString("aaaa"), "Funny")
    def test_cases_4(self):
        self.assertAlmostEqual(funnyString("z"), "Funny")
    def test_cases_5(self):
        self.assertAlmostEqual(funnyString("abcdedcba"), "Funny")
    def test_cases_6(self):
        self.assertAlmostEqual(funnyString("abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"), "Funny")

test_funnyString()