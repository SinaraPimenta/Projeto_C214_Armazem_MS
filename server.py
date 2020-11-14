from flask import Flask,request,send_from_directory
import os
import hashlib
from flask import  flash,  redirect, url_for
from flask import render_template
#from src.main.structure.controller import bancoDeDados

#def generate_hash(string_hash: str)->str:
 #   hash_object = hashlib.sha1(string_hash.encode('utf-8'))
  #  pbHash = hash_object.hexdigest()
   # return pbHash

app = Flask(__name__)
#app = Flask(__name__, static_url_path='/src/main/view/static')

#Função para substituição de valores na página html
def substituirHTML(var,value,html):
    if str(var)!=str(value):
        html=html.replace(('"'+str(value)+'"'),('"'+str(var)+'"'))
    return html

@app.route('/')
def login():
    html_file = open("templates/login.html","r")
    html = html_file.read()
    return html

@app.route('/admin')
def admin():
    html_file= open("templates/admin.html", "r") #Leitura do arquivo upload.html para exibição deste na página
    html = html_file.read()
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        #Verifica se a requisição veio da seleção de uma amostra da lista:sição veio do upload:
        email = request.form["email"]
        senha = request.form["senha"]
        hash = generate_hash('123456')
        #bancoDeDados.buscarUsuarioParaLogar(email,hash)  
    return html    

#Páginas do cafeicultor:
@app.route('/cafeicultor')
def cafeicultor():
    html_file= open("templates/cafeicultor.html", "r") 
    html = html_file.read() 
    return html

@app.route('/cafeicultor/dados_pessoais')
def cafeicultorDadosPessoais():
    html_file= open("templates/dados_pessoais.html", "r") 
    html = html_file.read() 
    return html  

@app.route('/cafeicultor/vender')
def cafeicultorVender():
    html_file= open("templates/vender.html", "r") 
    html = html_file.read() 
    return html  

@app.route('/cafeicultor/editar')
def cafeicultorEditar():
    html_file= open("templates/editar.html", "r") 
    html = html_file.read() 
    return html 

'''
@app.route('/control/')
def control():
    file = open("control.html", "r") #Leitura do arquivo control.html para exibição deste na página
    html = file.read()
    #Caso o nome da amostra tenha sido enviado para essa página, ela será buscada no BD de modo a retornar
    #os parâmetros necessários (a1,b1,ts,sp,pv,k,tal)
    nome_amostra = str(request.args.get('nome' , "" )) 
    resposta = database.searchSampleDB(nome_amostra)
    if(resposta):
        a1 = resposta['a1']
        b1 = resposta['b1']
        ts = resposta['ts']
        sp = resposta['sp']
        global pv,k,tal,nome
        pv = resposta['pv']
        k = resposta['k']
        tal = resposta['tal']
        nome = resposta['nome']
        #Os valores encontrados no BD, substituem os valores padrão existentes na página web
        #E deste modo, poderão ser usados no plot do gráfico
        html= Avaliar(a1,"0.9930900",html)
        html= Avaliar(b1,"0.0058096",html)
        html= Avaliar(ts,"0.3",html)
        html= Avaliar(sp,"50",html)
        html= Avaliar(k,"valork",html)
        html= Avaliar(tal,"valortal",html)
    else:
        #As próximas renderizações irão usar os valores fixados no input ou um novo valor que venha a ser informado
        a1 = str(request.args.get('A1' , "" ))
        b1 = str(request.args.get('B1' , ""))
        ts = str(request.args.get('Amostragem' , ""))
        sp= str(request.args.get('SetPoint'      , ""))
        k = str(request.args.get('k'    , ""))
        tal = str(request.args.get('tal'    , ""))
    #Os demais campos são obtidos normalmente da página html (não tem relação com o BD)
    os= str(request.args.get('Overshoot'      , ""))
    tm= str(request.args.get('tempo'      , ""))
    modo=str(request.args.get('Modo' , ""))
    p = str(request.args.get('Proporcional'  , ""))
    i = str(request.args.get('Integral'      , ""))
    d = str(request.args.get('Derivativo'    , ""))
    fs = str(request.args.get('fixed_scale'    , "")) #Obtém se o campo escala fixa está selecionado
    ps = str(request.args.get('plot_sample'    , "")) #Obtém se o campo exibir amostras está selecionado
    pa = str(request.args.get('plot_all'    , "")) #Obtém se o campo comparar modos está selecionado
    #Caso algum campo esteja vazio/não foi informado um valor para ele, atribui-se um valor padrão
    if a1=="":
        a1="0.9930900"
    if b1=="":
        b1 = 0.0058096
    if ts=="":
        ts=0.3
    if sp=="":
        sp = 50
    if p=="":
        p = 0
    if p=="kp":
        p=0
    if i=="":
        i = 0
    if i=="ki":
        i = 0
    if d=="":
        d = 0
    if d=="kd":
        d = 0
    if fs=="":
        fs=0
    if ps=="":
        ps=0
    if pa=="":
        pa=0
    if k=="":
        k=1
    if k=="valork":
        k=1
    if tal=="":
        tal=1
    if tal=="valortal":
        tal=1
    if os=="":
        os=15
    if tm=="":
        tm=60
    #Para retenção dos valores nos inputs:
    html= Avaliar(a1,"0.9930900",html)
    html= Avaliar(b1,"0.0058096",html)
    html= Avaliar(ts,"0.3",html)
    html= Avaliar(sp,"50",html)
    html= Avaliar(os,"15",html)
    html= Avaliar(tm,"60",html)
    html= Avaliar(k,"valork",html)
    html= Avaliar(tal,"valortal",html)
    html= Avaliar(p,"kp",html)
    html= Avaliar(i,"ki",html)
    html= Avaliar(d,"kd",html)

    #Armazena ultimo SetPoint para a tela de monitoramento
    global LastSP
    LastSP=float(sp)
    #Chama a função para plotar o gráfico, informando todos valores necessários:
    retorno,timestamp=plotGrafico.plot(modo,float(a1),float(b1),float(ts),float(sp),
 float(p),float(i),float(d),int(fs),int(ps),int(pa),float(os),float(tm),float(k),float(tal),pv,nome)
    #A nova tabela e o novo gráfico são renderizados:
    html=html.replace("table_placeholder",retorno)
    html=html.replace("Results.png",("Results"+timestamp+".png"))
    return html 

#Função que verifica se o arquivo é permitido:
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/import/', methods=['GET', 'POST'])
def upload_file():
    html_file= open("upload.html", "r") #Leitura do arquivo upload.html para exibição deste na página
    html = html_file.read()
    if request.method == 'POST': #Se houve uma requisição do tipo Post, verificar:
        #Verifica se a requisição veio da seleção de uma amostra da lista:
        if "sample-select" in request.form: 
            nome_sample = request.form["sample-select"] #Neste caso, salva-se o nome da amostra selecionada
            html=html.replace("none","block") #habilita a exibição da mensagem (A amostraX esta pronta para ser simulada!)
            html=html.replace("amostraX",nome_sample) #substitui amostraX pelo nome da amostra selecionada
            #Esse nome também será adicionado no link que redireciona para a página 'control'
            html=html.replace("nome_amostra",nome_sample) 
        #Verifica se a requisição veio do upload:
        else:
            if 'file' not in request.files: #Validação do arquivo
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '': #Validação do arquivo
                print('No selected file')
            if file and allowed_file(file.filename):#Validação do arquivo
                resp = []
                degrau = []
                sp = request.form["SP"]
                nome = request.form["NAME"]
                ts = request.form["TS"]
                if(sp=="" or nome=="" or ts==""): #Validação dos dados
                    print("fields must be filled ....")
                else:
                    #Caso todas validações obtenham sucesso,os valores podem ser enviados para o BD
                    #Mas antes há um ajuste no formato dos dados
                    sp=float(sp)
                    ts=float(ts)
                    linhas = file.read().decode("utf-8") 
                    aux = 0
                    for i in range(len(linhas)):
                        if(linhas[i]=='\n'):
                            resp.append(float(linhas[aux:i]))
                            aux = i
                            degrau.append(sp)    
                    print("sending to db ....")
                    database.sendDB(nome,ts,resp,degrau)
            file.close()      
    retorno = database.searchDB() #Chama a função de busca das amostras, para atualizar a lista exibida na tela
    html=html.replace("table_placeholder",retorno) 
    return html
 

@app.route('/tmp/<path:path>')
def send_file(path):
    return send_from_directory('tmp', path)
'''

if __name__ == '__main__':
  app.run(debug=True) 
