from DataStorage import DataStorage
import csv

class ReadStorage(DataStorage):

    def __init__(self, fileLocation):
        super().__init__(fileLocation)
        self.openFile()

    def openFile(self):
        self.file = open(self.fileLocation, 'r')
        self.reader = csv.reader(self.file)


    def readContent(self):
        for lines in self.reader:
            print(lines)
