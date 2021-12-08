from StorageReader import ReadStorage


class SearchEngine:

    def __init__(self):
        self._reader = None
        self._searchPatter = ""

    def check_pattern(self, search_pattern):
        self._reader = ReadStorage("data.csv")
        self._searchPatter = search_pattern
        data = self._get_data()
        results = list(filter(self._check_item_match, data))
        self._printer(results)

    def _printer(self, result):
        if not result:
            print("No matches found")
            return
        print("Oh no!", len(result), "titles found financed by the Department of Defense in data basis:\n")
        print("------------------------------------------\n")
        for movie in result:
            print(movie[0], "\t", movie[1])

    def _check_item_match(self, item):
        if self._searchPatter.lower() in item[0].lower():
            return True
        return False

    def _get_data(self):
        return self._reader.get_content()
