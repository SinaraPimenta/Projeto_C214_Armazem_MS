import pymongo
import sys
sys.path.append('src/main/model')
import cafeicultor

class BancoDeDadosLogin(object):
    
    #Conexão com o BD
    __cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
    __db = __cliente["ArmazemMS"] 
    __c: object

    def getCafeicultorBD(self,login):
        collection = self.__db["Usuarios"]#nome da coleção
        data = collection.find_one({'login':login})
        self.__c = cafeicultor.Cafeicultor(data['nome'],data['login'],data['senha'],data['telefone'],data['cpf'],data['cidade'],data['endereco'],data['nome_do_banco'],data['agencia_bancaria'],data['numero_da_conta'])
        return self.__c        

    #Função para verificar credencias no BD e retornar 1 usuário
    def buscarUsuarioParaLogar(self,login,senha):
        collection = self.__db["Usuarios"]#nome da coleção
        data = collection.find_one({'login':login, 'senha':senha})
        return data

    def buscarUsuarioParaTrocarSenha(self,login,senhaNova):
        collection = self.__db["Usuarios"]#nome da coleção
        resposta = collection.find_one({'login':login})
        if resposta != None:
            collection.update_one({'login': login},{'$set': {"senha":senhaNova}})
        return resposta