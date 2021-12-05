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
        self.writeStoreage = WriteStorage("data.csv")

    def performRequest(self):
        start = 1
        print("Perform Request. Please wait...")
        while True:
            response = requests.request("GET", self._prepareURL(start),
                    headers=self._headers, data = self._payload)
            start += 50
            if response.status_code == 200:
                data = response.json()
                if data["errorMessage"] == "":
                    self._appendNewMovies(data)
            if start >= 10 or not data["items"]:
                break;
        if not self._movies:
            print("\nSomething went wrong!")
            print("Please check your API Key")
            return
        self._safeMovies()

    def _appendNewMovies(self, data):
        for movie in data["items"]:
            self._movies.append( (movie["title"], movie["year"]) )


    def _prepareURL(self, start):
        return self._url + self._api_key + "/" + self._company_key + "&start=" + str(start)


    def _safeMovies(self):
        self.writeStoreage.writeContent(self._movies)
