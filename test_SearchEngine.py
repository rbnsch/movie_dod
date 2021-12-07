from unittest import TestCase, main
from SearchEngine import SearchEngine
from unittest.mock import patch
from io import StringIO 
import sys


class TestAPIRequest(TestCase):
    def setUp(self):
        self.searchEngine = SearchEngine()
        self.searchEngine._searchPatter = "Movie"

    def test_checkItemMatch_True(self):
        self.assertTrue(self.searchEngine._checkItemMatch(["movie", "2020"]))
        
    def test_checkItemMatch_False(self):
        self.assertFalse(self.searchEngine._checkItemMatch(["oie", "2020"]))
        
       
    @patch('sys.stdout', new_callable=StringIO)
    def test_printer_matches(self, mock_stdout):
        expected_output = "Oh no! 1 titels found financed by the Department of Defense in data basis:\n\n------------------------------------------\n\nMovie \t 2020\n"
        self.searchEngine._printer([["Movie", "2020"]])
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_printer_no_matches(self, mock_stdout):
        expected_output = "No matches found\n"
        self.searchEngine._printer([])
        self.assertEqual(mock_stdout.getvalue(), expected_output)



if __name__ == '__main__':
    unittest.main()
