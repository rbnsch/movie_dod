"""
File: main.py
Author: Robin Schmidt
Purpose: This file is responsible for testing the APIRequest class using Unittest.
"""
from unittest import TestCase, main
from Controller import Controller
from unittest.mock import patch


class TestAPIRequest(TestCase):
    def setUp(self):
        self.Controller = Controller()

    @patch("SearchEngine.SearchEngine")
    def test_check_movie(self, search_engine_mock):
        self.Controller._s = search_engine_mock
        self.Controller.check_movie("test")
        search_engine_mock.check_pattern.assert_called_with("test")


if __name__ == '__main__':
    main()
