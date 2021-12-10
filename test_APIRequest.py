"""
File: main.py
Author: Robin Schmidt
Purpose: This file is responsible for testing the APIRequest class using Unittest.
"""
from unittest import TestCase, main
from APIRequests import APIRequest


class TestAPIRequest(TestCase):
    def setUp(self):
        self.apiRequest = APIRequest("co0050471")
        self.apiRequest._api_key = "key_key"

    def test_prepare_url(self):
        self.assertEqual(self.apiRequest._prepare_url(1),
                         "https://imdb-api.com/en/API/Company/key_key/co0050471&start=1")

    def test_append_new_movies(self):
        data = {'id': 'co0050471&start=1', 'name': 'Department of Defense', 'items': [
            {'id': 'tt0117913', 'title': 'A Time to Kill', 'year': '(1996)',
             'image': 'https://imdb-api.com/images/original'
                      '/MV5BOWExZTg4ZWYtOTQxMieQXVyMTQxNzMzNDI@._V1_Ratio0.6800_AL_.jpg',
             'imDbRating': '7.5'}, {'id': 'tt0118480', 'title': 'Stargate SG-1', 'year': '(1997–2007)',
                                    'image': 'https://imdb-api.com/images/original'
                                             '/MV5BMTc3MjEwMTc5N15BMl5BanBnXkFtZTcwNzQ2NjQ4NA@@._V1_Ratio0.6800_AL_'
                                             '.jpg',
                                    'imDbRating': '8.4'}, ], 'errorMessage': ''}
        result = [('A Time to Kill', '(1996)'), ('Stargate SG-1', '(1997–2007)')]
        self.apiRequest._append_new_movies(data)
        self.assertEqual(self.apiRequest._movies, result)


if __name__ == '__main__':
    main()
