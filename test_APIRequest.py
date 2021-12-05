from unittest import TestCase, main
from APIRequests import APIRequest
from unittest.mock import patch


class TestAPIRequest(TestCase):
    def setUp(self):
        self.apiRequest = APIRequest("keykey", "co0050471")

    def test_prepareURL(self):
      self.assertEqual(self.apiRequest._prepareURL(1),
      "https://imdb-api.com/en/API/Company/keykey/co0050471&start=1")

    def test_appendNewMovies(self):
        data = {'id': 'co0050471&start=1', 'name': 'Department of Defense', 'items': [{'id': 'tt0117913', 'title': 'A Time to Kill', 'year': '(1996)', 'image': 'https://imdb-api.com/images/original/MV5BOWExZTg4ZWYtOTQxMi00YWZkLTkxYzgtOTg1MTUxNzNiNDcxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_Ratio0.6800_AL_.jpg', 'imDbRating': '7.5'}, {'id': 'tt0118480', 'title': 'Stargate SG-1', 'year': '(1997–2007)', 'image': 'https://imdb-api.com/images/original/MV5BMTc3MjEwMTc5N15BMl5BanBnXkFtZTcwNzQ2NjQ4NA@@._V1_Ratio0.6800_AL_.jpg', 'imDbRating': '8.4'}, ], 'errorMessage': ''}
        result = [('A Time to Kill', '(1996)'), ('Stargate SG-1', '(1997–2007)')]
        self.apiRequest._appendNewMovies(data)
        self.assertEqual(self.apiRequest._movies, result)

    @patch("StorageWriter.WriteStorage")
    def test_safeMovies(self, WriteStorage_mock):
        self.apiRequest.writeStoreage = WriteStorage_mock
        self.apiRequest._safeMovies()
        WriteStorage_mock.writeContent.assert_called_once()

if __name__ == '__main__':
    main()


