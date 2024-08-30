import requests as re
from bs4 import BeautifulSoup
from  datetime import datetime
from enviarEmail import atualizacaoDisponivel


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}


with open('novaVersao.txt','r') as file:
    versao = file.read()
    link = f'https://ftpdownload.dominiosistemas.com.br/atualizacao/contabil/{versao}atualizacoes/'
    requisicao = re.get(link,headers=headers)
    site = BeautifulSoup(requisicao.text,"html.parser") #deixa as informações mais organizadas
    
    campo = site.find("pre").get_text()
    hoje = datetime.now() #PEGA DATA DE HOJE
    
    dia_atual = hoje.date()
    formatar = dia_atual.strftime("%Y-%m-%d")
    
    buscaData = campo.find(formatar)

    
    if buscaData > 1:
        print('tem atualização')
        atualizacaoDisponivel()
    else:
        print('não tem atualização')
        
    
