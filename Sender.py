# email:     UvicConfessionsandCrushes
# password:  EdwardSnowdendontgotshitonme
# (remove when repository goes public)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sender:
    def __init__(self):
        pass
    def send_mail(self, email, title, subject):
        # Create and format the message,
        # specifying the sender name as it appears in an inbox,
        # the recipient, and the subject line
        msg = MIMEMultipart('Alternative')
        msg['From'] = title
        msg['To'] = email
        msg['Subject'] = subject
        
        # Opens and reads the html file with the message, attaching it to the message object
        html_open = open("Message.html")
        html = html_open.read()
        msg.attach(MIMEText(html, 'html'))

        # Opens a connection to the stmp gmail server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        # Prompts the user for the password, logging into the email account
        password = input("Password ")
        server.login("UvicConfessionsandCrushes", password)

        # Sends email
        server.sendmail("UvicConfessionsandCrushes@gmail.com", email, msg.as_string())