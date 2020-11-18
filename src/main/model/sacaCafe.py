class SacaCafe(object):
    __id:str
    __login:str
    __tipo:str
    __classificacaoBebida:int
    __quantidade:int
    __valor:float
    __data:str

    def __init__(self,tipo,classificacaoBebida,quantidade,valor=0.0,data="",login="",id=""):
        self.__id = id
        self.__login = login
        self.__tipo = tipo
        self.__classificacaoBebida = classificacaoBebida
        self.__quantidade = quantidade
        self.__valor = valor
        self.__data = data

    def idGet(self):
        return self.__id

    def loginGet(self):
        return self.__login

    def tipoGet(self):
        return self.__tipo

    def tipoSet(self,tipo):
        self.__tipo = tipo

    def classificacaoGet(self):
        return self.__classificacaoBebida

    def classificacaoSet(self, classificacao):
        self.__classificacaoBebida = classificacao

    def quantidadeGet(self):
        return self.__quantidade

    def quantidadeSet(self,qtd):
        self.__quantidade = qtd

    def valorSet(self,valor):
        self.__quantidade = valor

    def dataSet(self,data):
        self.__quantidade = data

    def atualizaCafe(self,tipo:str,classificacao:str,quantidade:int,valor:float,data:str):
        self.tipoSet(tipo)
        self.classificacaoSet(classificacao)
        self.quantidadeSet(quantidade)
        self.valorSet(valor)
        self.dataSet(data)
        