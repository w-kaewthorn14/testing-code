import unittest
from main_code.alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternatingCharacters("AAAAA"), 4)
    
    def test_case_2(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
    
    def test_case_3(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
    
    def test_case_4(self):
        self.assertEqual(alternatingCharacters("A"), 0)
    
    def test_case_5(self):
        self.assertEqual(alternatingCharacters("AA"), 1)
    
    def test_case_6(self):
        self.assertEqual(alternatingCharacters("ABBAABBB"), 4)
    
    def test_case_7(self):
        self.assertEqual(alternatingCharacters(""), 0)
    
    def test_case_8(self):
        self.assertEqual(alternatingCharacters("AB"), 0)

if __name__ == '__main__':
    unittest.main()