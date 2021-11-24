from DataStorage import DataStorage
import csv

class WriteStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self.openFile()

    def openFile(self):
        self.file = open(self.fileLocation, 'w+')
        self.writer = csv.writer(self.file)


    def writeContent(self, movies):
        print(movies)
        self.writer.writerow(("Name", "Year"))
        self.writer.writerows(movies)
