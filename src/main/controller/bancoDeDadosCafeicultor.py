import pymongo
from bson.objectid import ObjectId
from src.main.model.sacaCafe import SacaCafe

listaCafe = []

class BancoDeDadosCafeicultor(object):
    
    #Conexão com o BD
    __cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
    __db = __cliente["ArmazemMS"] #nome do banco
    __listaCafe = []

    #Função para verificar credencias no BD e retornar 1 usuário
    def buscarUsuarioParaLogar(self,login,senha):
        collection = self.__db["Usuarios"]#nome da coleção
        resposta = collection.find_one({'login':login, 'senha':senha})
        return print('oi')

    def getCafe(self,indice):
        return listaCafe[indice]

    def substituiCafe(self,indice,cafe):
        listaCafe[indice] = cafe

    def removerDalistaCafe(self,indice):
        listaCafe.pop(indice)

    def adicionarNalistaCafe(self,cafe):
        listaCafe.append(cafe)       

    #Função para retornar as sacas de cafe de um cafeicultor salvas no BD
    def buscarSacasDeCafe(self,login):
        collection = self.__db["SacasDeCafe"] #nome da coleção
        resposta = collection.find({'login':login}) #Busca-se no BD e exibe a listaCafeicultor em html
        Html = '<table id="tabela" class="table"><thead><tr><th scope="col">#</th><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col">Data do cadastro</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
        indice = 0
        for data in resposta:
            cafe = SacaCafe(data['tipo'],data['classificacao_bebida'],data['qtd'],data['valor'],data['data'],data['login'],str(data['_id']))
            listaCafe.append(cafe)
            Html = Html + '<tr>'
            Html= Html + '<th scope="row">'+str(indice)+'</th>'
            Html = Html + '<td>'+str(data["tipo"])+'</td>'
            Html = Html + '<td>'+str(data["classificacao_bebida"])+'</td>'
            Html = Html + '<td>'+str(data['valor'])+'</td>'
            Html = Html + '<td>'+str(data['qtd'])+'</td>'
            Html = Html + '<td>'+str(data['data'])+'</td>'
            Html = Html +  '<td><button type="button" class="btn btn-primary" id="editarCafe" onclick="venderCafe('+str(indice)+')">Vender</button></td>'
            Html = Html +  '<td><button type="button" class="btn btn-primary" id="editarCafe" onclick="editarCafe('+str(indice)+')">Editar</button></td>'
            Html = Html + '</tr>'
            indice+=1
        Html = Html + '</tbody></table>'   
        return Html

    #Função para salvar uma saca de café no BD
    def cadastrarSacasDeCafe(self,s,valor,data):
        collection = self.__db["SacasDeCafe"] 
        dados = {"login":s.loginGet(),"qtd":s.quantidadeGet(),"tipo": s.tipoGet(), "classificacao_bebida" : s.classificacaoGet(),
        "valor" : valor,"data":data}
        collection.insert_one(dados)

    #Função para atualizar uma saca de café no BD
    def alterarSacaDeCafe(self,s,valor,data):
        collection = self.__db["SacasDeCafe"] 
        collection.update_one({'_id': ObjectId(s.idGet())},{'$set': {"tipo":s.tipoGet(), "classificacao_bebida":s.classificacaoGet(),
        "qtd":s.quantidadeGet(),"valor":valor,"data":data} })

    #Função para atualizar uma saca de café no BD
    def venderSacaDeCafe(self,s,valor,data):
        collection = self.__db["SacasDeCafe"] 
        collection.update_one({'_id': ObjectId(s.idGet())},{'$set': {"qtd":s.quantidadeGet(),"valor":valor,"data":data} })

    #Função para deletar uma saca de café no BD
    def deletarSacaDeCafe(self,id):
        collection = self.__db["SacasDeCafe"] #nome da coleção
        collection.delete_one({'_id': ObjectId(id)})