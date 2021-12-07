from DataStorage import DataStorage
import csv

class ReadStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self._openFile()

    def _openFile(self):
        self._file = open(self._fileLocation, 'r')
        self._reader = csv.reader(self._file)



    def getContent(self):
        count = 0
        movies = []
        for row in self._reader:
            if count == 0:
                count += 1
            else:
                count += 1
                movies.append(row)
        return movies
