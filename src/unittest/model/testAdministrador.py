import sys
sys.path.append('src/main/model')
import administrador 
import cafeicultor 
import unittest
from unittest import TestCase
import pymongo

class AdministradorTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
        cls.db = cls.cliente["ArmazemMS"] 
        cls.colecao = "Teste_Usuarios"
        cls.a = administrador.Administrador("Admin","admin@inatel.br","Admin#2020")
        cls.c = cafeicultor.Cafeicultor("Joao","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        cls.db.Teste_Usuarios.delete_many({}) #limpar a coleção antes de fazer os testes 

    def test_buscarCafeicultorBdVazio(self):
        resposta = self.a.buscarCafeicultores(self.colecao)
        esperado = '<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody></tbody></table>'
        self.assertEqual(esperado,resposta)

    def test_buscarCafeicultor(self):
        self.a.cadastrarCafeicultor(self.c,self.colecao) 
        resposta = self.a.buscarCafeicultores(self.colecao)
        self.a.excluirCafeicultor('joao123@gmail.com',0,self.colecao)
        esperado='<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody><tr><th scope="row">0</th><td class="nome">Joao</td><td >3534-9965</td><td><button type="button" class="btn btn-primary" id="verCafeicultor" onclick="verCafeicultor(0)">Ver</button></td><td><button type="button" class="btn btn-primary" id="editarCafeicultor" onclick="editarCafeicultor(0)">Editar</button></td> </tr></tbody></table>'
        self.assertEqual(esperado,resposta)
        self.a.excluirCafeicultor('joao123@gmail.com',0,self.colecao)

    def test_cadastrarCafeicultor(self):
        self.a.cadastrarCafeicultor(self.c,self.colecao) 
        resposta = self.a.getCafeicultor(0)
        self.assertEqual("Joao",resposta.nomeGet()) 
        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual("teste123",resposta.senhaGet()) 
        self.assertEqual("3534-9965",resposta.telefoneGet())
        self.assertEqual("15923678941",resposta.cpfGet())
        self.assertEqual("Itamogi",resposta.cidadeGet())
        self.assertEqual("Sítio A",resposta.enderecoGet())
        self.assertEqual("Banco do Brasil",resposta.bancoGet()) 
        self.assertEqual("8218-X",resposta.agenciaGet()) 
        self.assertEqual("895-9",resposta.contaGet()) 
        self.a.excluirCafeicultor('joao123@gmail.com',0,self.colecao) 

    def test_editarCafeicultor(self):
        self.a.cadastrarCafeicultor(self.c,self.colecao) 
        self.cafeicultorAlterado = cafeicultor.Cafeicultor("Joao Pedro","joao123@gmail.com","teste123","3534-9965","15923678941","Pouso Alegre","Sítio A","Bradesco","8156-0","1234-9")
        self.a.editarCafeicultor(self.cafeicultorAlterado,0,self.colecao)
        resposta = self.a.getCafeicultor(0)
        self.assertEqual("Joao Pedro",resposta.nomeGet()) 
        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual("teste123",resposta.senhaGet()) 
        self.assertEqual("3534-9965",resposta.telefoneGet())
        self.assertEqual("15923678941",resposta.cpfGet())
        self.assertEqual("Pouso Alegre",resposta.cidadeGet())
        self.assertEqual("Sítio A",resposta.enderecoGet())
        self.assertEqual("Bradesco",resposta.bancoGet()) 
        self.assertEqual("8156-0",resposta.agenciaGet()) 
        self.assertEqual("1234-9",resposta.contaGet()) 
        self.a.excluirCafeicultor('joao123@gmail.com',0,self.colecao) 

    def test_excluirCafeicultor(self):
        self.a.cadastrarCafeicultor(self.c,self.colecao) 
        with self.assertRaises(IndexError):
            self.a.excluirCafeicultor('joao123@gmail.com',0,self.colecao)
            self.a.getCafeicultor(0)

if __name__ == "__main__":
    unittest.main()







