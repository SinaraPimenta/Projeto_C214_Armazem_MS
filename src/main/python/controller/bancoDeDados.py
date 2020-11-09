import pymongo

#Conexão com o BD
cliente = pymongo.MongoClient("mongodb+srv://admin:armazemMS@clusterc214.wv3t7.mongodb.net/ArmazemMS?retryWrites=true&w=majority")
db = cliente["ArmazemMS"] #nome do banco

#Função para verificar credencias no BD e retornar 1 usuário
def buscarUsuarioParaLogar(login,senha):
    collection = db["Usuarios"] #nome da coleção
    resposta = collection.find_one({'login':login, 'senha':senha})
    return resposta


#Função para retornar os cafeicultores salvos no BD
def buscarCafeicultores():
    collection = db["Usuarios"] #nome da coleção
    resposta = collection.find({'tipo':'Cafeicultor'}) #Busca-se no BD e exibe a lista em html
  #Html = "<select id="+select+"  multiple name="+sample+">"
  #for data in resposta: 
   # Html = Html+"<option value="+ str(data['nome']) + ">" + str(data['nome']) +  "</option>"
  #Html = Html + "<input type=submit value=Import id="+importar+">"
  #Html = Html+"</select>"
  #return Html

#Função para salvar um cafeicultor no BD
def cadastrarCafeicultor(tipo, nome,login,senha,cpf,telefone="", cidade="", endereco="",nome_do_banco="", agencia_bancaria="",numero_da_conta=""):
    collection = db["Usuarios"] #nome da coleção
    #receber hash da senha!!!!! 
    dados = {"tipo":'Cafeicultor',"nome": nome, "login" : login, "senha": senha, "telefone":telefone, 
    "cpf":cpf, "cidade":cidade, "endereco":endereco,"nome_do_banco":nome_do_banco,
    "agencia_bancaria":agencia_bancaria,"numero_da_conta":numero_da_conta}
    collection.insert_one(dados)

#Função para deletar um cafeicultor no BD
def deletarCafeicultor(login):
    collection = db["Usuarios"] #nome da coleção
    collection.delete_one({ 'login': login })

#Função para retornar as sacas de cafe de um cafeicultor salvas no BD
def buscarSacasDeCafe(login):
    collection = db["SacasDeCafe"] #nome da coleção
    resposta = collection.find({'login':login}) #Busca-se no BD e exibe a lista em html
  #Html = "<select id="+select+"  multiple name="+sample+">"
  #for data in resposta: 
   # Html = Html+"<option value="+ str(data['nome']) + ">" + str(data['nome']) +  "</option>"
  #Html = Html + "<input type=submit value=Import id="+importar+">"
  #Html = Html+"</select>"
  #return Html

#Função para salvar uma saca de café no BD
def cadastrarSacasDeCafe(qtd,tipo,classificacao_bebida,valor,data):
    collection = db["SacasDeCafe"] 
    dados = {"qtd":qtd,"tipo": tipo, "classificacao_bebida" : classificacao_bebida,
    "valor" : valor,"data":data}
    collection.insert_one(dados)

#Função para deletar uma saca de café no BD
def deletarSacaDeCafe(id):
    collection = db["SacasDeCafe"] #nome da coleção
    collection.delete_one({ 'id': id })

#Função para salvar um cafeicultor no BD
def alterarDadosDoCafeicultor(login,nome,senha,telefone,cidade, endereco,nome_do_banco, agencia_bancaria,numero_da_conta):
    collection = db["Usuarios"] #nome da coleção
    #receber hash da senha!!!!! 
    collection.update_one({'login': login},{'$set': {"nome": nome, "senha": senha, "telefone":telefone, 
    "cidade":cidade, "endereco":endereco,"nome_do_banco":nome_do_banco,
    "agencia_bancaria":agencia_bancaria,"numero_da_conta":numero_da_conta} })