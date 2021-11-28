import requests
import json
from StorageWriter import WriteStorage

class APIRequest:

    url = 'https://imdb-api.com/en/API/Company/'

    payload = {}
    headers = {}

    movies = []

    def __init__(self, api_key, company_key):
        self._api_key = api_key
        self._company_key = company_key

    def performRequest(self):
        start = 1
        while True:
            response = requests.request("GET", self.prepareURL(start),
                    headers=APIRequest.headers, data = APIRequest.payload)

            start += 50

            if response.status_code == 200:
                data = response.json()
                if data["errorMessage"] == "":
                    for movie in data["items"]:
                        APIRequest.movies.append( (movie["title"], movie["year"]) )
                if start >= 1000 or not data["items"]:
                    break;
        self.safeMovies()

    def prepareURL(self, start):
        return APIRequest.url + self._api_key + "/" + self._company_key + "&start=" + str(start)


    def safeMovies(self):
        writeStoreage = WriteStorage("data.csv")
        writeStoreage.writeContent(APIRequest.movies)
