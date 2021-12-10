"""
File: main.py
Author: Robin Schmidt
Purpose: The abstract class defined the structure of the classes that manage the data basis.
"""
from abc import ABC


class DataStorage(ABC):

    def __init__(self, file_location):
        self._file_location = file_location

    def _open_file(self):
        pass

    def __del__(self):
        if 'self._file' in locals():
            self._file.close()
