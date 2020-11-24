import pymongo
from bson.objectid import ObjectId
import sys
sys.path.append('src/main/model')
import cafeicultor
#from src.main.model.cafeicultor import Cafeicultor

listaCafeicultor = []
listaCafe = []

class BancoDeDadosAdmin(object):
    
    #Conexão com o BD
    __cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
    __db = __cliente["ArmazemMS"] #nome do banco
    __listaCafeicultor = []

    #Função para verificar credencias no BD e retornar 1 usuário
    def buscarUsuarioParaLogar(self,login,senha):
        collection = self.__db["Usuarios"]#nome da coleção
        resposta = collection.find_one({'login':login, 'senha':senha})
        return print('oi')

    def getCafeicultor(self,indice):
        return listaCafeicultor[indice]

    def substituiCafeicultor(self,indice,cafeicultor):
        listaCafeicultor[indice] = cafeicultor

    def removerDalistaCafeicultor(self,indice):
        listaCafeicultor.pop(indice)

    def adicionarNalistaCafeicultor(self,cafeicultor):
        listaCafeicultor.append(cafeicultor)

    #Função para retornar os cafeicultores salvos no BD
    def buscarCafeicultores(self,colecao):
        indice = 0
        collection = self.__db[colecao] #nome da coleção
        resposta = collection.find({'tipo':'Cafeicultor'}) #Busca-se no BD e exibe a listaCafeicultor em html
        Html = '<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
        for data in resposta:
            c = cafeicultor.Cafeicultor(data['nome'],data['login'],data['senha'],data['telefone'],data['cpf'],data['cidade'],data['endereco'],data['nome_do_banco'],data['agencia_bancaria'],data['numero_da_conta'])
            listaCafeicultor.append(c)
            Html= Html + '<tr>'
            Html= Html + '<th scope="row">'+str(indice)+'</th>'
            Html = Html + '<td class="nome">' + str(data['nome']) +'</td>'
            Html = Html + '<td >' + str(data['telefone']) +'</td>'
            Html = Html + '<td><button type="button" class="btn btn-primary" id="verCafeicultor" onclick="verCafeicultor('+str(indice)+')">Ver</button></td>'
            Html = Html +  '<td><button type="button" class="btn btn-primary" id="editarCafeicultor" onclick="editarCafeicultor('+str(indice)+')">Editar</button></td>'
            Html = Html + ' </tr>'
            indice += 1
        Html = Html + '</tbody></table>'
        return Html                

    #Função para salvar um cafeicultor no BD
    def cadastrarCafeicultor(self,c,colecao):
        collection = self.__db[colecao] #nome da coleção
        dados = {"tipo":'Cafeicultor',"nome": c.nomeGet(), "login" : c.loginGet(), "senha": c.senhaGet(), "telefone":c.telefoneGet(), 
        "cpf":c.cpfGet(), "cidade":c.cidadeGet(), "endereco":c.enderecoGet(),"nome_do_banco":c.bancoGet(),
        "agencia_bancaria":c.agenciaGet(),"numero_da_conta":c.contaGet()}
        collection.insert_one(dados)

    #Função para deletar um cafeicultor no BD
    def deletarCafeicultor(self,login,colecao):
        collection = self.__db[colecao] #nome da coleção
        collection.delete_one({ 'login': login })

    #Função para salvar um cafeicultor no BD
    def alterarDadosDoCafeicultor(self,c,colecao):
        collection = self.__db[colecao] #nome da coleção
        collection.update_one({'login': c.loginGet()},{'$set': {"nome": c.nomeGet(), "telefone":c.telefoneGet(), 
        "cidade":c.cidadeGet(), "endereco":c.enderecoGet(),"nome_do_banco":c.bancoGet(),
        "agencia_bancaria":c.agenciaGet(),"numero_da_conta":c.contaGet()} })