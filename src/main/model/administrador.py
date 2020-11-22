from src.main.model.usuario import Usuario
from src.main.controller.bancoDeDados import BancoDeDados

class Administrador(Usuario):
    bd = BancoDeDados()
    
    def __init__(self,  nome="",login="", senha=""):
        super().__init__(nome, login,senha)

    def buscarCafeicultores(self):
        return self.bd.buscarCafeicultores()
    
    def cadastrarCafeicultor(self,cafeicultor):
        self.bd.cadastrarCafeicultor(cafeicultor)
        self.bd.adicionarNalistaCafeicultor(cafeicultor)

    def editarCafeicultor(self,cafeicultor,indice):
        self.bd.alterarDadosDoCafeicultor(cafeicultor)
        self.bd.substituiCafeicultor(indice,cafeicultor)

    def excluirCafeicultor(self,login,indice):
        self.bd.deletarCafeicultor(login)
        self.bd.removerDalistaCafeicultor(indice)

    def getCafeicultor(self,indice):
        return self.bd.getCafeicultor(indice)