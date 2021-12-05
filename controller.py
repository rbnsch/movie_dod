from APIRequests import APIRequest
from searchEngine import SearchEngine

class Controller:


    def __init__(self):
        self._companyKey = "co0050471"


    def updateDataBasis(self, apiKey):
        print("Update data basis")
        a = APIRequest(apiKey,self._companyKey)
        a.performRequest()

    def checkMovie(self, searchPattern):
        print("Check for movie:", searchPattern)
        s = SearchEngine(searchPattern)
        s.checkPattern()

