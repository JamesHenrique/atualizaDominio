from email.message import EmailMessage
import smtplib
from  datetime import datetime
import os



hoje = datetime.now()
dia_atual = hoje.date()
formatar = dia_atual.strftime("%Y-%m-%d")


assunto = "Atualização da Dominio"
sender = "I.james1304@outlook.com"
recipient = "claudinojames1702@gmail.com"
senha = os.environ['senha_email']




def atualizacaoDisponivel():    
    
     
    data_obj = datetime.strptime(formatar, '%Y-%m-%d')

    data_formatada = data_obj.strftime('%d-%m-%Y')
    
    message = f"<H1>Atualização disponível! Hoje dia <strong>{data_formatada}</strong> </H1>"
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = f"{assunto}"
    email.set_content(message, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, senha)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()
    print("ATUALIZAÇÃO DISPONÍVEL email enviado com sucesso")
    
    

def atualizacaoVersao():
    data_obj = datetime.strptime(formatar, '%Y-%m-%d')

    data_formatada = data_obj.strftime('%d-%m-%Y')
    message = f"<H1>Atualização VERSÃO! Hoje dia <strong>{data_formatada}</strong> </H1>"
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = f"{assunto}"
    email.set_content(message, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, senha)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit() 
    print("ATUALIZAÇÃO DISPONÍVEL email enviado com sucesso")
        