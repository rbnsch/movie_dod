"""
File: StorageReader.py
Author: Robin Schmidt
Purpose: This class is responsible for reading all data from the csv file.
"""
from DataStorage import DataStorage
import csv


class ReadStorage(DataStorage):
    """
    Reading all data from a csv file and makes it available
    Attributes
    ----------
    file_location : str
        location of the file storing the data

    Methods
    -------

    get_content():
        returns the content of the csv file
    """

    def __init__(self, file_location):
        """
        Constructs the object.
        :param file_location: str
            location of the file storing the data
        """
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
        """
        Returns the content of the data basis
        :return: returns a list of titles with their matching release year
        """
        count = 0
        movies = []
        for row in self._reader:
            if count == 0:
                count += 1
            else:
                count += 1
                movies.append(row)
        return movies
