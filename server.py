from flask import Flask,request,send_from_directory
import os
import hashlib
from flask import  flash,  redirect, url_for
from flask import render_template
from datetime import date
from src.main.controller import bancoDeDados
from src.main.model.cafeicultor import Cafeicultor
from src.main.model.sacaCafe import SacaCafe
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
        bancoDeDados.removerDalistaCafeicultor(int(indice))
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
        cafeicultor.atualizaCafeicultor(nome,telefone,endereco,cidade,banco,agencia,conta)
        bancoDeDados.substituiCafeicultor(int(indice),cafeicultor)
        html=html.replace("none","block") #habilita a exibição da mensagem
        return redirect("/admin/edicaoCafeicultor/?id="+indice)
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
    html_file= open("templates/vender_cafe.html", "r") 
    html = html_file.read() 
    return html  

@app.route('/cafeicultor/cadastroCafe', methods=['GET', 'POST'])
def cadastrarCafe():
    flag = False
    html_file= open("templates/cadastrar_cafe.html", "r") 
    html = html_file.read() 
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        if "formControlQtd" in request.form:
            qtd = request.form["formControlQtd"]
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
                    bancoDeDados.cadastrarSacasDeCafe(cafe,valor,data)
    return html

@app.route('/cafeicultor/edicaoCafe/', methods=['GET','POST'])
def editarCafe():
    html_file = open("templates/editar_cafe.html","r")
    html = html_file.read()
    indice = str(request.args.get('id' , "" )) 
    cafe = bancoDeDados.getCafe(int(indice))
    if(cafe):
        html= substituirHTML(cafe.tipoGet(),"Tipo",html)
        html= substituirHTML(cafe.classificacaoGet(),"Bebida",html)
        html= substituirHTML(cafe.quantidadeGet(),"Qtd atual",html)
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        tipo = request.form["tipo"]
        bebida = request.form["bebida"]
        qtd = request.form["qtd"]
        if tipo == '':
            tipo = cafe.tipoGet()
        if bebida == '':
            bebida = cafe.classificacaoGet()
        if qtd == '':
            qtd = cafe.quantidadeGet()
        webS = WebScrapping()
        valor = webS.cotacaoCafe(tipo,bebida) * int(qtd)
        data = date.today()
        data = data.strftime("%d/%m/%Y")
        #if valor==0:
            #html=html.replace("block","none")
            #html=html.replace("hidden","visible") #habilita a exibição da mensagem
        #else:
        bancoDeDados.alterarSacaDeCafe(cafe,valor,data)
        cafe.atualizaCafe(tipo,bebida,qtd,valor,data)
        bancoDeDados.substituiCafe(int(indice),cafe)
        html=html.replace("none","block") #habilita a exibição da mensagem
        return redirect("/cafeicultor/edicaoCafe/?id="+indice)
    return html

if __name__ == '__main__':
  app.run(debug=True) 
