

from email.message import EmailMessage
import smtplib
from datetime import datetime
import os
from config import SENHA_EMAIL,REMETENTE,DESTINATARIO

hoje = datetime.now()
dia_atual = hoje.date()
formatar = dia_atual.strftime("%d")
dia_da_semana = datetime.now().weekday()

match dia_da_semana:
    case 0:
        dia_da_semana = "Segunda-feira"
    case 1:
        dia_da_semana = "Terça-feira"
    case 2:
        dia_da_semana = "Quarta-feira"
    case 3:
        dia_da_semana = "Quinta-feira"
    case 4:
        dia_da_semana = "Sexta-feira"
    case 5:
        dia_da_semana = "Sábado"
    case 6:
        dia_da_semana = "Domingo"

# Configurações do remetente e destinatário

sender = REMETENTE
senha = SENHA_EMAIL
recipient = DESTINATARIO[0]

assunto = "Atualização da Dominio"

# Função para enviar o e-mail
def atualizacaoDisponivel():

    mensagem = f"<H1>Atualização disponível! {dia_da_semana} dia <strong>{formatar}</strong> </H1>"
    
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = assunto
    email.set_content(mensagem, subtype="html")

    # Configurar o servidor SMTP do Gmail
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls()  # Iniciar a conexão segura
        smtp.login(sender, senha)  # Realizar o login
        smtp.sendmail(sender, recipient, email.as_string())  # Enviar o e-mail

    print("E-mail enviado com sucesso!")



def atualizacaoVersao():
    mensagem = f"<H1>Atualização de <strong> versão Domínio Contabil</strong>! Hoje {dia_da_semana} dia <strong>{formatar}</strong>  </H1>"
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = assunto
    email.set_content(mensagem, subtype="html")

    # Configurar o servidor SMTP do Gmail
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls()  # Iniciar a conexão segura
        smtp.login(sender, senha)  # Realizar o login
        smtp.sendmail(sender, recipient, email.as_string())  # Enviar o e-mail

    print("E-mail enviado com sucesso!")


        