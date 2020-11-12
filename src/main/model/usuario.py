class Usuario(object):
    __nome: str
    __login: str
    __senha: str

    def __init__(self, nome="",login="", senha=""):
        self.__nome = nome
        self.__login = login
        self.__senha = senha