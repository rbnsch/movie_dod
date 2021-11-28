from StorageReader import ReadStorage

class SearchEngine:

    def __init__(self, searchPattern):
        self._reader = ReadStorage("data.csv")
        self._searchPatter = searchPattern

    def checkPattern(self):
        data = self._getData()
        results = list(filter(self._checkItemMatch, data))
        print(results)

    def _checkItemMatch(self, item):
        if item[0] == "Dave":
            return True
        return False

    def _getData(self):
        return self._reader.getContent()
