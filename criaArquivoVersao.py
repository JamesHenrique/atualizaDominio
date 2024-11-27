from  datetime import datetime
import requests
from bs4 import BeautifulSoup
from enviarEmail import atualizacaoVersao


def cria_arquivo_versao_dominio():

    link = "https://ftpdownload.dominiosistemas.com.br/atualizacao/contabil/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
    requisicao = requests.get(link,headers=headers)


    dataHoje = datetime.now()
    dataFormatada = dataHoje.date()


    site = BeautifulSoup(requisicao.text,"html.parser") #deixa as informações mais organizadas

    file_path = 'novaVersao.txt'


    def get_latest_version():
        
        
        # Encontrar a versão mais recente (exemplo: 104a07, 104a08, etc.)
        versions = [a.text for a in site.find_all('a') if a.text.startswith('10')]
        
        latest_version = sorted(versions)[-1] if versions else None
        
        return latest_version


    def checkDate():
        
        campo = site.find("pre").get_text()
        
        hoje = datetime.now() #PEGA DATA DE HOJE
        
        dia_atual = hoje.date()

        formatar = dia_atual.strftime("%Y-%m-%d")
        
        buscaData = campo.find(formatar)
        
        
        if buscaData > 1:
            return True
        else:
            return False
        
        
    def createFile(version):
        with open(file_path,'w') as file:
            file.write(version)
        
        
    if checkDate():
        print('Tem atualização de mudança de versão ')
        createFile(get_latest_version())
        atualizacaoVersao()
    else:
        createFile(get_latest_version())
        print('Não tem atualização de versão')
        

