from main.python.controller.webScrapping import WebScrapping 

import unittest
from unittest import TestCase

class WebScrappingTest(TestCase):
    
    #def setUp(self): 

    def test_cotacaoCafe(self):
        esperado = 'B/C, tipo 6, bebida dura, 20/21 (livre de impostos)'
        obtido = WebScrapping.cotacaoCafe(self,'6','dura')  
        self.assertEqual(esperado,obtido)

if __name__ == "__main__":
    unittest.main()







