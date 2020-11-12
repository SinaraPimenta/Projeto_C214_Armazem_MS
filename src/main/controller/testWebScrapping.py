#from main.python.controller.webScrapping import WebScrapping 
from webScrapping import WebScrapping
import unittest
from unittest import TestCase

class WebScrappingTest(TestCase):
    
    #def setUp(self): 

    def test_cotacaoCafe(self):
        esperado = 549
        obtido = WebScrapping.cotacaoCafe(self,'6','dura')  
        self.assertEqual(esperado,obtido)

if __name__ == "__main__":
    unittest.main()







