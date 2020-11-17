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
    indice = 0
    collection = db["Usuarios"] #nome da coleção
    resposta = collection.find({'tipo':'Cafeicultor'}) #Busca-se no BD e exibe a lista em html
    Html='<table class="table"><thead><tr><th scope="col">#</th><th scope="col">Cafeicultor</th><th scope="col">Telefone</th><th scope="col"></th><th scope="col"></th></tr></thead><tbody>'
    for data in resposta: 
        print(data['nome'])
        Html= Html + '<tr>'
        Html= Html + '<th scope="row">'+str(indice)+'</th>'
        Html = Html + '<td class="nome">' + str(data['nome']) +'</td>'
        Html = Html + '<td >' + str(data['telefone']) +'</td>'
        Html = Html + '<td><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#modalVer">Ver</button></td>'
        Html = Html +  '<td><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#modalExcluir">Excluir</button></td>'
        Html = Html + ' </tr>'
        indice += 1
    Html = Html + '</tbody><tfoot><tr><td></td><td></td><td></td>'
    Html = Html + ' <td>Pagina 1 de 5</td>'                
    Html = Html + '<td><button class="nav-button-table "><i class="fas fa-angle-double-left"></i></button>'
    Html = Html + '<button class="nav-button-table "><i class="fas fa-chevron-left"></i></button><button class="nav-button-table ">'
    Html = Html + '<i class="fas fa-chevron-right"></i></button><button class="nav-button-table "><i class="fas fa-angle-double-right"></i></button></td></tr></tfoot></table>'
    return Html                
                        
                   
  #Html = "<select id="+select+"  multiple name="+sample+">"
  #for data in resposta: 
   # Html = Html+"<option value="+ str(data['nome']) + ">" + str(data['nome']) +  "</option>"
  #Html = Html + "<input type=submit value=Import id="+importar+">"
  #Html = Html+"</select>"
  #return Html

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
  #Html = "<select id="+select+"  multiple name="+sample+">"
  #for data in resposta: 
   # Html = Html+"<option value="+ str(data['nome']) + ">" + str(data['nome']) +  "</option>"
  #Html = Html + "<input type=submit value=Import id="+importar+">"
  #Html = Html+"</select>"
  #return Html

#Função para salvar uma saca de café no BDa
def cadastrarSacasDeCafe(s,valor,data):
    collection = db["SacasDeCafe"] 
    dados = {"qtd":s.getSacas(),"tipo": s.getTipo(), "classificacao_bebida" : s.getCBebida(),
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