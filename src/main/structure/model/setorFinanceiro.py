
class setorFinaceiro(object):
    __saldo_disponivel:str
    __quantidade_sacas_armazenadas:int
    __quantidade_sacas_vendidas:int

    def __init__(self,saldo_disponivel='',quantidade_sacas_armazenadas=0,quantidade_sacas_vendidas=0):

        self.__saldo_disponivel = saldo_disponivel
        self.__quantidade_sacas_armazenadas = quantidade_sacas_armazenadas
        self.__quantidade_sacas_vendidas = quantidade_sacas_vendidas

    def registrarVenda(self):
        print("Registra Venda")
    
    def atualizarEstoque(self):
        print("Atualiza Estoque")
    
    def registrarCompraCafe(self):
        print("Regista Compra Café")