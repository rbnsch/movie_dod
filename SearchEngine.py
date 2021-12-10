"""
File: main.py
Author: Robin Schmidt
Purpose: This class is responsible for searching for the movie requested by the user from the data basis and displaying
all matching results.
"""
from StorageReader import ReadStorage


def print_results(result):
    if not result:
        print("No matches found")
        return
    print("Oh no!", len(result), "titles found financed by the Department of Defense in data basis:\n")
    print("------------------------------------------\n")
    for movie in result:
        print(movie[0], "\t", movie[1])


class SearchEngine:

    def __init__(self):
        self._reader = None
        self._search_pattern = ""

    def check_pattern(self, search_pattern):
        self._reader = ReadStorage("data.csv")
        self._search_pattern = search_pattern
        data = self._get_data()
        results = list(filter(self._check_item_match, data))
        print_results(results)

    def _check_item_match(self, item):
        if self._search_pattern.lower() in item[0].lower():
            return True
        return False

    def _get_data(self):
        return self._reader.get_content()
