import sys
sys.path.append('src/main/model')
import cafeicultor 
import sacaCafe
import unittest
from bson.objectid import ObjectId
from unittest import TestCase
import pymongo

class AdministradorTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
        cls.db = cls.cliente["ArmazemMS"] 
        cls.colecao = "Teste_SacasDeCafe"
        cls.s = sacaCafe.SacaCafe("tipo 6","bebida riada",3,"","","joao123@gmail.com")
        cls.c = cafeicultor.Cafeicultor("Joao","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        cls.db.Teste_SacasDeCafe.delete_many({}) #limpar a coleção antes de fazer os testes 
    
    def test_buscarCafeBdVazio(self):
        resposta = self.c.buscarCafe(self.c.getLogin(),self.colecao)
        esperado = '<table id="tabela" class="table"><thead><tr><th scope="col">#</th><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col">Data do cadastro</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody></tbody></table>'
        
        self.assertEqual(esperado,resposta)
    
    def test_buscarCafe(self):
        self.c.cadastrarCafe(self.s,1200,"25/11/2020",self.colecao) 
        resposta = self.c.buscarCafe(self.s.loginGet(),self.colecao)
        cafe = self.c.consultaBd(self.s.loginGet(),self.colecao)
        for data in cafe:
            idC = data['_id']
        self.c.excluirCafe(ObjectId(idC),0,self.colecao)
        esperado='<table id="tabela" class="table"><thead><tr><th scope="col">#</th><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col">Data do cadastro</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody><tr><th scope="row">0</th><td>tipo 6</td><td>bebida riada</td><td>1200</td><td>3</td><td>25/11/2020</td><td><button type="button" class="btn btn-primary" id="editarCafe" onclick="venderCafe(0)">Vender</button></td><td><button type="button" class="btn btn-primary" id="editarCafe" onclick="editarCafe(0)">Editar</button></td></tr></tbody></table>'
        
        self.assertEqual(esperado,resposta)
        
        self.c.excluirCafe(ObjectId(idC),0,self.colecao)
    
    def test_cadastrarCafe(self):
        self.c.cadastrarCafe(self.s,1200,"25/11/2020",self.colecao) 
        cafe = self.c.consultaBd(self.s.loginGet(),self.colecao)
        for data in cafe:
            idC = data['_id']
        resposta = self.c.getCafe(0)
        resposta.valorSet(1200)
        resposta.dataSet('25/11/2020')

        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual(3,resposta.quantidadeGet())
        self.assertEqual("tipo 6",resposta.tipoGet())
        self.assertEqual("bebida riada",resposta.classificacaoGet())
        self.assertEqual(1200,resposta.valorGet())
        
        self.c.excluirCafe(ObjectId(idC),0,self.colecao) 
    
    
    def test_editarCafe(self):
        self.c.cadastrarCafe(self.s ,1200,'25/11/2020',self.colecao) 
        cafe = self.c.consultaBd(self.s.loginGet(),self.colecao)
        for data in cafe:
            idC = data['_id']
        self.cafeAlterado = sacaCafe.SacaCafe("tipo 6","bebida dura",5,"","","joao123@hotmail.com",idC)
        self.c.editarCafe(self.cafeAlterado,2000,'25/11/2020',0,self.colecao)
        resposta = self.c.getCafe(0)
        resposta.valorSet(2000)
        resposta.dataSet('25/11/2020')

        self.assertEqual("joao123@hotmail.com",resposta.loginGet())
        self.assertEqual(5,resposta.quantidadeGet())
        self.assertEqual("tipo 6",resposta.tipoGet())
        self.assertEqual("bebida dura",resposta.classificacaoGet())
        self.assertEqual(2000,resposta.valorGet()) 
        
        self.c.excluirCafe(idC,0,self.colecao) 
    
    def test_excluirCafe(self):
        self.c.cadastrarCafe(self.s,1200,"25/11/2020",self.colecao) 
        cafe = self.c.consultaBd(self.s.loginGet(),self.colecao)
        for data in cafe:
            idC = data['_id']

        with self.assertRaises(IndexError):
            self.c.excluirCafe(idC,0,self.colecao)
            self.c.getCafe(0)
    
if __name__ == "__main__":
    unittest.main()







