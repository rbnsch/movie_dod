from DataStorage import DataStorage
import csv

class WriteStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self._openFile()

    def _openFile(self):
        self._file = open(self._fileLocation, 'w+')
        self._writer = csv.writer(self._file)


    def writeContent(self, movies):
        self._writer.writerow(("Name", "Year"))
        self._writer.writerows(movies)
        print(len(movies), "items have been sucessfully added!")
