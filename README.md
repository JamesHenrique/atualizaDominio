**Atualizador de Versão - Domínio Contábil**

Este projeto tem como objetivo realizar a verificação de atualizações de versão para um sistema
contábil (Domínio Contábil),
enviando e-mails para notificar os responsáveis caso haja uma nova versão ou atualização.

Estrutura do código:
1. **cria_arquivo_versao_dominio.py**: Este módulo cria um arquivo de versão (novaVersao.txt)
que contém a versão mais recente
 disponível do sistema.

3. **atualizaVersao.py**: Este módulo verifica se há atualizações de versão verificando o link do
FTP, e se houver, aciona o envio
 de e-mail de notificação.

5. **enviarEmail.py**: Este módulo é responsável por enviar os e-mails de notificação quando uma
atualização de versão está
 disponível.

Módulo `cria_arquivo_versao_dominio.py`:
A função `cria_arquivo_versao_dominio()` realiza os seguintes passos:
1. Acessa o link FTP para o sistema Domínio Contábil e obtém as versões mais recentes.
2. Verifica se há uma versão mais recente disponível com base na data.
3. Cria ou atualiza o arquivo `novaVersao.txt` com a versão mais recente.


Módulo `atualizaVersao.py`:
A função `verifica_atualizacao_dominio()` realiza os seguintes passos:
1. Lê o arquivo `novaVersao.txt` para saber a versão atual do sistema.
2. Acessa o link FTP e verifica se há atualizações de versão.
3. Se houver uma atualização, chama a função `atualizacaoDisponivel()` que envia o e-mail de
notificação.


Módulo `enviarEmail.py`:
O módulo `enviarEmail.py` contém duas funções:
1. **atualizacaoDisponivel**: Envia um e-mail informando sobre a disponibilidade de uma
atualização.
2. **atualizacaoVersao**: Envia um e-mail informando que houve uma atualização de versão.


Requisitos do Sistema:
Para executar o projeto, os seguintes pacotes Python são necessários:
- requests
- beautifulsoup4
- smtplib (já integrado no Python)
- email.message (já integrado no Python)
Arquivo `requirements.txt`:
beautifulsoup4==4.12.3
certifi==2024.6.2
charset-normalizer==3.3.2
idna==3.7
requests==2.32.3
soupsieve==2.5
urllib3==2.2.1


Como Usar:
1. Execute o arquivo principal:
 python main.py
