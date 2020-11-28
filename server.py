from flask import Flask,request,send_from_directory
import os
import hashlib
from flask import  flash,  redirect, url_for
from flask import render_template
from datetime import date
from src.main.model.cafeicultor import Cafeicultor
from src.main.model.sacaCafe import SacaCafe
from src.main.model.administrador import Administrador
from src.main.controller.webScrapping import WebScrapping
from src.main.controller.mediador import MediadorDoCafeicultor
from src.main.controller.bancoDeDadosCafeicultor import BancoDeDados

flag= False
flagErro = False
valor_venda = 0
administrador = Administrador()
cafeicultorSacas = Cafeicultor()
bd = BancoDeDados()

def generate_hash(string_hash: str)->str:
    hash_object = hashlib.sha1(string_hash.encode('utf-8'))
    pbHash = hash_object.hexdigest()
    return pbHash

app = Flask(__name__)
#app = Flask(__name__, static_url_path='/src/main/view/static')

#Função para substituição de valores na página html
def substituirHTML(var,value,html):
    if str(var)!=str(value):
        html=html.replace(('"'+str(value)+'"'),('"'+str(var)+'"'))
    return html

#Página de Login
@app.route('/',methods=['GET', 'POST'])
def login():
    global usuarioLogado 
    html_file = open("templates/login.html","r")
    html = html_file.read()
    if request.method == 'POST':
        email = request.form["email"]
        senha = request.form["senha"]
        senha = generate_hash(senha)
        bd = BancoDeDados()
        resposta = bd.buscarUsuarioParaLogar(email,senha)
        if resposta == None:
            html = html.replace("Entre com seu email","Email/senha incorretos, entre com seu email")
            html = html.replace("Entre com sua senha","Email/senha incorretos, entre com sua senha")
        elif resposta['tipo'] == 'Cafeicultor':
            usuarioLogado = email
            return redirect("/cafeicultor")
        elif resposta['tipo'] == 'Administrador':
            usuarioLogado = email
            return redirect("/admin")
    return html

#Pagina de Trocar a Senha
@app.route('/novaSenha',methods=['GET', 'POST'])
def novaSenha():
    html_file = open("templates/trocar_senha.html","r")
    html = html_file.read()
    if request.method == 'POST':
        email = request.form["email"]
        novaSenha = request.form["senha"]
        novaSenha = generate_hash(novaSenha)
        bd = BancoDeDados()
        resposta = bd.buscarUsuarioParaTrocarSenha(email,novaSenha)
        if resposta == None:
            html = html.replace("Entre com seu email","Email incorreto, entre com seu email")
        else:
            return redirect("/")
    return html

#Páginas do admin:
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    html_file= open("templates/admin.html", "r") 
    html = html_file.read()
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    tabela = administrador.buscarCafeicultores("Usuarios")
    html=html.replace("table_placeholder",tabela) 
    return html 

@app.route('/admin/dadosCafeicultor/', methods=['GET', 'POST'])
def verCafeicultor():
    html_file= open("templates/ver_cafeicultor.html", "r") 
    html = html_file.read()
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    indice = str(request.args.get('id' , "" )) 
    cafeicultor = administrador.getCafeicultor(int(indice))
    if(cafeicultor):
        html = html.replace("NomeCafeilcutor",cafeicultor.nomeGet())
        html = html.replace("CPF",cafeicultor.cpfGet())
        html= substituirHTML(cafeicultor.telefoneGet(),"Telefone",html)
        html= substituirHTML(cafeicultor.loginGet(),"Email",html)
        html= substituirHTML(cafeicultor.enderecoGet(),"Rua, numero",html)
        html= substituirHTML(cafeicultor.cidadeGet(),"Cidade",html)
        html= substituirHTML(cafeicultor.bancoGet(),"Banco",html)
        html= substituirHTML(cafeicultor.agenciaGet(),"Agencia Bancaria",html)
        html= substituirHTML(cafeicultor.contaGet(),"Numero da Conta",html)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        administrador.excluirCafeicultor(cafeicultor.loginGet(),int(indice),"Usuarios")
        html = html.replace("eneable","disabled")
        html=html.replace("none","block") #habilita a exibição da mensagem
    return html  

@app.route('/admin/cadastroCafeicultor', methods=['GET', 'POST'])
def cadastrarCafeicultor():
    html_file= open("templates/cadastrar_cafeicultor.html", "r") 
    html = html_file.read() 
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        html=html.replace("none","block") #habilita a exibição da mensagem
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        endereco = request.form["endereco"]
        cidade = request.form["cidade"]
        banco = request.form["banco"]
        agencia = request.form["agencia"]
        conta = request.form["conta"]
        senha = 'C4f31cult0R#2020'
        senha = generate_hash(senha)
        if nome!= '':
            cafeicultor = Cafeicultor(nome,email,senha,telefone,cpf,cidade,endereco,banco,agencia,conta)
            administrador.cadastrarCafeicultor(cafeicultor,"Usuarios")
    return html 

@app.route('/admin/edicaoCafeicultor/', methods=['GET', 'POST'])
def editaCafeicultor():
    cafeicultor = Cafeicultor()
    html_file= open("templates/editar_cafeicultor.html", "r") 
    html = html_file.read() 
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    global flag
    if(flag):
        html=html.replace("none","block") #habilita a exibição da mensagem
        flag = False
    indice = str(request.args.get('id' , "" )) 
    cafeicultor = administrador.getCafeicultor(int(indice))
    if(cafeicultor):
        html = html.replace("Nome do Cafeicultor",cafeicultor.nomeGet())
        html = html.replace("CPF",cafeicultor.cpfGet())
        html= substituirHTML(cafeicultor.telefoneGet(),"Telefone",html)
        html= substituirHTML(cafeicultor.enderecoGet(),"Rua, numero",html)
        html= substituirHTML(cafeicultor.cidadeGet(),"Cidade",html)
        html= substituirHTML(cafeicultor.bancoGet(),"Banco",html)
        html= substituirHTML(cafeicultor.agenciaGet(),"Agencia Bancaria",html)
        html= substituirHTML(cafeicultor.contaGet(),"Numero da Conta",html)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        cidade = request.form["cidade"]
        banco = request.form["banco"]
        agencia = request.form["agencia"]
        conta = request.form["conta"]
        if nome == '':
            nome = cafeicultor.nomeGet()
        if telefone == '':
            telefone = cafeicultor.telefoneGet()
        if endereco == '':
            endereco = cafeicultor.enderecoGet()
        if cidade == '':
            cidade = cafeicultor.cidadeGet()
        if banco == '':
            banco = cafeicultor.bancoGet()
        if agencia == '':
            agencia = cafeicultor.agenciaGet()
        if conta == '':
            conta = cafeicultor.contaGet()
        cafeicultor.atualizaCafeicultor(nome,telefone,endereco,cidade,banco,agencia,conta)
        administrador.editarCafeicultor(cafeicultor,int(indice),"Usuarios")
        flag = True
        return redirect("/admin/edicaoCafeicultor/?id="+indice)
    return html

#Páginas do cafeicultor:
@app.route('/cafeicultor')
def cafeicultor():
    html_file= open("templates/cafeicultor.html", "r") 
    html = html_file.read() 
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    mediador = MediadorDoCafeicultor("SacasDeCafe",bd,login=usuarioLogado)
    tabela = cafeicultorSacas.buscarCafe(mediador)
    html=html.replace("table_placeholder",tabela)
    return html

@app.route('/cafeicultor/dadosPessoais')
def cafeicultorDadosPessoais():
    html_file= open("templates/dados_cafeicultor.html", "r") 
    html = html_file.read()
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    bd = BancoDeDadosLogin()
    cafeicultor = bd.getCafeicultorBD(usuarioLogado)
    print(cafeicultor.nomeGet())
    if(cafeicultor):
        html = html.replace("NomeCafeilcutor",cafeicultor.nomeGet())
        html = html.replace("CPF",cafeicultor.cpfGet())
        html= substituirHTML(cafeicultor.telefoneGet(),"Telefone",html)
        html= substituirHTML(cafeicultor.loginGet(),"Email",html)
        html= substituirHTML(cafeicultor.enderecoGet(),"Rua, numero",html)
        html= substituirHTML(cafeicultor.cidadeGet(),"Cidade",html)
        html= substituirHTML(cafeicultor.bancoGet(),"Banco",html)
        html= substituirHTML(cafeicultor.agenciaGet(),"Agencia Bancaria",html)
        html= substituirHTML(cafeicultor.contaGet(),"Numero da Conta",html)
    return html

@app.route('/cafeicultor/vendaCafe/', methods=['GET', 'POST'])
def cafeicultorVender():
    global flag,flagErro,valor_venda
    html_file= open("templates/vender_cafe.html", "r") 
    html = html_file.read()
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    indice = str(request.args.get('id' , "" )) 
    mediador = MediadorDoCafeicultor("SacasDeCafe",bd,indice=int(indice))
    cafe = cafeicultorSacas.getCafe(mediador)
    if(flag):
        html=html.replace("none","block") #habilita a exibição da mensagem
        #html=html.replace("Valor do cafe",str(cafe.valorGet())) 
        html=html.replace("Valor do cafe",str(valor_venda)) 
        flag = False
    if(flagErro):
        html=html.replace("Valor do cafe",str(valor_venda)) 
        html=html.replace("eneable","disabled")
        flagErro = False
    if(cafe):
        html= substituirHTML(cafe.tipoGet(),"Tipo",html)
        html= substituirHTML(cafe.classificacaoGet(),"Bebida",html)
        html= substituirHTML(cafe.quantidadeGet(),"Qtd atual",html)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        qtd_venda = int(request.form["qtd"])
        webS = WebScrapping()
        valor_venda = webS.cotacaoCafe(cafe.tipoGet(),cafe.classificacaoGet()) * qtd_venda
        data = date.today()
        data = data.strftime("%d/%m/%Y")
        qtd_nova = cafe.quantidadeGet() - qtd_venda
        if qtd_nova==0:
            mediador = MediadorDoCafeicultor("SacasDeCafe",bd,cafe,indice=int(indice))
            cafeicultorSacas.excluirCafe(mediador)
            flagErro = True
        else:
            valor_novo = webS.cotacaoCafe(cafe.tipoGet(),cafe.classificacaoGet()) * qtd_nova
            cafe.atualizaCafe(cafe.tipoGet(),cafe.classificacaoGet(),qtd_nova,valor_novo,data,int(indice))
            mediador = MediadorDoCafeicultor("SacasDeCafe",bd,cafe)
            cafeicultorSacas.venderCafe(mediador) 
            flag = True   
        return redirect("/cafeicultor/vendaCafe/?id="+indice)
    return html

@app.route('/cafeicultor/cadastroCafe', methods=['GET', 'POST'])
def cadastrarCafe():
    html_file= open("templates/cadastrar_cafe.html", "r") 
    html = html_file.read() 
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        if "formControlQtd" in request.form:
            qtd = int(request.form["formControlQtd"])
            tipo = request.form["formControlTipo"]
            classificacao_bebida = request.form["formControlBebida"]
            webS = WebScrapping()
            valor = webS.cotacaoCafe(tipo,classificacao_bebida) * int(qtd)
            if valor==0:
                html=html.replace("block","none")
                html=html.replace("hidden","visible") #habilita a exibição da mensagem
            else:
                html=html.replace("Valor do cafe",str(valor)) 
                data = date.today()
                data = data.strftime("%d/%m/%Y")
                if qtd != '':
                    flag=True
                    html=html.replace("visible","hidden")
                    html=html.replace("none","block") #habilita a exibição da mensagem
                    login = 'fulano_de_tal123@hotmail.com' #PEGAR O LOGIN DA PESSOAAAAAA
                    cafe = SacaCafe(tipo,classificacao_bebida,qtd,0.0,'',login)
                    cafe.valorSet(valor)
                    cafe.dataSet(data)
                    cafe.loginSet(usuarioLogado)
                    mediador = MediadorDoCafeicultor("SacasDeCafe",bd,cafe)
                    cafeicultorSacas.cadastrarCafe(mediador)
    return html

@app.route('/cafeicultor/edicaoCafe/', methods=['GET','POST'])
def editarCafe():
    global flag,flagErro
    html_file = open("templates/editar_cafe.html","r")
    html = html_file.read()
    global usuarioLogado
    html = html.replace("login do usuario", usuarioLogado)
    indice = str(request.args.get('id' , "" )) 
    mediador = MediadorDoCafeicultor("SacasDeCafe",bd,indice=int(indice))
    cafe = cafeicultorSacas.getCafe(mediador)
    if(flag):
        html=html.replace("none","block") #habilita a exibição da mensagem
        html=html.replace("visible","hidden") #habilita a exibição da mensagem
        html=html.replace("Valor do cafe",str(cafe.valorGet())) 
        flag = False
    if(flagErro):
        html=html.replace("block","none")
        html=html.replace("hidden","visible") #habilita a exibição da mensagem
        flagErro = False
    if(cafe):
        html= substituirHTML(cafe.tipoGet(),"Tipo",html)
        html= substituirHTML(cafe.classificacaoGet(),"Bebida",html)
        html= substituirHTML(cafe.quantidadeGet(),"Qtd atual",html)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        tipo = request.form["tipo"]
        bebida = request.form["bebida"]
        qtd = int(request.form["qtd"])
        if tipo == '':
            tipo = cafe.tipoGet()
        if bebida == '':
            bebida = cafe.classificacaoGet()
        if qtd == '':
            qtd = cafe.quantidadeGet()
        webS = WebScrapping()
        valor = webS.cotacaoCafe(tipo,bebida) * qtd
        data = date.today()
        data = data.strftime("%d/%m/%Y")
        if valor==0:
            if qtd==0:
                mediador = MediadorDoCafeicultor("SacasDeCafe",bd,cafe)
                cafeicultorSacas.excluirCafe(mediador)
                return redirect("/cafeicultor")
            else:
                flagErro = True
        else:            
            cafe.atualizaCafe(tipo,bebida,qtd,valor,data,int(indice))
            mediador = MediadorDoCafeicultor("SacasDeCafe",bd,cafe)
            cafeicultorSacas.editarCafe(mediador)
            flag = True   
        return redirect("/cafeicultor/edicaoCafe/?id="+indice)
    return html

if __name__ == '__main__':
  app.run(debug=True) 
