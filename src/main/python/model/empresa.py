
class Empresa(object):
    __nome:str
    __telefone:str
    __cnpj:str
    __admin:object
    __cafeicultores = []

    def __init__(self, admin, cafeicultores, nome="",telefone="", cnpj=""):
        self.__nome = nome
        self.__telefone = telefone
        self.__cnpj = cnpj
        self.__admin = admin
        self.__cafeicultores = cafeicultores

    def adicionarAdministrador(self):
        print('adicionarAdministrador')

    def exibirDadosDaEmpresa(self):
        print('exibirDadosDaEmpresa')