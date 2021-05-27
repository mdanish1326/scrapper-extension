# mailing logic in this file
import os
import smtplib
from email.message import EmailMessage


EMAIL_ADD = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

def send_mail(mail, prd_name, prd_price, link):
    body = f"""The price of the product- {prd_name}, has dropped.
            \nThe Dropped Price is: {prd_price}
            \nFollow This link to grab your product: {link}\n\n\n\t\t\t\t
             This is a system generated mail..."""
    msg = EmailMessage()
    msg['Subject'] = 'PRICE DROPPED !!'
    msg['From'] = EMAIL_ADD
    msg['To'] = mail
    msg.set_content(body)
    print(mail)
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADD, EMAIL_PASS)
        smtp.send_message(msg)



