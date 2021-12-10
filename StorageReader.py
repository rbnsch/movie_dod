"""
File: main.py
Author: Robin Schmidt
Purpose: This class is responsible for reading all data from the csv file.
"""
from DataStorage import DataStorage
import csv


class ReadStorage(DataStorage):

    def __init__(self, file_location):
        super().__init__(file_location)
        self._open_file()

    def _open_file(self):
        try:
            self._file = open(self._file_location, 'r')
            self._reader = csv.reader(self._file)
        except FileNotFoundError:
            print("Error! File data.csv not found! Please update Data Basis")
            exit()

    def get_content(self):
        count = 0
        movies = []
        for row in self._reader:
            if count == 0:
                count += 1
            else:
                count += 1
                movies.append(row)
        return movies
