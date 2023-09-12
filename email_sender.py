from email.message import EmailMessage #went to google and set up in gmail 2 factor verification ->Security->App password ->create new one
from email_sender import password #the password  generated from app 
import ssl #import 
import smtplib

email_sender = 'mshange2@gmail.com' #your email address
email_password =  password #the password you generated in app password

email_receiver = 'jayipo1420@sesxe.com' # generated email from temp email.org 

subject = "Don't forget to sent me feedback " # what you want towrite in the subject
body = """ 
When you go through my work don't forget to send me some feedback
""" # What you want to write in the body

em = EmailMessage
em['From'] = email_sender 
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string())
