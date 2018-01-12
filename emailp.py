import smtplib
import email
from email.mime.text import MIMEText
from email.message import compat32
from email.base64mime import b64encode
import json
import csv
import imaplib


mail_host= stmp.xxx.com
mail_user= shuhao@ctssea.com
mail_pass= "Hsh19930928"
recevier = ''
message= MIMEText('Send email test','plain','utf-8')
message['From'] = 'Python'+ '<'mail_user'>'
message['Tp'] = recevier
message['Subject'] = 'Python email test'

class b64encode:
    def