"""
File: main.py
Author: Robin Schmidt
Purpose: This file is responsible for testing the APIRequest class using Unittest.
"""
from unittest import TestCase, main
from SearchEngine import SearchEngine, print_results
from unittest.mock import patch
from io import StringIO


class TestAPIRequest(TestCase):
    def setUp(self):
        self.searchEngine = SearchEngine()
        self.searchEngine._search_pattern = "Movie"

    def test_check_item_match_true(self):
        self.assertTrue(self.searchEngine._check_item_match(["movie", "2020"]))

    def test_check_item_match_false(self):
        self.assertFalse(self.searchEngine._check_item_match(["oie", "2020"]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_printer_matches(self, mock_stdout):
        expected_output = "Oh no! 1 titles found financed by the Department of Defense in data " \
                          "basis:\n\n------------------------------------------\n\nMovie \t 2020\n"
        print_results([["Movie", "2020"]])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_printer_no_matches(self, mock_stdout):
        expected_output = "No matches found\n"
        print_results([])
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    main()
