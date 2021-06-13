# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:19:44 2021

@author: Admin
"""

import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np
from pathlib import Path
class Email:
    
    
    def __init__(self, sender_email, password, subject, body):
    
        self.subject = subject
        self.body = body
        self.sender_email = sender_email
        self.password = password
        self.logs = []
        self.login = True
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.login(self.sender_email, self.password)
            except Exception as e:
                self.login = False
                     
                     
    
    
    def sendEmail(self,receiver_email, filename):
        if self.login == False:
            return 'Error on login to your business account'
        self.logs = []
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = self.subject
        self.run = True
        message.attach(MIMEText(self.body, "plain"))
        
        my_file = Path(filename)
        if my_file.is_file():
           self.run = True 
           self.logs = self.logs.append('The file does not exist')
        else:
            self.run = False
            
        if self.run == True:
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
    
            encoders.encode_base64(part)
            
    
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            
    
            message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, text)
                return 'Success on sending email to ' + receiver_email
            except Exception as e:
                     return 'Error Sending the email: ' + receiver_email
                 