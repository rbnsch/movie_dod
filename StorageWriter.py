"""
File: StorageWriter.py
Author: Robin Schmidt
Purpose: This class is responsible for overwriting data in the csv file.
"""
from DataStorage import DataStorage
import csv


class WriteStorage(DataStorage):
    """
    Overwriting a csv file with new data
    Attributes
    ----------
    file_location : str
        location of the file storing the data

    Methods
    -------
    write_content(movies):
        overwrites the csv file with the provided list of titles with year
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
        self._file = open(self._file_location, 'w+')
        self._writer = csv.writer(self._file)

    def write_content(self, movies):
        """
        Writes the list of handed over titles with the years in a csv file
        :param movies: list of titles with their matching release year
        :return: none
        """
        self._writer.writerow(("Name", "Year"))
        self._writer.writerows(movies)
        print(len(movies), "items have been successfully added!")
