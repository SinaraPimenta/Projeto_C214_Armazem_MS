import sys
sys.path.append('src/main/model')
import usuario
sys.path.append('src/main/controller')
import bancoDeDadosCafeicultor

#from src.main.model.usuario import Usuario
#from src.main.controller.bancoDeDadosCafeicultor import BancoDeDadosCafeicultor

class Cafeicultor(usuario.Usuario):
    bd = bancoDeDadosCafeicultor.BancoDeDadosCafeicultor()
    __telefone: str
    __cpf: str
    __cidade: str
    __endereco: str
    __agencia_bancaria: str
    __numero_da_conta: str
    __nome_do_banco: str

    def __init__(self, nome="",login="",senha="",telefone="", cpf="", cidade="", endereco="",nome_do_banco="", agencia_bancaria="",numero_da_conta=""):
        super().__init__(nome, login,senha)
        self.__telefone = telefone
        self.__cpf = cpf
        self.__cidade = cidade
        self.__endereco = endereco
        self.__agencia_bancaria = agencia_bancaria
        self.__numero_da_conta = numero_da_conta
        self.__nome_do_banco = nome_do_banco
    
    def nomeGet(self):
        return super().getNome()
    
    def nomeSet(self,nome):
        super().setNome(nome)
    
    def loginGet(self):
        return super().getLogin()
    
    def senhaGet(self):
        return super().getSenha()
    
    def telefoneGet(self):
        return self.__telefone
    
    def telefoneSet(self,telefone):
        self.__telefone = telefone

    def cpfGet(self):
        return self.__cpf

    def cidadeGet(self):
        return self.__cidade
    
    def cidadeSet(self,cidade):
        self.__cidade = cidade

    def enderecoGet(self):
        return self.__endereco
    
    def enderecoSet(self,endereco):
        self.__endereco = endereco
    
    def agenciaGet(self):
        return self.__agencia_bancaria
    
    def agenciaSet(self,agencia):
        self.__agencia_bancaria = agencia

    def contaGet(self):
        return self.__numero_da_conta

    def contaSet(self,conta):
        self.__numero_da_conta = conta
    
    def bancoGet(self):
        return self.__nome_do_banco
    
    def bancoSet(self,banco):
        self.__nome_do_banco = banco

    def atualizaCafeicultor(self,nome:str,telefone:str,endereco:str,cidade:str,banco:str,agencia:str,conta:str):
        self.nomeSet(nome)
        self.telefoneSet(telefone)
        self.enderecoSet(endereco)
        self.cidadeSet(cidade)
        self.bancoSet(banco)
        self.agenciaSet(agencia)
        self.contaSet(conta)

    def buscarCafe(self,login,colecao):
        return self.bd.buscarSacasDeCafe(login,colecao)

    def cadastrarCafe(self,cafe,valor,data,colecao):
        self.bd.cadastrarSacasDeCafe(cafe,valor,data,colecao)
        self.bd.adicionarNalistaCafe(cafe)

    def editarCafe(self,cafe,valor,data,indice,colecao):
        self.bd.alterarSacaDeCafe(cafe,valor,data,colecao)
        self.bd.substituiCafe(indice,cafe)

    def excluirCafe(self,id,indice,colecao):
        self.bd.deletarSacaDeCafe(id,colecao)
        self.bd.removerDalistaCafe(indice)
    
    def venderCafe(self,cafe,valor_novo,data,indice,colecao):
        self.bd.venderSacaDeCafe(cafe,valor_novo,data,colecao)
        self.bd.substituiCafe(indice,cafe) 
    
    def getCafe(self,indice):
        return self.bd.getCafe(indice)

    def consultaBd(self,login,colecao):
        retorno = self.bd.buscaNoBD(login,colecao)
        return retorno
    
    
    #def solicitarDados(self):
        #print('solicita dados')
    
