from abc import ABC, abstractmethod

class DataStorage(ABC):

    def __init__(self, fileLocation):
        self._fileLocation = fileLocation

    def openFile(self):
        pass

    def __del__(self):
        self._file.close()
