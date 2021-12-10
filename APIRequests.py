"""
File: APIRequests.py
Author: Robin Schmidt
Purpose: This class is responsible for fetching all titles from the IMDB
database that have been supported by the Department of defense.
"""
import requests


class APIRequest:
    """
    Performs API requests to the IMBD API, and fetches titles that have been supported by a given company.

    Attributes
    ----------
    company_key : str
        key of the company to fetch the movies

    Methods
    -------

    perform_request(api_key):
        Performs the request.
    """

    def __init__(self, company_key):
        """
        Constructs the object.

        :param company_key: str
            key of the company to fetch the movies
        """
        self._api_key = ""
        self._company_key = company_key
        self._url = 'https://imdb-api.com/en/API/Company/'
        self._movies = []

    def perform_request(self, api_key):
        """
        Performs the request.
        :param api_key: str
            api key needed to perform the request
        :return:
            returns a list of titles with their matching release year
        """
        self._api_key = api_key
        start = 1
        print("Perform Request. Please wait...")
        while True:
            response = requests.request("GET", self._prepare_url(start))
            start += 50
            if response.status_code == 200:
                data = response.json()
                if data["errorMessage"] == "":
                    self._append_new_movies(data)
            if start >= 1000 or not data["items"]:
                break
        if not self._movies:
            print("\nSomething went wrong!")
            print("Please check your API Key")
            exit()
        return self._movies

    def _append_new_movies(self, data):
        for movie in data["items"]:
            self._movies.append((movie["title"], movie["year"]))

    def _prepare_url(self, start):
        return self._url + self._api_key + "/" + self._company_key + "&start=" + str(start)
