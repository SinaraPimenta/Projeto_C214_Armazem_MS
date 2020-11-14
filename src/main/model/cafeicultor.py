from src.main.model.usuario import Usuario

class Cafeicultor(Usuario):
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
    
    def loginGet(self):
        return super().getLogin()
    
    def senhaGet(self):
        return super().getSenha()
    
    def telefoneGet(self):
        return self.__telefone

    def cpfGet(self):
        return self.__cpf

    def cidadeGet(self):
        return self.__cidade

    def enderecoGet(self):
        return self.__endereco
    
    def agenciaGet(self):
        return self.__agencia_bancaria

    def contaGet(self):
        return self.__numero_da_conta
    
    def bancoGet(self):
        return self.__nome_do_banco

    def cadastrarVenda(self):
        print('cadastra venda')
    
    def venderCafe(self):
        print('vende o café')
    
    #def solicitarDados(self):
        #print('solicita dados')
    
