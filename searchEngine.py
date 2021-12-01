from StorageReader import ReadStorage

class SearchEngine:

    def __init__(self, searchPattern):
        self._reader = ReadStorage("data.csv")
        self._searchPatter = searchPattern

    def checkPattern(self):
        data = self._getData()
        results = list(filter(self._checkItemMatch, data))
        self._printer(results)

    def _printer(self, result):
        if not result:
            print("No matches found")
            return
        print("Oh no!", len(result), "movies found in database:i\n")
        print("------------------------------------------\n")
        for movie in result:
           print(movie[0], "\t", movie[1])


    def _checkItemMatch(self, item):
        if self._searchPatter.lower() in item[0].lower():
            return True
        return False

    def _getData(self):
        return self._reader.getContent()
