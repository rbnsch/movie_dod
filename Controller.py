"""
File: main.py
Author: Robin Schmidt
Purpose: This class is responsible for passing the task requested by the user to the appropriate classes.
"""
from APIRequests import APIRequest
from SearchEngine import SearchEngine
from StorageWriter import WriteStorage


def _write_data(data):
    write_storage = WriteStorage("data.csv")
    write_storage.write_content(data)


class Controller:

    def __init__(self):
        self._companyKey = "co0050471"
        self._a = APIRequest(self._companyKey)
        self._s = SearchEngine()

    def update_data_basis(self, api_key):
        print("Update data basis")
        data = self._a.perform_request(api_key)
        _write_data(data)

    def check_movie(self, search_pattern):
        print("Check for movie:", search_pattern)
        self._s.check_pattern(search_pattern)
