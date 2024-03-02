import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your name'
email['to'] = 'email_you_are_sending_to'
email['subject'] = 'totaly not a scam'

email.set_content(html.substitute({'name': 'name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('your_email_address', 'your_password')
  smtp.send_message(email)
  print('all good boss!')