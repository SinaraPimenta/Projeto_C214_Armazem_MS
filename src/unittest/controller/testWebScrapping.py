#from src.main.controller.webScrapping import WebScrapping 
import sys
sys.path.append('src/main/controller/exception')
import exception
sys.path.append('src/main/controller')
import webScrapping
import unittest
import requests
import nose.tools
from unittest import TestCase
from unittest.mock import patch,Mock

class WebScrappingTest(TestCase):

    def test_cotacaoCafe(self):
        mock = Mock()
        mock.webScrapping.WebScrapping.cotacaoCafe()
        mock.webScrapping.WebScrapping.cotacaoCafe.assert_called_once()

    def test_exception_webScrapping(self):
        with patch.object(requests,"get") as get_mock:
            with nose.tools.assert_raises(exception.RequestException):
                get_mock.side_effect = exception.RequestException
                webScrapping.WebScrapping.cotacaoCafe(self,'','')

if __name__ == "__main__":
    unittest.main()








