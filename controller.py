from APIRequests import APIRequest
from SearchEngine import SearchEngine
from StorageWriter import WriteStorage

class Controller:


    def __init__(self):
        self._companyKey = "co0050471"
        self._a = APIRequest(self._companyKey)
        self.s = SearchEngine()
        

    def updateDataBasis(self, apiKey):
        print("Update data basis")
        data = self._a.performRequest(apiKey)
        self._writeData(data)
        

    def checkMovie(self, searchPattern):
        print("Check for movie:", searchPattern)
        self.s.checkPattern(searchPattern)
        
    def _writeData(self, data):
        self.writeStoreage = WriteStorage("data.csv")
        self.writeStoreage.writeContent(data)
        
