import requests
import json
from StorageWriter import WriteStorage

class APIRequest:


    def __init__(self, api_key, company_key):
        self._api_key = api_key
        self._company_key = company_key
        self._url = 'https://imdb-api.com/en/API/Company/'
        self._payload = {}
        self._headers = {}
        self._movies = []

    def performRequest(self):
        start = 1
        while True:
            response = requests.request("GET", self._prepareURL(start),
                    headers=self._headers, data = self._payload)

            start += 50
            print(start)

            if response.status_code == 200:
                data = response.json()
                if data["errorMessage"] == "":
                    self._appendNewMovies(data)
            if start >= 1000 or not data["items"]:
                break;
        self._safeMovies()


    def _appendNewMovies(self, data):
        for movie in data["items"]:
            self._movies.append( (movie["title"], movie["year"]) )


    def _prepareURL(self, start):
        return self._url + self._api_key + "/" + self._company_key + "&start=" + str(start)


    def _safeMovies(self):
        writeStoreage = WriteStorage("data.csv")
        writeStoreage.writeContent(self._movies)
