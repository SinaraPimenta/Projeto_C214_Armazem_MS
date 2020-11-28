class SacaCafe(object):
    __id:str
    __login:str
    __indice:int
    __tipo:str
    __classificacaoBebida:int
    __quantidade:int
    __valor: float
    __data:str

    def __init__(self,tipo,classificacaoBebida,quantidade,valor=0.0,data="",indice=-1,login="",id=""):
        self.__id = id
        self.__login = login
        self.__tipo = tipo
        self.__classificacaoBebida = classificacaoBebida
        self.__quantidade = quantidade
        self.__valor = valor
        self.__data = data
        self.__indice = indice

    def idGet(self):
        return self.__id

    def indiceSet(self,indice):
        self.__indice = indice
    
    def indiceGet(self):
        return self.__indice

    def loginGet(self):
        return self.__login

    def loginSet(self,login):
        self.__login = login

    def tipoGet(self):
        return self.__tipo
    
    def valorGet(self):
        return self.__valor
    
    def dataGet(self):
        return self.__data

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
        self.__valor = valor

    def dataSet(self,data):
        self.__data = data

    def atualizaCafe(self,tipo:str,classificacao:str,quantidade:int,valor:float,data:str,indice:int):
        self.tipoSet(tipo)
        self.classificacaoSet(classificacao)
        self.quantidadeSet(quantidade)
        self.valorSet(valor)
        self.dataSet(data)
        self.indiceSet(indice)
        