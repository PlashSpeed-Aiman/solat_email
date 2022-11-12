import smtplib,ssl
import os
from dotenv import load_dotenv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass


def send_email(msg:str) -> None:
    load_dotenv()
    smtp_server : str = os.getenv('SMTP_SERVER')
    port : int = os.getenv('SMTP_PORT_NUM')
    sender_email : str = os.getenv('SENDER_EMAIL_VAR')
    receiver_email : str = 'amarsyerif8@gmail.com'
    password:str  = os.getenv('EM_PASS')

    context : ssl.SSLContext = ssl.create_default_context()
    message = """
    Subject: Hi there

    This message is sent from Python.

    """

    try:
        server = smtplib.SMTP(smtp_server,port,timeout=120)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, msg)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
