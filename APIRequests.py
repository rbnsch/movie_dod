import requests
import json
from StorageWriter import WriteStorage

url = 'https://imdb-api.com/en/API/Company/'

payload = {}
headers = {}

start = 1
api_key = ""
company_key = "co0050471"

movies = []

while True:
    requestURL = url + api_key + "/" + company_key + "&start=" + str(start)
    print(requestURL)
    response = requests.request("GET", requestURL, headers=headers, data = payload)

    start += 50

    if response.status_code == 200:
        data = response.json()
        if data["errorMessage"] == "":
            print(data["name"])
            for movie in data["items"]:
                print(movie["title"])
                print(movie["year"])
                movies.append( (movie["title"], movie["year"]) )
        if start >= 50 or not data["items"]:
            break;

writeStoreage = WriteStorage("data.csv")
writeStoreage.writeContent(movies)
