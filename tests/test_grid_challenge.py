import unittest
from main_code.grid_challenge import gridChallenge  # แก้ไข path ตามโครงสร้างโปรเจค

class TestGridChallenge(unittest.TestCase):
    def test_all_rows_and_columns_sorted(self):
        grid = ["abc", "def", "ghi"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_columns_not_sorted_after_sorting_rows(self):
        grid = ["xyz", "uvw"]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_single_row(self):
        grid = ["cba"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_single_column_sorted(self):
        grid = ["a", "b", "c"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_single_column_unsorted(self):
        grid = ["c", "b", "a"]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_all_characters_same(self):
        grid = ["aaa", "aaa", "aaa"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_mixed_columns_one_unsorted(self):
        grid = ["abc", "def", "axz"]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_minimum_grid_size_1x1(self):
        grid = ["z"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_unsorted_rows_but_columns_sorted_after_sorting(self):
        grid = ["cba", "fed", "ihg"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_rows_sorted_but_first_column_unsorted(self):
        grid = ["mno", "abc"]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_multiple_unsorted_columns(self):
        grid = ["ab", "cd", "ea"]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_non_alpha_characters(self):
        grid = ["!ab", "c!b", "a!c"]
        self.assertEqual(gridChallenge(grid), "NO")

if __name__ == '__main__':
    unittest.main()