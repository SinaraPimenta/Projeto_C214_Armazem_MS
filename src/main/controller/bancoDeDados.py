import pymongo
from src.main.model.cafeicultor import Cafeicultor
from src.main.model.cadastroCafe import CadastroCafe

lista = []

#Conexão com o BD
cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
db = cliente["ArmazemMS"] #nome do banco

#Função para verificar credencias no BD e retornar 1 usuário
def buscarUsuarioParaLogar(login,senha):
    collection = db["Usuarios"] #nome da coleção
    resposta = collection.find_one({'login':login, 'senha':senha})
    return resposta

def getCafeicultor(indice):
    return lista[indice]

def removerDaLista(indice):
    return lista.pop(indice)

#Função para retornar os cafeicultores salvos no BD
def buscarCafeicultores():
    indice = 0
    collection = db["Usuarios"] #nome da coleção
    resposta = collection.find({'tipo':'Cafeicultor'}) #Busca-se no BD e exibe a lista em html
    Html = '<table class="table" id="tabela"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
    for data in resposta:
        cafeicultor = Cafeicultor(data['nome'],data['login'],data['senha'],data['telefone'],data['cpf'],data['cidade'],data['endereco'],data['nome_do_banco'],data['agencia_bancaria'],data['numero_da_conta'])
        lista.append(cafeicultor)
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
def cadastrarCafeicultor(c):
    collection = db["Usuarios"] #nome da coleção
    dados = {"tipo":'Cafeicultor',"nome": c.nomeGet(), "login" : c.loginGet(), "senha": c.senhaGet(), "telefone":c.telefoneGet(), 
    "cpf":c.cpfGet(), "cidade":c.cidadeGet(), "endereco":c.enderecoGet(),"nome_do_banco":c.bancoGet(),
    "agencia_bancaria":c.agenciaGet(),"numero_da_conta":c.contaGet()}
    collection.insert_one(dados)

#Função para deletar um cafeicultor no BD
def deletarCafeicultor(login):
    collection = db["Usuarios"] #nome da coleção
    collection.delete_one({ 'login': login })

#Função para retornar as sacas de cafe de um cafeicultor salvas no BD
def buscarSacasDeCafe(login):
    collection = db["SacasDeCafe"] #nome da coleção
    resposta = collection.find({'login':login}) #Busca-se no BD e exibe a lista em html
    Html = '<table class="table"><thead><tr><th scope="col">Tipo</th><th scope="col">Bebida</th><th scope="col">Valor* [R$]</th><th scope="col">Quantidade</th><th scope="col"></th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
    
    for data in resposta:
        Html = Html + '<tr>'
        Html = Html + '<th scope="row">'+str(data["tipo"])+'</th>'
        Html = Html + '<td>'+str(data["classificacao_bebida"])+'</td>'
        Html = Html + '<td>'+str(data['valor'])+'</td>'
        Html = Html + '<td>'+str(data['qtd'])+'</td>'
        Html = Html + '<td><button class="btn btn-primary">Vender</button></td>'
        Html = Html + '<td><button class="btn btn-primary">Editar</button></td>'
        Html = Html + '<td><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#modalExcluir">Excluir</button></td>'
        Html = Html + '</tr>'

    Html = Html + '</tbody></table>'   
 
    return Html

#Função para salvar uma saca de café no BDa
def cadastrarSacasDeCafe(s,login,valor,data):
    collection = db["SacasDeCafe"] 
    dados = {"login":login,"qtd":s.getSacas(),"tipo": s.getTipo(), "classificacao_bebida" : s.getCBebida(),
    "valor" : valor,"data":data}
    collection.insert_one(dados)

#Função para deletar uma saca de café no BD
def deletarSacaDeCafe(id):
    collection = db["SacasDeCafe"] #nome da coleção
    collection.delete_one({ 'id': id })

#Função para salvar um cafeicultor no BD
def alterarDadosDoCafeicultor(login,nome,telefone,cidade, endereco,nome_do_banco, agencia_bancaria,numero_da_conta):
    collection = db["Usuarios"] #nome da coleção
    collection.update_one({'login': login},{'$set': {"nome": nome, "telefone":telefone, 
    "cidade":cidade, "endereco":endereco,"nome_do_banco":nome_do_banco,
    "agencia_bancaria":agencia_bancaria,"numero_da_conta":numero_da_conta} })