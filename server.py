from flask import Flask,request,send_from_directory
import os
import hashlib
from flask import  flash,  redirect, url_for
from flask import render_template
from datetime import date
from src.main.controller import bancoDeDados
from src.main.model.cafeicultor import Cafeicultor
from src.main.model.cadastroCafe import  CadastroCafe
from src.main.controller.webScrapping import WebScrapping

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
@app.route('/')
def login():
    html_file = open("templates/login.html","r")
    html = html_file.read()
    return html

#Páginas do admin:
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    html_file= open("templates/admin.html", "r") 
    html = html_file.read()
    tabela = bancoDeDados.buscarCafeicultores()
    html=html.replace("table_placeholder",tabela) 
    return html 

@app.route('/admin/dadosCafeicultor/', methods=['GET', 'POST'])
def verCafeicultor():
    html_file= open("templates/ver_cafeicultor.html", "r") 
    html = html_file.read()
    indice = str(request.args.get('id' , "" )) 
    cafeicultor = bancoDeDados.getCafeicultor(int(indice))
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
        bancoDeDados.deletarCafeicultor(cafeicultor.loginGet())
        bancoDeDados.removerDaLista(int(indice))
        html = html.replace("eneable","disabled")
        html=html.replace("none","block") #habilita a exibição da mensagem
    return html  

@app.route('/admin/cadastroCafeicultor', methods=['GET', 'POST'])
def cadastrarCafeicultor():
    html_file= open("templates/cadastrar_cafeicultor.html", "r") 
    html = html_file.read() 
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
            bancoDeDados.cadastrarCafeicultor(cafeicultor)
    return html 

@app.route('/admin/edicaoCafeicultor/', methods=['GET', 'POST'])
def editaCafeicultor():
    cafeicultor = Cafeicultor()
    html_file= open("templates/editar_cafeicultor.html", "r") 
    html = html_file.read() 
    indice = str(request.args.get('id' , "" )) 
    cafeicultor = bancoDeDados.getCafeicultor(int(indice))
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
        print('post')
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
        bancoDeDados.alterarDadosDoCafeicultor(cafeicultor.loginGet(),nome,telefone,cidade,endereco,banco,agencia,conta)
        html=html.replace("none","block") #habilita a exibição da mensagem
    return html

#Páginas do cafeicultor:
@app.route('/cafeicultor')
def cafeicultor():
    html_file= open("templates/cafeicultor.html", "r") 
    html = html_file.read() 
    login = 'fulano_de_tal123@hotmail.com'
    tabela = bancoDeDados.buscarSacasDeCafe(login)
    html=html.replace("table_placeholder",tabela)
    return html

@app.route('/cafeicultor/dadosPessoais')
def cafeicultorDadosPessoais():
    html_file= open("templates/dados_pessoais.html", "r") 
    html = html_file.read() 
    return html  

@app.route('/cafeicultor/vendaCafe')
def cafeicultorVender():
    html_file= open("templates/vender.html", "r") 
    html = html_file.read() 
    return html  

@app.route('/cafeicultor/cadastroCafe', methods=['GET', 'POST'])
def cadastrarCafe():
    flag = False
    html_file= open("templates/cadastrar_cafe.html", "r") 
    html = html_file.read() 
    print(request)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        if "formControlQtd" in request.form:
            qtd = request.form["formControlQtd"]
            tipo = request.form["formControlTipo"]
            classificacao_bebida = request.form["formControlBebida"]
            webS = WebScrapping()
            valor = webS.cotacaoCafe(tipo,classificacao_bebida) * int(qtd)
            html=html.replace("Valor do cafe",str(valor)) 
            data = str(date.today())
            if qtd != '':
                flag=True
                html=html.replace("none","block") #habilita a exibição da mensagem
                login = 'fulano_de_tal123@hotmail.com'
                cafe = CadastroCafe(qtd,tipo,classificacao_bebida)
                bancoDeDados.cadastrarSacasDeCafe(cafe,login,valor,data)
    return html

if __name__ == '__main__':
  app.run(debug=True) 
