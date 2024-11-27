from atualizaVersao import verifica_atualizacao_dominio
import time as tm
from criaArquivoVersao import cria_arquivo_versao_dominio 


cria_arquivo_versao_dominio()
tm.sleep(5)
verifica_atualizacao_dominio()

