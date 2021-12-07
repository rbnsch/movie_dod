from abc import ABC, abstractmethod

class DataStorage(ABC):

    def __init__(self, fileLocation):
        self._fileLocation = fileLocation

    def openFile(self):
        pass

    def __del__(self):
        if 'self._file' in locals():
            self._file.close()
