import pymongo
from bson.objectid import ObjectId
from src.main.model.cafeicultor import Cafeicultor
from src.main.model.sacaCafe import SacaCafe
from src.main.model.cafeicultor import Cafeicultor

listaCafeicultor = []
listaCafe = []

class BancoDeDados(object):
    
    #Conexão com o BD
    __cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
    __db = __cliente["ArmazemMS"] #nome do banco
    __listaCafeicultor = []
    __listaCafe = []

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

    def getCafe(self,indice):
        return listaCafe[indice]

    def substituiCafe(self,indice,cafe):
        listaCafe[indice] = cafe

    def removerDalistaCafe(self,indice):
        listaCafe.pop(indice)

    #Função para retornar os cafeicultores salvos no BD
    def buscarCafeicultores(self):
        indice = 0
        collection = self.__db["Usuarios"] #nome da coleção
        resposta = collection.find({'tipo':'Cafeicultor'}) #Busca-se no BD e exibe a listaCafeicultor em html
        Html = '<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
        for data in resposta:
            cafeicultor = Cafeicultor(data['nome'],data['login'],data['senha'],data['telefone'],data['cpf'],data['cidade'],data['endereco'],data['nome_do_banco'],data['agencia_bancaria'],data['numero_da_conta'])
            listaCafeicultor.append(cafeicultor)
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
    def cadastrarCafeicultor(self,c):
        collection = self.__db["Usuarios"] #nome da coleção
        dados = {"tipo":'Cafeicultor',"nome": c.nomeGet(), "login" : c.loginGet(), "senha": c.senhaGet(), "telefone":c.telefoneGet(), 
        "cpf":c.cpfGet(), "cidade":c.cidadeGet(), "endereco":c.enderecoGet(),"nome_do_banco":c.bancoGet(),
        "agencia_bancaria":c.agenciaGet(),"numero_da_conta":c.contaGet()}
        collection.insert_one(dados)

    #Função para deletar um cafeicultor no BD
    def deletarCafeicultor(self,login):
        collection = self.__db["Usuarios"] #nome da coleção
        collection.delete_one({ 'login': login })

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

    #Função para salvar um cafeicultor no BD
    def alterarDadosDoCafeicultor(self,c):
        collection = self.__db["Usuarios"] #nome da coleção
        collection.update_one({'login': c.loginGet()},{'$set': {"nome": c.nomeGet(), "telefone":c.telefoneGet(), 
        "cidade":c.cidadeGet(), "endereco":c.enderecoGet(),"nome_do_banco":c.bancoGet(),
        "agencia_bancaria":c.agenciaGet(),"numero_da_conta":c.contaGet()} })