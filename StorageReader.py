from DataStorage import DataStorage
import csv

class ReadStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self._openFile()

    def _openFile(self):
        try:
            self._file = open(self._fileLocation, 'r')
            self._reader = csv.reader(self._file)
        except FileNotFoundError:
            print("Error! File data.csv not found! Please update Data Basis")
            exit()
            



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
