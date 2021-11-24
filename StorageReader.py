from DataStorage import DataStorage
import csv

class ReadStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self.openFile()

    def openFile(self):
        self.file = open(self.fileLocation, 'r')
        self.reader = csv.reader(self.file)


    def getContent(self):
        count = 0
        movies = []
        for row in self.reader:
            if count == 0:
                count += 1
            else:
                count += 1
                movies.append(row)
        return movies
