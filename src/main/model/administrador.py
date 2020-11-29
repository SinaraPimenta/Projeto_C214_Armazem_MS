import sys
sys.path.append('src/main/model')
import usuario
sys.path.append('src/main/controller')
import bancoDeDados
#from src.main.model.usuario import Usuario
#from src.main.controller.bancoDeDadosAdmin import BancoDeDadosAdmin

class Administrador(usuario.Usuario):
    bd = bancoDeDados.BancoDeDados()
    
    def __init__(self,  nome="",login="", senha=""):
        super().__init__(nome, login,senha)

    def buscarCafeicultores(self,colecao):
        return self.bd.buscarCafeicultores(colecao)
    
    def cadastrarCafeicultor(self,cafeicultor,colecao):
        self.bd.cadastrarCafeicultor(cafeicultor,colecao)
        self.bd.adicionarNalistaCafeicultor(cafeicultor)

    def editarCafeicultor(self,cafeicultor,indice,colecao):
        self.bd.alterarDadosDoCafeicultor(cafeicultor,colecao)
        self.bd.substituiCafeicultor(indice,cafeicultor)

    def excluirCafeicultor(self,login,indice,colecao):
        self.bd.deletarCafeicultor(login,colecao)
        self.bd.removerDalistaCafeicultor(indice)

    def getCafeicultor(self,indice):
        return self.bd.getCafeicultor(indice)