"""
File: Controller.py
Author: Robin Schmidt
Purpose: This class is responsible for passing the task requested by the user to the appropriate classes.
"""
from APIRequests import APIRequest
from SearchEngine import SearchEngine
from StorageWriter import WriteStorage


def write_data(data):
    """
    Controls the overwriting of the current data basis
    :param data:
        List of tupels with Name and Year of a title
    :return: None
    """
    write_storage = WriteStorage("data.csv")
    write_storage.write_content(data)


class Controller:
    """
    Executes the task requested by the user.

    Attributes
    ----------
    None

    Methods
    -------

    update_data_basis(api_key):
        Performs the update of the data basis

    check_movie(search_pattern):
        Checks if the entered pattern of the user is present in the data base.
    """

    def __init__(self):
        """
        Constructs the object.
        """
        self._companyKey = "co0050471"
        self._a = APIRequest(self._companyKey)
        self._s = SearchEngine()

    def update_data_basis(self, api_key):
        """
        Performs the update of the data basis
        :param api_key: str
            api key needed to perform the request
        :return: none
        """
        print("Update data basis")
        data = self._a.perform_request(api_key)
        write_data(data)

    def check_movie(self, search_pattern):
        """
        Checks if the entered pattern of the user is present in the data base.
        :param search_pattern: str
            Pattern to be checked if it is in the data basis
        :return: none
        """
        print("Check for movie:", search_pattern)
        self._s.check_pattern(search_pattern)
