from abc import ABC, abstractmethod


class DataStorage(ABC):

    def __init__(self, file_location):
        self._file_location = file_location

    # @abstractmethod
    def _open_file(self):
        pass

    def __del__(self):
        if 'self._file' in locals():
            self._file.close()
