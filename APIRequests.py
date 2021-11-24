import requests
import json
from StorageWriter import WriteStorage
'''
url = 'https://imdb-api.com/en/API/Company/'

payload = {}
headers = {}

start = 1
api_key = ""
company_key = "co0050471"

while True:
    requestURL = url + api_key + "/" + company_key + "&start=" + str(start)
    print(requestURL)
    response = requests.request("GET", requestURL, headers=headers, data = payload)
    print(response.status_code)
    start += 50

    if response.status_code == 200:
        data = response.json()
        if data["errorMessage"] == "":
            movies = []
            print(data["name"])
            for movie in data["items"]:
                print(movie["title"])
                movies.append(movie["title"])
        if start >= 1000 or not data["items"]:
            break;
'''
movies = [ ("First", 2), ("Secodn", 3), ("Last", 3)]
print(movies)
writestorage = WriteStorage("data.csv")
writestorage.writeContent(movies)
