from abc import ABC, abstractmethod

class DataStorage(ABC):

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation

    def openFile(self):
        pass

    def __del__(self):
        self.file.close()
