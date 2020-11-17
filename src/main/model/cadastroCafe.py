
class CadastroCafe(object):
    __qtdSacas:int
    __tipoBebida:str
    __classificacaoBebida:str

    def __init__(self,qtdSacas,tipoBebida,classsificacaoBebida):
        self.__qtdSacas = qtdSacas
        self.__tipoBebida = tipoBebida
        self.__classificacaoBebida = classsificacaoBebida
    
    def getSacas(self):
        return self.__qtdSacas
    
    def getTipo(self):
        return self.__tipoBebida
        
    def getCBebida(self):
        return self.__classificacaoBebida