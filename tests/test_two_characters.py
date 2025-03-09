import unittest
from main_code.two_characters import alternate  # แก้ไขตามตำแหน่งที่เก็บฟังก์ชันจริง

class TestAlternateFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)
    
    def test_single_character(self):
        self.assertEqual(alternate("a"), 0)
    
    def test_all_same_characters(self):
        self.assertEqual(alternate("aaaaa"), 0)
    
    def test_two_alternating_even(self):
        self.assertEqual(alternate("ababab"), 6)
    
    def test_two_alternating_odd(self):
        self.assertEqual(alternate("ababa"), 5)
    
    def test_valid_pair_with_others(self):
        self.assertEqual(alternate("abcab"), 4)
    
    def test_multiple_pairs_same_max(self):
        self.assertEqual(alternate("abacbc"), 4)
    
    def test_non_adjacent_valid(self):
        self.assertEqual(alternate("abxyzcdab"), 4)
    
    def test_case_sensitivity(self):
        self.assertEqual(alternate("AaBb"), 2)
    
    def test_no_valid_pairs(self):
        self.assertEqual(alternate("aaabbb"), 0)
    
    def test_interrupted_alternation(self):
        self.assertEqual(alternate("abba"), 0)
    
    def test_mix_valid_invalid_pairs(self):
        self.assertEqual(alternate("abcdcba"), 3)
    
    def test_all_unique_characters(self):
        self.assertEqual(alternate("abcde"), 2)

if __name__ == '__main__':
    unittest.main()