import unittest
from main_code.caesar_cipher_1 import caesarCipher  # แก้ไข path ตามโครงสร้างโปรเจค

class TestCaesarCipher(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
    
    def test_case_2(self):
        self.assertEqual(caesarCipher("XYZ", 2), "ZAB")
    
    def test_case_3(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")
    
    def test_case_4(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")
    
    def test_case_5(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")
    
    def test_case_6(self):
        self.assertEqual(caesarCipher("abc", 27), "bcd")
    
    def test_case_7(self):
        self.assertEqual(caesarCipher("a!b c", 1), "b!c d")
    
    def test_case_8(self):
        self.assertEqual(caesarCipher("aBc", 2), "cDe")
    
    def test_case_9(self):
        self.assertEqual(caesarCipher("", 5), "")
    
    def test_case_10(self):
        self.assertEqual(caesarCipher("123!@#", 4), "123!@#")
    
    def test_case_11(self):
        self.assertEqual(caesarCipher("abc", -1), "zab")
    
    def test_case_12(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = "fghijklmnopqrstuvwxyzabcde"
        self.assertEqual(caesarCipher(s, 5), expected)
    
    def test_case_13(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected = "FGHIJKLMNOPQRSTUVWXYZABCDE"
        self.assertEqual(caesarCipher(s, 5), expected)
    
    def test_case_14(self):
        self.assertEqual(caesarCipher("Hello, World!", 3), "Khoor, Zruog!")
    
    def test_case_15(self):
        self.assertEqual(caesarCipher("abcXYZ", 0), "abcXYZ")

if __name__ == '__main__':
    unittest.main()