from src.main.model.administrador import Administrador 
from src.main.model.cafeicultor import Cafeicultor 
import unittest
from unittest import TestCase

class AdministradorTest(TestCase):
    
    def setUp(self): 
        self.administrador = Administrador("Admin","admin@inatel.br","Admin#2020")
        self.cafeicultor = Cafeicultor("João","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")

    def test_cadastrarCafeicultor(self):
        self.administrador.cadastrarCafeicultor(self.cafeicultor)
        resposta = self.administrador.getCafeicultor(0)
        self.assertEqual("João",resposta.nomeGet()) #Fazer para todos parâmetros???
    
    def test_editarCafeicultor(self):
        self.administrador.cadastrarCafeicultor(self.cafeicultor)
        self.cafeicultorAlterado = Cafeicultor("João Pedro","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        self.administrador.editarCafeicultor(self.cafeicultorAlterado,0)
        resposta = self.administrador.getCafeicultor(0)
        self.assertEqual("João Pedro",resposta.nomeGet()) #Fazer para todos parâmetros???

    def test_excluirCafeicultor(self):
        with self.assertRaises(IndexError):
            self.administrador.cadastrarCafeicultor(self.cafeicultor)
            self.administrador.excluirCafeicultor('joao123@gmail.com',0)
            self.administrador.getCafeicultor(0)
    

if __name__ == "__main__":
    unittest.main()







