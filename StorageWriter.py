from DataStorage import DataStorage
import csv


class WriteStorage(DataStorage):

    def __init__(self, file_location):
        super().__init__(file_location)
        self._open_file()

    def _open_file(self):
        self._file = open(self._file_location, 'w+')
        self._writer = csv.writer(self._file)

    def write_content(self, movies):
        self._writer.writerow(("Name", "Year"))
        self._writer.writerows(movies)
        print(len(movies), "items have been successfully added!")
