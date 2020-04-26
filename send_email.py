import smtplib
from email.message import EmailMessage

email = EmailMessage()  # email object
email['from'] = 'Manshul Arora'
email['to'] = 'arora.manshul@gmail.com'
email['subject'] = 'Check Check Manshul'
email.set_content('Hey!! Wassup Manshul')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('manshul.dummy@gmail.com', '***')
    smtp.send_message(email)
    print('all good boss!')
