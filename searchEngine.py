from StorageReader import ReadStorage

class SearchEngine:

    def __init__(self):
        self._reader = ReadStorage("data.csv")

    def checkPattern(self, searchPattern):
        data = self._getData()
        results = list(filter(self._checkItemMatch, data))
        print(results)

    def _checkItemMatch(self, item):
        if item[0] == "Dave":
            return True
        return False

    def _getData(self):
        return self._reader.getContent()
