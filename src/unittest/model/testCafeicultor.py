import sys
sys.path.append('src/main/model')
import cafeicultor 
import sacaCafe
import unittest
from bson.objectid import ObjectId
from unittest import TestCase
import pymongo
sys.path.append('src/main/controller')
import mediador
import bancoDeDados

class AdministradorTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        #Configuração do BD:
        cls.cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
        cls.db = cls.cliente["ArmazemMS"] 
        cls.colecao = "Teste_SacasDeCafe"
        cls.db.Teste_SacasDeCafe.delete_many({}) #limpar a coleção antes de fazer os testes 
        #Objetos:
        cls.s = sacaCafe.SacaCafe("tipo 6","bebida riada",3,1200,"25/11/2020",0,"joao123@gmail.com")
        cls.c = cafeicultor.Cafeicultor("Joao","joao123@gmail.com","teste123","3534-9965","15923678941","Itamogi","Sítio A","Banco do Brasil","8218-X","895-9")
        cls.b = bancoDeDados.BancoDeDados()
        
    def test_buscarCafeBdVazio(self):
        #Buscar café/Resposta:
        m = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        resposta = self.c.buscarCafe(m)
        #Valor esperado:
        esperado = '<table id="tabela" class="table"><thead><tr><th scope="col">#</th><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col">Data do cadastro</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody></tbody></table>'
        #Comparação:
        self.assertEqual(esperado,resposta)

    def test_buscarCafe(self):
        #Cadastrar café:
        m = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.cadastrarCafe(m) 
        #Buscar café/Resposta:
        m1 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        resposta = self.c.buscarCafe(m1)
        #Obter _id gerado pelo MongoDB: 
        m2 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m2)
        for data in cafe:
            idC = data['_id']
        self.s.idSet(idC)
        #Excluir café:
        m3 = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.excluirCafe(m3)
        esperado='<table id="tabela" class="table"><thead><tr><th scope="col">#</th><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col">Data do cadastro</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody><tr><th scope="row">0</th><td>tipo 6</td><td>bebida riada</td><td>1200</td><td>3</td><td>25/11/2020</td><td><button type="button" class="btn btn-primary" id="editarCafe" onclick="venderCafe(0)">Vender</button></td><td><button type="button" class="btn btn-primary" id="editarCafe" onclick="editarCafe(0)">Editar</button></td></tr></tbody></table>'
        #Comparação:
        self.assertEqual(esperado,resposta)
        #Obter _id gerado pelo MongoDB: 
        m4 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m4)
        for data in cafe:
            idC = data['_id']
        self.s.idSet(idC)
        #Excluir café:
        m5 = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.excluirCafe(m5)

    def test_cadastrarCafe(self):
        #Cadastrar café:
        m = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.cadastrarCafe(m) 
        #Obter café/Resposta:
        m2 = mediador.MediadorDoCafeicultor(self.colecao,self.b,indice=0)
        resposta = self.c.getCafe(m2)
        #Comparações:
        self.assertEqual("joao123@gmail.com",resposta.loginGet())
        self.assertEqual(3,resposta.quantidadeGet())
        self.assertEqual("tipo 6",resposta.tipoGet())
        self.assertEqual("bebida riada",resposta.classificacaoGet())
        self.assertEqual(1200,resposta.valorGet())
        self.assertEqual('25/11/2020',resposta.dataGet())
        #Obter _id gerado pelo MongoDB: 
        m3 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m3)
        for data in cafe:
            idC = data['_id']
        self.s.idSet(idC)
        #Excluir café:
        m4 = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.excluirCafe(m4)

    def test_editarCafe(self):
        #Cadastrar café:
        m = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.cadastrarCafe(m)
        #Obter _id gerado pelo MongoDB: 
        m2 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m2)
        for data in cafe:
            idC = data['_id']
        #Novo café:
        self.cafeAlterado = sacaCafe.SacaCafe("tipo 6","bebida dura",5,2000,"28/11/2020",0,"joao123@hotmail.com",idC)
        #Editar café:
        m3= mediador.MediadorDoCafeicultor(self.colecao,self.b,self.cafeAlterado)
        self.c.editarCafe(m3)
        #Obter café/Resposta:
        m4 = mediador.MediadorDoCafeicultor(self.colecao,self.b,indice=0)
        resposta = self.c.getCafe(m4)
        #Comparações:
        self.assertEqual("joao123@hotmail.com",resposta.loginGet())
        self.assertEqual(5,resposta.quantidadeGet())
        self.assertEqual("tipo 6",resposta.tipoGet())
        self.assertEqual("bebida dura",resposta.classificacaoGet())
        self.assertEqual(2000,resposta.valorGet())
        self.assertEqual("28/11/2020",resposta.dataGet())
        #Obter _id gerado pelo MongoDB: 
        m5 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m5)
        for data in cafe:
            idC = data['_id']
        self.s.idSet(idC)
        #Excluir café:
        m6 = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.excluirCafe(m6)

    def test_excluirCafeicultor(self):
        #Cadastrar café:
        m = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.cadastrarCafe(m)
        #Obter _id gerado pelo MongoDB: 
        m1 = mediador.MediadorDoCafeicultor(self.colecao,self.b,login=self.c.loginGet())
        cafe = self.c.consultaBd(m1)
        for data in cafe:
            idC = data['_id']
        self.s.idSet(idC)
        #Excluir café:
        m2 = mediador.MediadorDoCafeicultor(self.colecao,self.b,self.s)
        self.c.excluirCafe(m2)
        #Obter café:
        m3 = mediador.MediadorDoCafeicultor(self.colecao,self.b,indice=0)
        with self.assertRaises(IndexError):
            self.c.getCafe(m3)
    
if __name__ == "__main__":
    unittest.main()







