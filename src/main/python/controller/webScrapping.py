#pip install requests
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

class WebScrapping(object):
    def cotacaoCafe(self,tipo,classificacao_bebida):
        html = requests.get("http://cccmg.com.br/cotacao-do-cafe/").content
        soup = BeautifulSoup(html, 'html.parser')
        tabela = soup.find('table', attrs={'class':'tabela-resultados'})
        linhas = tabela.find_all('td')
        achou = False
        for i in linhas:
            if achou==True:
                preco=i.text
                preco=preco.replace(',','.')
                preco=float(preco.replace('R$ ',''))
                break
            if classificacao_bebida in i.text and tipo in i.text:
                achou = True
        return preco
    