"""
File: DataStorage.py
Author: Robin Schmidt
Purpose: The abstract class defined the structure of the classes that manage the data basis.
"""
from abc import ABC


class DataStorage(ABC):
    """
    This abstract class defines the structure of the classes that manage the data basis.

    Attributes
    ----------
    file_location : str
        location of the file storing the data

    Methods
    -------

    none
    """

    def __init__(self, file_location):
        """
        :param file_location: str
            location of the file storing the data
        """
        self._file_location = file_location

    def _open_file(self):
        pass

    def __del__(self):
        """
        Closes the file when the object is destroyed
        :return: none
        """
        if 'self._file' in locals():
            self._file.close()
