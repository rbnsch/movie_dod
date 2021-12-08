import requests


class APIRequest:

    def __init__(self, company_key):
        self._api_key = ""
        self._company_key = company_key
        self._url = 'https://imdb-api.com/en/API/Company/'
        self._movies = []

    def perform_request(self, api_key):
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
            if start >= 10 or not data["items"]:
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
