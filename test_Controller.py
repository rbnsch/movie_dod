from unittest import TestCase, main
from Controller import Controller
from unittest.mock import patch


class TestAPIRequest(TestCase):
    def setUp(self):
        self.Controller = Controller()

    @patch("SearchEngine.SearchEngine")
    def test_checkMovie(self, SearchEngine_mock):
        self.Controller._s = SearchEngine_mock
        self.Controller.checkMovie("test")
        SearchEngine_mock.checkPattern.assert_called_with("test")
        
    #@patch("APIRequests.APIRequest")
    #def test_updateDataBasis(self, APIRequest_mock):
        #self.Controller._a = APIRequest_mock
        

if __name__ == '__main__':
    unittest.main()



